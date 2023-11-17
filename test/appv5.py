import gradio as gr
from gradio.themes.base import Base

class Seafoam(Base):
    pass

seafoam = Seafoam()

def calculate(num1,num2):
    return int(num1)+int(num2)
def multiply(num1,num2):
    return int(num1)*int(num2)

with gr.Blocks(theme=seafoam) as demo:
    gr.Markdown("Calculater Demo")
    with gr.Tab("Add"):
        add_textbox1 = gr.Textbox(label="Num1")
        add_textbox2 = gr.Textbox(label="Num2")
        add_output = gr.Textbox(label="Addition")
        addbutton = gr.Button("Submit", variant="primary")
    with gr.Tab("Mul"):
        mul_textbox1 = gr.Textbox(label="Num1")
        mul_textbox2 = gr.Textbox(label="Num2")
        mul_submit = gr.Textbox(label="Addition")
        mulbutton = gr.Button("Submit", variant="primary")
    
    addbutton.click(calculate, [add_textbox1, add_textbox2], add_output)
    mulbutton.click(multiply, [mul_textbox1, mul_textbox2], mul_submit)

if __name__ == "__main__":
    demo.launch()