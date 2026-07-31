from reportlab.pdfgen import canvas

def create_hello_world_pdf():
    c = canvas.Canvas('hello.pdf')
    c.drawString(100, 700, 'Hello World')
    c.save()