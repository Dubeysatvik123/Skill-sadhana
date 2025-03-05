from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_certificate_pdf(certification):
    file_path = f"/tmp/{certification.student.username}_certificate.pdf"
    c = canvas.Canvas(file_path, pagesize=letter)
    c.drawImage("certificate_bg.jpg", 0, 0, width=600, height=800)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(200, 600, "Certificate of Completion")
    c.setFont("Helvetica", 18)
    c.drawString(100, 500, f"Presented to: {certification.student.username}")
    c.drawString(100, 450, f"For successfully completing: {certification.course.name}")
    c.drawString(100, 400, f"Instructor: {certification.instructor.username}")
    c.showPage()
    c.save()
    return file_path
