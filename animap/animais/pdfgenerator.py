from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas 
from .models import Animal
import io

def gerarPDF(entry_id): 
    entry = Animal.objects.get(id=entry_id)


    pdf_file = io.BytesIO()
    canvas = Canvas(pdf_file, pagesize=letter)
    canvas.setFont('Helvetica', 12)


    canvas.drawString(1 * inch, 10 * inch, "Relatório:")
    canvas.drawString(1 * inch, 9.5 * inch, f"ID: {entry.id}")
    canvas.drawString(1 * inch, 9 * inch, f"Username: {entry.username}")
    canvas.drawString(1 * inch, 8.5 * inch, f"Endereço: {entry.endereço}")
    canvas.drawString(1 * inch, 8 * inch, f"Descrição: {entry.descriçao}")
    canvas.drawString(1 * inch, 7.5 * inch, f"Ponto de referência: {entry.ponto_ref}")
    canvas.drawString(1 * inch, 7 * inch, f"Coordenadas: ({entry.coordX}, {entry.coordY})")
    canvas.drawString(1 * inch, 6.5 * inch, f"Estado: {entry.estado}")


    canvas.save()
    pdf_data = pdf_file.getvalue()
    return pdf_data