# https://cloud.ibm.com/apidocs/assistant-v2?code=python

from flask import redirect, render_template, jsonify,request,url_for
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

import os
import flask
from pdfminer.high_level import extract_text

app = flask.Flask(__name__)
app.secret_key = 'hello'

# Watson Assistant credentials
API_KEY = '5Bx7ALnm9_bks7pOMaY7XPZkjnO9HSa_DyL0vfl6vDGT'
# ASSISTANT_ID = '81c56a4e-7066-4513-998a-93f0efb702c0'
# ASSISTANT_ID = '0c2bbac8-9232-45cd-b1c8-1500a0e104be' # instance id
ASSISTANT_ID = '7f4b68e3-b059-4617-a308-90204b511092'
ASSISTANT_URL = 'https://api.us-south.assistant.watson.cloud.ibm.com'

authenticator = IAMAuthenticator(API_KEY)
assistant = AssistantV2(
    version='2021-11-27',
    authenticator=authenticator
)

assistant.set_service_url(ASSISTANT_URL)

session = assistant.create_session(ASSISTANT_ID).get_result()
session_json = json.dumps(session)
session_dict = json.loads(session_json)
session_id = session_dict['session_id']

# Create a session with the assistant
# session_response = assistant.create_session(
#     assistant_id = ASSISTANT_ID
# ).get_result()
# session_id = session_response['session_id']


response = assistant.message(
            assistant_id=ASSISTANT_ID,
            session_id=session_id,
            input={
                'message_type': 'text',
                'text': 'Provide document summary flask response',
            }
            ).get_result()

summary = response['output']['generic'][0]['text']

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    response = assistant.message(
        assistant_id=ASSISTANT_ID,
        input={
            'text': user_input
        }
    ).get_result()

    reply = response['output']['generic'][0]['text']
    return jsonify({'reply': reply})



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)