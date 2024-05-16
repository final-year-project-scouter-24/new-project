# app.py
import io

from flask import Flask, render_template, request, make_response
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Get form data
    name = request.form['name']
    age = request.form['age']
    # Add more form fields as needed

    # Create PDF
    response = make_response()
    response.headers['Content-Disposition'] = 'attachment; filename=medical_report.pdf'
    buffer = response.stream
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    data = [['Name', name],
            ['Age', age]]
    # Add more rows as needed

    table = Table(data, colWidths=200, rowHeights=30)
    table.setStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    doc.build([table])

    return response

if __name__ == '__main__':
    app.run(debug=True)

