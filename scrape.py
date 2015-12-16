import urllib2
from bs4 import BeautifulSoup
import re
#import codecs
import json
from flask import *
from flask import render_template
import requests
from flask_sslify import SSLify

#Grabs a random wikipedia article
app = Flask(__name__)
sslify = SSLify(app)

#returns list of images in json at 127.0.0.1:5000/scrape_images
@app.route('/scrape_images', methods=['POST', 'GET'])
def scrape_images():
    url = request.args.get('url')
    image_page = BeautifulSoup(urllib2.urlopen(url).read())
    header = image_page.find("h1")
    image_page = image_page.findAll('img')
    image_url_list = []
    image_url_list.append(str(header))
    for image_tag in image_page:
       image_tag['src'] = image_tag['src'].replace("thumbs/thumbs_", "")
       image_url_list.append(image_tag['src'])
    image_list_json = json.dumps(image_url_list)
    return image_list_json

#The main page!
@app.route('/')
def main_page(name=None):
    return render_template('index.html', name=name)

#This is where pinterest stuff will go!
@app.route('/authenticate_pinterest')
def pinterest():
    payload = {'response_type':'code',
                'client_id':"4806877807896439056",
                'scope':('read_public', 'write_public'),
                'redirect_uri':'https://localhost:5000'}
    r = requests.get('https://api.pinterest.com/oauth/', params = payload)
    return redirect(r.history[0].url)


if __name__ == '__main__':
    app.run(debug=True)
