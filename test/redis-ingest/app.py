import os
import datetime
import gradio as gr
from gradio.themes.base import Base
import requests
from bs4 import BeautifulSoup
#from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.document_loaders import PyPDFium2Loader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores.redis import Redis

class Seafoam(Base):
    pass

seafoam = Seafoam()

def listFD(url, ext=''):
    page = requests.get(url).text
    #print(page)
    soup = BeautifulSoup(page, 'html.parser')
    return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

def getFileName():
    current_date_and_time = datetime.datetime.now()
    current_date_and_time_string = str(current_date_and_time)
    extension = ".yaml"
    file_name =  'redisSchema' + current_date_and_time_string + extension
    return file_name

#redis_url = "redis://default:mydocpass@my-doc-headless.redisdb.svc.cluster.local:17073"
#index_name = "pdfdemodocs"
#url = 'http://xxx.xxx.xxx.xxx/pdf/demo'
#ext = 'pdf'

def redisIngest(redis_url,index_name, docsUrl):
    shema_name = getFileName()
    for file in listFD(docsUrl, 'pdf'):
        loader = PyPDFium2Loader(file)
        data = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=40)
        all_splits = text_splitter.split_documents(data)
        embeddings = HuggingFaceEmbeddings()
        rds = Redis.from_documents(all_splits,
                                embeddings,
                                redis_url=redis_url,
                                index_name=index_name)
    rds.write_schema(shema_name)
    with open(shema_name, "r") as f_in:
        data = f_in.read()
    #print(data)
    return data

with gr.Blocks(theme=seafoam) as demo:
    in_textbox1 = gr.Textbox(label="Redis URL")
    in_textbox2 = gr.Textbox(label="Redis Index Name")
    in_textbox3 = gr.Textbox(label="PDF Web URL")

    with gr.Row():
        button = gr.Button("Submit", variant="primary")

    output = gr.Textbox(label="Output")

    button.click(redisIngest, [in_textbox1, in_textbox2, in_textbox3], output)

if __name__ == "__main__":
    demo.launch(debug = True)