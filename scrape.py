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
@app.route('/grab_article_en')
def grab_random_article():
    payload = {'response_type':'code', 
                'client_id':"4806877807896439056", 
                'scope':('read_public', 'write_public'),
                'redirect_uri':'https://localhost:5000'}
    r = requests.get('https://api.pinterest.com/oauth/', params = payload)
    print(r.url)
    image_page = BeautifulSoup(urllib2.urlopen('http://www.freshdesigner.com/figure-drawing-reference/').read())    
    header = image_page.find("h1")
    image_page = image_page.findAll('img')
    image_url_list = [] 
    image_url_list.append(str(header))
    for image_tag in image_page:
       image_tag['src'] = image_tag['src'].replace("thumbs/thumbs_", "")
       image_url_list.append(image_tag['src']) 

    

    image_list_json = json.dumps(image_url_list)
    
    #f = codecs.open('wiki_page', 'w', "utf-8")
    #f.write(wiki_json)
    #f.close()
    
    
    return image_list_json


@app.route('/')
def main_page(name=None):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)

