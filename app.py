# https://cloud.ibm.com/apidocs/assistant-v2?code=python

from flask import redirect, render_template, jsonify,request,url_for
import json

import os
import flask
from pdfminer.high_level import extract_text
from watsonxAI.EmailNotification import read_unread_outlook_emails

EmailCOunt = read_unread_outlook_emails()

app = flask.Flask(__name__)
app.secret_key = 'hello'


    
# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/', methods=['POST','GET'])
def index():
    
    
    
    return render_template('./index.html',EmailCOunt=EmailCOunt)





if __name__ == '__main__':
    app.run(debug=True)