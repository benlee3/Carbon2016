#!flask/bin/python
from urllib2 import Request, urlopen, URLError
from flask import Flask, render_template, jsonify
import urllib, json
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

try:   #For python 2
    from urllib2 import Request, urlopen, URLError
except ImportError:		#For python 3
	from urllib import request
	from urllib.request import urlopen
	from urllib.error import URLError

from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def enter():

	request = Request('http://api.reimaginebanking.com/customers?key=fdcdbc9f4d339cd5970c2d87c8e8d16f')

	try:
		response = urllib.urlopen('http://api.reimaginebanking.com/customers?key=fdcdbc9f4d339cd5970c2d87c8e8d16f')
		customers = json.loads(response.read())
		acct_response = urllib.urlopen('http://api.reimaginebanking.com/customers/'+customers[0]['_id']+'/accounts?key=fdcdbc9f4d339cd5970c2d87c8e8d16f')
		accounts = json.loads(acct_response.read())
		customer_name = customers[0]['first_name']
		checking = accounts[2]['balance']
		return render_template('index.html', customer=customer_name, balance=checking)
	except URLError, e:
		return "404 error"



if __name__ == '__main__':
    app.run()
