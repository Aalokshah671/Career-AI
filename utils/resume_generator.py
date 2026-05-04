from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_resume(data, filename="resume.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    content = []

    # Name
    content.append(Paragraph(f"<b>{data['name']}</b>", styles['Title']))
    content.append(Spacer(1, 10))

    # Contact
    content.append(Paragraph(f"Email: {data['email']}", styles['Normal']))
    content.append(Paragraph(f"Phone: {data['phone']}", styles['Normal']))
    content.append(Paragraph(f"LinkedIn: {data['linkedin']}", styles['Normal']))
    content.append(Spacer(1, 10))

    # Summary
    content.append(Paragraph("<b>Summary</b>", styles['Heading2']))
    content.append(Paragraph(data['summary'], styles['Normal']))
    content.append(Spacer(1, 10))

    # Skills
    content.append(Paragraph("<b>Skills</b>", styles['Heading2']))
    content.append(Paragraph(data['skills'], styles['Normal']))
    content.append(Spacer(1, 10))

    # Education
    content.append(Paragraph("<b>Education</b>", styles['Heading2']))
    content.append(Paragraph(data['education'], styles['Normal']))
    content.append(Spacer(1, 10))

    # Experience
    content.append(Paragraph("<b>Experience</b>", styles['Heading2']))
    content.append(Paragraph(data['experience'], styles['Normal']))
    content.append(Spacer(1, 10))

    # Projects
    content.append(Paragraph("<b>Projects</b>", styles['Heading2']))
    content.append(Paragraph(data['projects'], styles['Normal']))
    content.append(Spacer(1, 10))

    # Certifications
    content.append(Paragraph("<b>Certifications</b>", styles['Heading2']))
    content.append(Paragraph(data['certifications'], styles['Normal']))
    content.append(Spacer(1, 10))

    # Achievements
    content.append(Paragraph("<b>Achievements</b>", styles['Heading2']))
    content.append(Paragraph(data['achievements'], styles['Normal']))
    content.append(Spacer(1, 10))

    # Languages
    content.append(Paragraph("<b>Languages</b>", styles['Heading2']))
    content.append(Paragraph(data['languages'], styles['Normal']))
    content.append(Spacer(1, 10))

    # Hobbies
    content.append(Paragraph("<b>Hobbies</b>", styles['Heading2']))
    content.append(Paragraph(data['hobbies'], styles['Normal']))
    content.append(Spacer(1, 10))

    doc.build(content)

    return filename