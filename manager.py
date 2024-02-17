from database import Database
from flask import Flask, render_template, request, redirect, url_for
import os
import ast
import time

from werkzeug.utils import secure_filename
from bardapi import Bard

from vector_classes import vectordb, llm, article, author

app = Flask(__name__)

# Define the upload folder
db_connection = {'host': 'localhost', 'user': 'root', 'password': 'Mariaw57!', 'database': 'news'}
app.config["db"] = Database( **db_connection )

llm = llm(Bard(token='dAhcWNK3jSiJ4HfkH3ovmWh6PBZxtztYGZ8Kj6-1TNKh6bHr-rnEC3Hk8Ntx9ifNoWLvkw.'))

vector_db_connection = {
    'api_key': '269730f8-72c2-4b39-87e8-ccd0a568405a',
    'enviroment': 'gcp-starter',
    'summarizer': llm
}

app.config["vdb"] = vectordb( **vector_db_connection)

@app.route("/", methods=['GET', 'POST'])
def index():
    return "install sucsess"

if __name__ == "__main__":
    app.run(debug=True, port=8001)