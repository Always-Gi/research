from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "hanggi-cho-cv.pdf"

INK = colors.HexColor("#1f2933")
MUTED = colors.HexColor("#5f6b76")
ACCENT = colors.HexColor("#315b7d")
RULE = colors.HexColor("#d8dde2")


def build_cv() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=21 * mm,
        rightMargin=21 * mm,
        topMargin=20 * mm,
        bottomMargin=18 * mm,
        title="Curriculum Vitae - Hanggi Cho",
        author="Hanggi Cho",
        subject="Academic curriculum vitae",
    )

    styles = getSampleStyleSheet()
    name = ParagraphStyle(
        "Name",
        parent=styles["Title"],
        fontName="Times-Bold",
        fontSize=26,
        leading=30,
        textColor=INK,
        alignment=TA_LEFT,
        spaceAfter=5,
    )
    role = ParagraphStyle(
        "Role",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=15,
        textColor=INK,
    )
    contact = ParagraphStyle(
        "Contact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=14,
        textColor=MUTED,
        spaceAfter=11,
    )
    section = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontName="Times-Bold",
        fontSize=14,
        leading=18,
        textColor=INK,
        spaceBefore=15,
        spaceAfter=7,
    )
    body = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=14.5,
        textColor=INK,
        spaceAfter=4,
    )
    story = [
        Paragraph("Hanggi Cho", name),
        Paragraph(
            "Undergraduate Student in Mathematics and Applied Statistics<br/>"
            "Yonsei University",
            role,
        ),
        Spacer(1, 4),
        Paragraph(
            '<link href="mailto:dabicho33@gmail.com" color="#315b7d">dabicho33@gmail.com</link>'
            ' &nbsp;&nbsp;|&nbsp;&nbsp; <link href="https://github.com/Always-Gi" color="#315b7d">GitHub</link>'
            ' &nbsp;&nbsp;|&nbsp;&nbsp; <link href="https://www.linkedin.com/in/hanggi-cho-268119409/" color="#315b7d">LinkedIn</link>',
            contact,
        ),
        HRFlowable(width="100%", thickness=0.7, color=RULE),
        Paragraph("Education", section),
        Paragraph("<b>Yonsei University</b>", body),
        Paragraph("Undergraduate study in Mathematics and Applied Statistics", body),
        Paragraph("Overall GPA: 4.17/4.30 &nbsp;&nbsp;|&nbsp;&nbsp; Major GPA: 4.10/4.30", body),
        Paragraph("Honors and Awards", section),
        Paragraph("Spring 2026 &mdash; Academic Excellence Award", body),
        Paragraph("Fall 2025 &mdash; Academic Excellence Award", body),
        Paragraph("Spring 2025 &mdash; Highest Academic Excellence Award", body),
        Paragraph("Research Interests", section),
        Table(
            [
                [Paragraph("&#8226;&nbsp; Operations Research", body), Paragraph("&#8226;&nbsp; Machine Learning", body)],
                [Paragraph("&#8226;&nbsp; Quantitative Finance", body), Paragraph("&#8226;&nbsp; Statistics", body)],
            ],
            colWidths=[78 * mm, 78 * mm],
            style=TableStyle(
                [
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5 * mm),
                    ("TOPPADDING", (0, 0), (-1, -1), 2),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ]
            ),
        ),
    ]

    doc.build(story)


if __name__ == "__main__":
    build_cv()
