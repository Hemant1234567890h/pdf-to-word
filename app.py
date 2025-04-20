from flask import Flask, request, send_file
from pdf2docx import Converter
import os

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_word():
    file = request.files['pdf']
    input_path = 'input.pdf'
    output_path = 'output.docx'
    
    file.save(input_path)
    
    cv = Converter(input_path)
    cv.convert(output_path)
    cv.close()
    
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
