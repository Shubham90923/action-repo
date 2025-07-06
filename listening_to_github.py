from flask import json
from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongodb://…')
db = client['github_webhooks']
coll = db['events']

@app.route('/webhook', methods=['POST'])
def webhook():
    event = request.headers.get('X-GitHub-Event')
    data = request.json
    # Extract only the needed info based on event type:
    record = {
        'event': event,
        'author': ...,
        'from_branch': ..., # only PR or merge
        'to_branch': ...,
        'timestamp': datetime.utcnow()
    }
    coll.insert_one(record)
    return '', 204

if __name__ == '__main__':
        app.run(debug=True, host='localhost', port=8000)