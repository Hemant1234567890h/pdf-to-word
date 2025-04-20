from flask import Flask, request, jsonify, send_file
import os
from werkzeug.utils import secure_filename
from pdf2docx import Converter

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ PDF to Word API is live on Render!"

@app.route('/convert', methods=['POST'])
def convert_pdf_to_word():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    file_path = os.path.join('/tmp', filename)
    file.save(file_path)

    output_path = file_path.replace('.pdf', '.docx')

    cv = Converter(file_path)
    cv.convert(output_path, start=0, end=None)
    cv.close()

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
