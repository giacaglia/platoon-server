import os
import requests
import operator
import re
import nltk
from flask import Flask, render_template, request, jsonify
from stop_words import stops
from collections import Counter
from bs4 import BeautifulSoup
from rq import Queue
from rq.job import Job
from worker import conn
# flask-peewee bindings
from flask_peewee.db import Database, SqliteDatabase
from flask_peewee.auth import Auth
import json

# configure our database
DATABASE = {
    'name': 'example.db',
    'engine': 'peewee.SqliteDatabase',
}
app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object(__name__)
db = Database(app)
auth = Auth(app, db)

q = Queue(connection=conn)

from models import *

def count_and_save_words(url):
    errors = []

    try:
        r = requests.get(url)
    except:
        errors.append(
            "Unable to get URL. Please make sure it's valid and try again."
        )
        return {"error": errors}

    # text processing
    raw = BeautifulSoup(r.text, "html.parser").get_text()
    nltk.data.path.append('./nltk_data/')  # set the path
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)

    # remove punctuation, count raw words
    nonPunct = re.compile('.*[A-Za-z].*')
    raw_words = [w for w in text if nonPunct.match(w)]
    raw_word_count = Counter(raw_words)

    # stop words
    no_stop_words = [w for w in raw_words if w.lower() not in stops]
    no_stop_words_count = Counter(no_stop_words)
    print("models")
    # save the results
    # try:
    from models import Result
    print("BEFORE URL")
    print(url)
    # raw_word_count = json.dumps(raw_word_count)
    data = {}
    no_stop_words_count = '{}'
    # print(raw_word_count)
    # print(no_stop_words_count)
    result = Result(url=url, result_all=data)
                # result_no_stop_words=no_stop_words_count
            # )
    print("created it")
    print(result)
    result.save()
    return result.id
    # except:
    #     print("error")
    #     errors.append("Unable to add item to database.")
    #     return {"error": errors}


@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    if request.method == "POST":
        # get url that the person has entered
        url = request.form['url']
        if 'http://' not in url[:7]:
            url = 'http://' + url
        job = q.enqueue_call(
            func="hello.count_and_save_words", args=(url,), result_ttl=5000
        )
        print(job.get_id())

    return render_template('index.html', results=results)

@app.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):
    from flask import jsonify
    job = Job.fetch(job_key, connection=conn)

    if job.is_finished:
        print(job)
        query = Result.select().where(Result.id == job.result)
        result = query.first()
        results = sorted(
            result.result_no_stop_words.items(),
            key=operator.itemgetter(1),
            reverse=True
        )[:10]
        return jsonify(results)
    else:
        return "Nay!", 202

if __name__ == '__main__':
    database = SqliteDatabase('example.db')
    database.connect()
    database.create_tables([auth.User, Result])
    # data = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    # url = "http://en.wikipedia.org/wiki/Firebase"
    # result = Result(url=url, result_all=url)
    # print(result)
    # result.save()
    app.run()
