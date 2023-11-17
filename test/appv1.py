import gradio as gr
from gradio.themes.base import Base

class Seafoam(Base):
    pass

seafoam = Seafoam()

def calculate(num1,num2):
    return int(num1)+int(num2)

with gr.Blocks(theme=seafoam) as demo:
    in_textbox1 = gr.Textbox(label="Num1")
    in_textbox2 = gr.Textbox(label="Num2")

    with gr.Row():
        button = gr.Button("Submit", variant="primary")
        #clear = gr.Button("Clear")

    output = gr.Textbox(label="Output")

    button.click(calculate, [in_textbox1, in_textbox2], output)

demo.launch(auth=("admin", "pass1234"))

# gr.Interface(theme = "dark",
#              fn=calculate, 
#              inputs=["textbox","textbox"], 
#              outputs="textbox"
#              ).launch()