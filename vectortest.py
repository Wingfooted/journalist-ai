from bardapi import Bard
from vector_classes import vectordb, llm, article, author
from sentence_transformers import SentenceTransformer
from database import Database

import time
from tqdm import tqdm

bard_token = 'BARD_TOKEN'
if __name__ == '__main__':

    bard = Bard(token=bard_token)

    #find a new llm model since this one no longer works. 
    text = llm(bard=bard)
    
    #get pinecone api key from pinecone website
    api_key = 'PINECONE_API_KEY'
    enviroment = 'gcp-starter'

    db = vectordb(
        api_key=api_key,
        enviroment=enviroment,
        summarizer=text,
    )

    db_connection = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mariaw57!', 
    'database': 'news'
    }

    author = author(
        vdb=db, 
        db=Database( **db_connection ), 
        llm=text,
    )

    a = article("articles/PLS.txt")
    b = article("articles/Lithium.txt")
    c = article("articles/test.txt")
    #db.vector_wipe()
    test_a = {
                "a": "articles/PLS.txt",
                "b": "articles/Lithium.txt"
            }
    #run loop 1
    run = False

    while run:
        usr = input("$ ")

        if usr == "info":
            print(db.info())

        elif usr == "wipe":
            db.vector_wipe()
            for i in tqdm(range(15)):
                time.sleep(1)
        elif usr == "ss":
            q = input("Q: ")
            ks = input("Ks: ") or 3

            print(
                db.simmilarity_search (
                queries=[q],
                ks=int(ks)
                )
            )
        elif usr == "exit":
            run = False    
        elif usr == "tt":
            print(db.tag(
                text="Lithium and comodities traders are looking forward to large government investments into tech. Government has invested lots in the current markets which means that there is lots of money in the current art history market of technologoical market of art government art markets testing the art markets"
            ))
        elif usr == "":
            pass


        elif usr == "prod":
            prompt = input("prompt: ")

            research = text.research(prompt, n=3)
            print ("research output ", research)
            
            case = []
            for q in research:
                answer = db.simmilarity_search(
                    queries=[q],
                    ks=3
                )
                print(f"Q/A test point ###############, answer: {answer}, question: {q}")

                print("testing answer formatting")
                answer_content = [content['metadata']['content'] for content in answer]
                print(answer_content)
                #ADD A TOTAL TAGS SYSTEM. 

                # ADD A THRESHOLD FOR SIMMILARITY. COMPARE ONLY THE MOST SIMMILAR/RELEVATN RESPONSES
                #ADD A BIT OF RANDOMNESS DURING THE RANKING PROCESS.

                #p for paragraph, q for question
                p = text.answer(question=q, xanswer='\n'.join(answer_content))
                case.append(p)
                #MAKE THE CASE WRITING PROCESS MORE ITERATIVE. ADD AN EDITING AND REVIEW FEATURE SOMEHOW.
            
            print("case output: ", case)
            article = text.write(case=case, prompt=prompt)
            print("article output: ", article)


        elif usr in test_a:
            db.vectorize_article(
                article=article(path=test_a[usr]),
                LOC="LITH2"
            )

    run = True  

    while run:
        usr = input("$ ")
        if usr == "exit":
            run = False
        elif usr == "locs":
            author.test("Scientia Naturae Journal")
        elif usr == "prime":
            author.prime("Scientia Naturae Journal")
        elif usr == "write":
            prompt = input("prompt: ")
            print(author.write(prompt))
        elif usr == "folder":
            folder = input("folder: ")
            author.load_batch("BIOL1", _folder=folder)

    #self, api_key, enviroment, summarizer, index_name='AIO-INFO'
    #Embedding model.





