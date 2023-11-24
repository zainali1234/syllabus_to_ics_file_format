from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from gpt import response
from icsconverter import ics_converter
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        file = request.files['file']
        file_name = file.filename
        print('Received file:', file_name)

        reader = PdfReader(file)
        
        text = ""
        for page in reader.pages:
            text += page.extract_text() + " "
        
        # print(text)
        gpt_response = response(text)
        result = ics_converter(gpt_response)

        return result
    return 'No file received.'

if __name__ == '__main__':
    app.run(debug=True)