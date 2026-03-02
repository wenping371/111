import fpdf

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.pdf = fpdf.FPDF()

    def add_page(self):
        self.pdf.add_page()

    def set_font(self, font='Arial', size=12):
        self.pdf.set_font(font, size=size)

    def add_text(self, text):
        self.pdf.multi_cell(0, 10, text)

    def save(self):
        self.pdf.output(self.filename)

# Example usage:
# pdf = PDFGenerator('example.pdf')
# pdf.add_page()
# pdf.set_font('Arial', 'B', 16)
# pdf.add_text('Hello, World!')
# pdf.save()