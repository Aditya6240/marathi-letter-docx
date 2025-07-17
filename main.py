from flask import Flask, request, send_file
from docx import Document
import tempfile

app = Flask(__name__)

@app.route('/')
def home():
    return 'Marathi Letter DOCX Generator Running ✅'

@app.route('/generate-docx', methods=['POST'])
def generate_docx():
    content = request.json.get('text', '')
    doc = Document()
    doc.add_paragraph(content)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    doc.save(temp_file.name)
    return send_file(temp_file.name, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
