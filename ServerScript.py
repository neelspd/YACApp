# -*- coding: utf-8 -*-
"""
Created on Sat May  8 15:25:09 2021

@author: Neel Shah
"""

import flask

app = flask.Flask(__name__, static_url_path='', static_folder='Frontend/static', template_folder='Frontend/templates')

@app.route('/yacapp', methods=['GET'])
def retrunSitemap():
    return app.send_static_file('sitemap.html')


@app.route('/', methods=['GET'])
def home():
    return "Its Working, move on jackass"


@app.route('/logout')
def logout():
    return flask.redirect(flask.url_for('/yacapp'))

app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
