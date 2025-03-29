from flask import Flask,render_template,request,session, redirect, url_for
from flask_oauthlib.client import OAuth
from flask_cors import CORS, cross_origin
from google.oauth2 import id_token
from google.auth.transport import requests
import pymongo,certifi,json,time,copy,re
from bs4 import BeautifulSoup
import requests as rq

mongoUrl = "mongodb+srv://dkru4jo6:1300rd1684@soulforge.xxmrjtk.mongodb.net/?retryWrites=true&w=majority"
host = 'https://soul-forged-resourcs-map.vercel.app/'
# host = 'http://localhost:3000/'
def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', 'resourceMap', resourceMap)
    
    return app

dbName = 'resourceMap'
# dbName = 'resourceMapTest'
verNum = '1-8-2'
whVerNum = '0-0-1'
def resourceMap():
    return render_template('Shoot.html')