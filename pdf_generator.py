from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle
)
from reportlab.pdfgen import canvas
import math

def draw_mind_map(c, keywords, title):

    width, height = A4

    c.setFont(
        "Helvetica-Bold",
        22
    )

    c.drawCentredString(
        width / 2,
        height - 50,
        "MIND MAP"
    )

    center_x = width / 2
    center_y = height / 2

    main_width = 190
    main_height = 65

    c.setFillColor(
        colors.lightgrey
    )

    c.setStrokeColor(
        colors.black
    )

    c.setLineWidth(1.5)

    c.roundRect(
        center_x - main_width / 2,
        center_y - main_height / 2,
        main_width,
        main_height,
        12,
        fill=1,
        stroke=1
    )

    c.setFillColor(
        colors.black
    )

    c.setFont(
        "Helvetica-Bold",
        12
    )

    main_title = str(title)[:28]

    c.drawCentredString(
        center_x,
        center_y - 4,
        main_title
    )

    keywords = [
        str(k).strip()
        for k in keywords
        if str(k).strip()
    ]

    keywords = keywords[:8]

    if not keywords:

        c.setFont(
            "Helvetica",
            11
        )

        c.drawCentredString(
            center_x,
            center_y - 100,
            "No keywords available"
        )

        return

    radius_x = 220
    radius_y = 245

    for i, keyword in enumerate(keywords):

        angle = (
            2 * math.pi * i / len(keywords)
        ) - (math.pi / 2)

        x = (
            center_x
            + radius_x * math.cos(angle)
        )

        y = (
            center_y
            + radius_y * math.sin(angle)
        )

        box_width = 125
        box_height = 45

        c.setStrokeColor(
            colors.grey
        )

        c.setLineWidth(1.2)

        c.line(
            center_x,
            center_y,
            x,
            y
        )

        # Keyword box
        c.setFillColor(
            colors.whitesmoke
        )

        c.setStrokeColor(
            colors.black
        )

        c.roundRect(
            x - box_width / 2,
            y - box_height / 2,
            box_width,
            box_height,
            10,
            fill=1,
            stroke=1
        )

        # Keyword
        c.setFillColor(
            colors.black
        )

        c.setFont(
            "Helvetica-Bold",
            9
        )

        keyword = keyword[:20]

        c.drawCentredString(
            x,
            y - 3,
            keyword
        )

def add_page_number(canvas_obj, doc):

    canvas_obj.saveState()

    canvas_obj.setFont(
        "Helvetica",
        8
    )

    canvas_obj.drawCentredString(
        A4[0] / 2,
        20,
        f"Page {doc.page}"
    )

    canvas_obj.restoreState()

class MindMapCanvas(canvas.Canvas):

    def __init__(
        self,
        filename,
        pagesize=A4,
        **kwargs
    ):
        """
        **kwargs is important.
        ReportLab may pass arguments such as
        invariant, pageCompression, etc.
        """

        super().__init__(
            filename,
            pagesize=pagesize,
            **kwargs
        )

        self.page_number = 0
        self.mindmap_page = None
        self.keywords = []
        self.title = "Study Notes"

    def showPage(self):

        self.page_number += 1

        if (
            self.mindmap_page is not None
            and self.page_number == self.mindmap_page
        ):

            draw_mind_map(
                self,
                self.keywords,
                self.title
            )

        super().showPage()

    def save(self):

        # Handle last page
        if (
            self.mindmap_page is not None
            and self.page_number + 1 == self.mindmap_page
        ):

            self.page_number += 1

            draw_mind_map(
                self,
                self.keywords,
                self.title
            )

        super().save()

