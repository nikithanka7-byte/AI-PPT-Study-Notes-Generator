from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def draw_rounded_box(
    c,
    x,
    y,
    width,
    height,
    text,
    font_size=10
):

    c.roundRect(
        x,
        y,
        width,
        height,
        8,
        stroke=1,
        fill=0
    )

    c.setFont(
        "Helvetica-Bold",
        font_size
    )

    text_width = c.stringWidth(
        text,
        "Helvetica-Bold",
        font_size
    )

    c.drawString(
        x + (width - text_width) / 2,
        y + height / 2 - 4,
        text[:30]
    )

def draw_mind_map(
    c,
    keywords,
    title="MAIN CONCEPT"
):

    page_width, page_height = A4

    center_x = page_width / 2
    center_y = page_height / 2

    center_width = 55 * mm
    center_height = 18 * mm

    draw_rounded_box(
        c,
        center_x - center_width / 2,
        center_y - center_height / 2,
        center_width,
        center_height,
        title
    )

    if not keywords:
        return

    positions = [
        (center_x - 75 * mm, center_y + 60 * mm),
        (center_x + 25 * mm, center_y + 60 * mm),
        (center_x - 95 * mm, center_y),
        (center_x + 40 * mm, center_y),
        (center_x - 75 * mm, center_y - 60 * mm),
        (center_x + 25 * mm, center_y - 60 * mm),
        (center_x - 120 * mm, center_y + 30 * mm),
        (center_x + 65 * mm, center_y - 30 * mm)
    ]

    box_width = 48 * mm
    box_height = 14 * mm

    for i, keyword in enumerate(
        keywords[:8]
    ):

        x, y = positions[i]

        c.line(
            center_x,
            center_y,
            x + box_width / 2,
            y + box_height / 2
        )

        draw_rounded_box(
            c,
            x,
            y,
            box_width,
            box_height,
            keyword.title(),
            9
        )