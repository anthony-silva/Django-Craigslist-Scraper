# Create your views here.
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from .models import *
from scraper.forms import SearchForm

BASE_CRAIGSLIST_URL = 'craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


def CraigslistIndexView(request):
    form = SearchForm()
    return render(request, 'base.html', {'form': form})


def CraigslistResultsView(request):
        search = request.GET.get('search')
        city = request.GET.get('city')
        obj = Search(search=search, city=city)
        obj.save()
        city_url = ''.join(city.split())
        final_url = 'https://' + city_url + '.' + BASE_CRAIGSLIST_URL.format(quote_plus(search))
        response = requests.get(final_url)
        data = response.text
        soup = BeautifulSoup(data, features='html.parser')
        post_listings = soup.find_all('li', {'class': 'result-row'})
        final_postings = []

        # Parse text data for craigslist results
        for post in post_listings:
            post_title = post.find(class_='result-title').text
            post_url = post.find('a').get('href')

            if post.find(class_='result-price'):
                post_price = post.find(class_='result-price').text
            else:
                post_price = 'N/A'

            if post.find(class_='result-image').get('data-ids'):
                post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
                post_image_url = BASE_IMAGE_URL.format(post_image_id)
                print(post_image_url)
            else:
                post_image_url = 'https://craigslist.org/images/peace.jpg'

            final_postings.append((post_title, post_url, post_price, post_image_url))

        # context object for front end
        form = SearchForm()
        stuff_for_frontend = {
            'form': form,
            'search': search,
            'final_postings': final_postings,
        }

        return render(request, 'scraper/index.html', stuff_for_frontend)
