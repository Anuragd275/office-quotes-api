from flask import *
import json, time
from bson.objectid import ObjectId
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://admin:root-admin@first.cndzcil.mongodb.net/?retryWrites=true&w=majority")

# Select Database
db = client.get_database('first')

#Select collection
collection = db.office_quotes

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/quote/', methods=['GET'])
def get_quote():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    data_set = {'Page': 'Quote', 'Message': "Successfully landed on quotes page", 'quotes': f'{quote_fetcher()}', 'Time': current_time}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/limit/', methods=['GET'])
def limit_quote_fetcher():
    limited_value = str(request.args.get('limit'))
    data_set = {'Status': 'Successful', 'Message': f'Results {limited_quote_fetcher(limited_value)}'}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/user/', methods=['GET'])
def user_page():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    user_query = str(request.args.get('user'))
    data_set = {'Page': 'Request', 'Message': f"Success on User for {user_query}", 'Time': current_time}
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/add/', methods=['GET', 'POST'])
def add_quote():
    if request.method == 'POST':
        quote = request.form.get('quote')
        author = request.form.get('author')
        
        # Insert the values into MongoDB
        collection.insert_one({'quote': quote, 'author': author})

        # Redirect to a success page or render a success message
        return 'Values inserted successfully'
    
    # Render the HTML form
    return render_template('add_quote.html')

@app.route('/delete/', methods=['GET', 'POST', 'DELETE'])
def delete_quote():
    if  request.method == 'DELETE'or request.method == 'POST':
        quote_id = request.form.get('quote_ID')

        # Delete the quote from MongoDB
        collection.delete_one({'_id': ObjectId(quote_id)})

        # Redirect to a success page or render a success message
        return (f"Deleted this: ObjectId('{quote_id}')")
    
    # Render the HTML form
    return render_template('delete_quote.html')


if __name__ == '__main__':
    app.run(port=5600)
