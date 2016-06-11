import os
import requests
import operator
import re
import nltk
from flask import Flask, Blueprint, Response, render_template, request, jsonify
from stop_words import stops
from collections import Counter
from bs4 import BeautifulSoup
from rq import Queue
from rq.job import Job
from worker import conn
# flask-peewee bindings
from flask_peewee.db import SqliteDatabase
from flask_peewee.rest import RestAPI

from models.company import Company
from models.load import Load
from models.user import User

app = Flask(__name__)
app.config.from_object(__name__)
q = Queue(connection=conn)

api = RestAPI(app)
api.register(User)
api.register(Company)
api.register(Load)
api.setup()

# def count_and_save_words(url):
#     errors = []
#     try:
#         r = requests.get(url)
#     except:
#         errors.append(
#             "Unable to get URL. Please make sure it's valid and try again."
#         )
#         return {"error": errors}
#
#     # text processing
#     raw = BeautifulSoup(r.text, "html.parser").get_text()
#     nltk.data.path.append('./nltk_data/')  # set the path
#     tokens = nltk.word_tokenize(raw)
#     text = nltk.Text(tokens)
#
#     # remove punctuation, count raw words
#     nonPunct = re.compile('.*[A-Za-z].*')
#     raw_words = [w for w in text if nonPunct.match(w)]
#     raw_word_count = Counter(raw_words)
#
#     # stop words
#     no_stop_words = [w for w in raw_words if w.lower() not in stops]
#     no_stop_words_count = Counter(no_stop_words)
#     from models.result import Result
#     print(url)
#     data = {}
#     result = Result(url=url, result_all=data)
#     print(result)
#     result.save()
#     return result.id



@app.route('/', methods=['GET', 'POST'])
def index():
    results = {}
    # if request.method == "POST":
    #     # get url that the person has entered
    #     url = request.form['url']
    #     if 'http://' not in url[:7]:
    #         url = 'http://' + url
        # job = q.enqueue_call(
        #     func="hello.count_and_save_words", args=(url,), result_ttl=5000
        # )
        # print(job.get_id())

    return render_template('index.html', results=results)

# @app.route("/results/<job_key>", methods=['GET'])
# def get_results(job_key):
#     from flask import jsonify
#     job = Job.fetch(job_key, connection=conn)
#
#     if job.is_finished:
#         print(job)
#         query = Result.select().where(Result.id == job.result)
#         result = query.first()
#         results = sorted(
#             result.result_no_stop_words.items(),
#             key=operator.itemgetter(1),
#             reverse=True
#         )[:10]
#         return jsonify(results)
#     else:
#         return "Nay!", 202

def validate(phone_number):
    print(phone_number)
    Response(phone_number, mimetype='application/json')

db = SqliteDatabase('example.db')
if __name__ == '__main__':
    db.connect()
    db.create_tables([User, Company, Load], safe=True)
    app.run()
