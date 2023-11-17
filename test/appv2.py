import os
import gradio as gr
from gradio.themes.base import Base
from zipfile import ZipFile

class Seafoam(Base):
    pass

seafoam = Seafoam()

def zip_files(files):
    with ZipFile("tmp.zip", "w") as zipObj:
        for idx, file in enumerate(files):
            zipObj.write(file.name, file.name.split("/")[-1])
    return "tmp.zip"

demo = gr.Interface(
    zip_files,
    gr.File(file_count="multiple", file_types=["text", ".json", ".csv"]),
    "file"
    #examples=[[[os.path.join(os.path.dirname(__file__),"files/titanic.csv"), 
    #os.path.join(os.path.dirname(__file__),"files/titanic.csv"), 
    #os.path.join(os.path.dirname(__file__),"files/titanic.csv")]]], 
    #cache_examples=True
)

if __name__ == "__main__":
    demo.launch()
    #demo.launch(auth=("xxxxxx", "xxxxxxxx"))