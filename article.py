from bardapi import Bard
from sentence_transformers import SentenceTransformer

from database import Database
from vector_classes import vectordb, llm, article, author

import time
import os
from tqdm import tqdm
from newsapi import NewsApiClient 

import requests

import secrets
import string

def generate_random_string(length=10):
    #function to generate a random string
    characters = string.ascii_letters + string.digits  

    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    
    return random_string

if __name__ == '__main__':

    #these tokens have expired since the release of gemini
    bard_token = 'BARD_TOKEN'
    bard_token = 'BARD_TOKEN'


    bard = Bard(token=bard_token)

    #to regenerate this code, a different model has to be used
    text = llm(bard=bard)
    
    #this contains the api keys for the pinecone db
    #user must go to pinecoe and acquire the api keys from there upon creation of an account. 
    api_key = ''
    enviroment = 'gcp-starter'

    db = vectordb(
        api_key=api_key,
        enviroment=enviroment,
        summarizer=text,
    )

    #database ran locally, mysql. User has to input their own credentials. 
    db_connection = {
    'host': 'localhost',
    'user': 'root',
    'password': '', 
    'database': ''
    }

    author = author(
        vdb=db, 
        db=Database( **db_connection ), 
        llm=text,
    )

    #this section is non-operational.
    url = ('https://newsapi.org/v2/top-headlines?'
            'country=uk&'
            'apiKey=517fc122218e49b3a77ee030ed14a982')
    

    newsapi = NewsApiClient(api_key='517fc122218e49b3a77ee030ed14a982')
    all_articles = newsapi.get_everything(q='climate',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
    count = 0
    print("printing", all_articles["articles"])
    for article in all_articles.get("articles", ''):
        filename = f"{generate_random_string(6)}.txt"
        file_path = os.path.join("breaking", filename)

        with open(file_path, 'w', encoding='utf-8') as file:
            paragraphs = article.get('description', '').split('\n') or ""
            file.write('\n'.join(paragraphs))  
        
    print("sucsess loaded")



    



