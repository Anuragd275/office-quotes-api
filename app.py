from flask import *
import json, time
import random as rand
from db import quote_fetcher

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    # current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    # data_set = {'Page': 'Home', 'Message': "Success on home", 'Time': current_time}
    # json_dump = json.dumps(data_set)
    # return json_dump

    return render_template('index.html')

@app.route('/quote/', methods=['GET'])
def get_quote():


    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    data_set = {'Page': 'Quote', 'Message': "Successfully landed on quotes page", 'quote': f'{quote_fetcher()}', 'details': 'This data is fetched from Mongo DB'}
    
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/user/', methods=['GET'])
def user_page():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    user_query = str(request.args.get('user'))
    data_set = {'Page': 'Request', 'Message': f"Success on User for {user_query}", 'Time': current_time}
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(port=5600)