def create_pdf(
    notes,
    output_path
):

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=45,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=30,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    subtitle_style = ParagraphStyle(
        "SubtitleStyle",
        parent=styles["BodyText"],
        fontName="Helvetica-Oblique",
        fontSize=12,
        leading=18,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=17,
        leading=22,
        spaceBefore=10,
        spaceAfter=12
    )

    bullet_style = ParagraphStyle(
        "BulletStyle",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=11,
        leading=17,
        leftIndent=18,
        firstLineIndent=-10,
        spaceAfter=7
    )

    title = notes.get(
        "title",
        "Study Notes"
    )

    sections = notes.get(
        "sections",
        []
    )

    definitions = notes.get(
        "definitions",
        []
    )

    keywords = notes.get(
        "keywords",
        []
    )

    quick_revision = notes.get(
        "quick_revision",
        []
    )

    story = []

    story.append(
        Spacer(1, 180)
    )

    story.append(
        Paragraph(
            "AI-Powered Study Notes",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Generated from PPT using OCR",
            subtitle_style
        )
    )

    story.append(
        Spacer(1, 30)
    )

    story.append(
        Paragraph(
            str(title),
            heading_style
        )
    )

    story.append(
        Spacer(1, 100)
    )

    story.append(
        Paragraph(
            "Study • Understand • Revise",
            subtitle_style
        )
    )

    story.append(
        PageBreak()
    )

    for section in sections:

        heading = section.get(
            "heading",
            "Topic"
        )

        content = section.get(
            "content",
            []
        )

        story.append(
            Paragraph(
                str(heading),
                heading_style
            )
        )

        for item in content:

            item = str(
                item
            ).strip()

            if item:

                story.append(
                    Paragraph(
                        "• " + item,
                        bullet_style
                    )
                )

        story.append(
            Spacer(1, 10)
        )

    if definitions:

        story.append(
            PageBreak()
        )

        story.append(
            Paragraph(
                "Important Definitions",
                heading_style
            )
        )

        table_data = [
            [
                "Term",
                "Definition"
            ]
        ]

        for definition in definitions:

            if isinstance(
                definition,
                dict
            ):

                term = str(
                    definition.get(
                        "term",
                        ""
                    )
                )

                meaning = str(
                    definition.get(
                        "definition",
                        ""
                    )
                )

            else:

                term = ""

                meaning = str(
                    definition
                )

            table_data.append(
                [
                    term,
                    meaning
                ]
            )

        table = Table(
            table_data,
            colWidths=[
                130,
                340
            ],
            repeatRows=1
        )

        table.setStyle(
            TableStyle([
                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightgrey
                ),
                (
                    "FONTNAME",
                    (0, 0),
                    (-1, 0),
                    "Helvetica-Bold"
                ),
                (
                    "FONTNAME",
                    (0, 1),
                    (-1, -1),
                    "Helvetica"
                ),
                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    9
                ),
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.grey
                ),
                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP"
                ),
                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    7
                ),
                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    7
                ),
                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    7
                ),
                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    7
                )
            ])
        )

        story.append(
            table
        )

    story.append(
        PageBreak()
    )

    story.append(
        Spacer(1, 400)
    )

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "Quick Revision",
            heading_style
        )
    )

    for item in quick_revision:

        item = str(
            item
        ).strip()

        if item:

            story.append(
                Paragraph(
                    "• " + item,
                    bullet_style
                )
            )

    content_count = 0

    for section in sections:

        content_count += len(
            section.get(
                "content",
                []
            )
        )

    notes_pages = max(
        1,
        math.ceil(
            content_count / 14
        )
    )

    mindmap_page = (
        1
        + notes_pages
        + (1 if definitions else 0)
        + 1
    )

    def canvas_maker(
        filename,
        pagesize=A4,
        **kwargs
    ):
        """
        **kwargs fixes the ReportLab
        'unexpected keyword argument invariant'
        error.
        """

        c = MindMapCanvas(
            filename,
            pagesize=pagesize,
            **kwargs
        )

        c.mindmap_page = mindmap_page
        c.keywords = keywords
        c.title = title

        return c

    doc.build(
        story,
        onFirstPage=add_page_number,
        onLaterPages=add_page_number,
        canvasmaker=canvas_maker
    )