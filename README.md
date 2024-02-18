# journalist-ai

## 🛑 NOTE: Project Discontinuation 🛑
The bulk of large language model capability and writing ability of this project was run off google's Bard. However, as of the 10/2/24, Google Bard is now Gemini and the Bard Api utilized to make this project is not as stable. Consequently the project may not work, however provided is example_written_article.txt, which is a representation of what this tool was capable of creating. 

## AI Journalist Overview
This was a project to implement a Retrival Augmented Generation (RAG) for a Large Language Model (LLM). User prompts to write articles would under go a "research" process, where relevant information would be collected and compiled into a case study and formatted by Bard, which then would be authored as a final article. 
Information for the RAG process was collected in a vector database (PINECONE). Built in mind with scale, when not in use these vector embeddings (created with scentence transformers) they're are stored within a MySQL Database within a Location or LOC. 

## Accessing the Project
Much of this project was run through vectortest.py, with an interface to acsess each of the functions, although all of the actual functionality was created within the vector_classes.py. Additionally, much of the information used in retrival augmented generation is stored within the folders containing text files of articles taken from the internet. To acsess the project the user will have to utilize the vector_classes.py file to import the relevant classes and call the relevant methods and import the feild specific knowledge utilizing the tools provided.
Aleternatively, a sample article is provided on the "Lithium Markets as of December 2023". 
