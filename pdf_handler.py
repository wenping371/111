import os
from fpdf import FPDF

class PDFHandler:
    def __init__(self, filename):
        self.filename = filename
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()

    def set_title(self, title):
        self.pdf.set_font('Arial', 'B', 16)
        self.pdf.cell(0, 10, title, ln=True, align='C')

    def add_paragraph(self, text):
        self.pdf.set_font('Arial', '', 12)
        self.pdf.multi_cell(0, 10, text)

    def save_pdf(self):
        self.pdf.output(self.filename)

    def delete_pdf(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
        else:
            print(f"{self.filename} not found.")

# Example usage:
# pdf_handler = PDFHandler('example.pdf')
# pdf_handler.set_title('My PDF Document')
# pdf_handler.add_paragraph('This is a sample paragraph in the PDF.')
# pdf_handler.save_pdf()
# pdf_handler.delete_pdf()