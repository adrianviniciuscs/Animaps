from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas 
from .models import Animal
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO


def gerarPDF(entry_id):
    entry = Animal.objects.get(id=entry_id)

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    story = []

    # Add a title
    title = Paragraph("<u><b>Relatório - Animaps</b></u>", styles['Title'])
    story.append(title)

    img_path = entry.foto  # Replace with the actual path to your image
    logo = Image(img_path, width=4*inch, height=4*inch)
    story.append(logo)
    # Add details
    details = [
        f"<b>ID:</b> {entry.id}",
        f"<b>Username:</b> {entry.username}",
        f"<b>Endereço:</b> {entry.endereço}",
        f"<b>Descrição:</b> {entry.descriçao}",
        f"<b>Ponto de referência:</b> {entry.ponto_ref}",
        f"<b>Coordenadas:</b> ({entry.coordX}, {entry.coordY})",
        f"<b>Estado:</b> {entry.state}"
    ]

    for detail in details:
        p = Paragraph(detail, styles['BodyText'])
        story.append(p)
        story.append(Spacer(1, 12))  # Add some space between details

    doc.build(story)

    pdf_data = buffer.getvalue()
    buffer.close()

    return pdf_data

