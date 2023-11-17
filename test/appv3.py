import os
import gradio as gr
from gradio.themes.base import Base
from zipfile import ZipFile


url = 'http://xxx.xxx.xxx.xxx/pdf/demo'
ext = 'pdf'

import requests
from bs4 import BeautifulSoup

def get_url_paths(url, ext='', params={}):
    response = requests.get(url, params=params)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    return parent

def showFiles (url):
    result = get_url_paths(url, 'pdf')
    return(result)

def showLocalFiles(files):
    #newList = ""
    for idx, file in enumerate(files):
        newList += file.name.split("/")[-1]
    return newList

demo = gr.Interface(
    #gr.themes.colors.green,
    showLocalFiles,
    gr.File(file_count="multiple"),# file_types=["text", ".json", ".csv"]),
    "text",

)

if __name__ == "__main__":
    demo.launch()
    #demo.launch(auth=("*******", "**********"))