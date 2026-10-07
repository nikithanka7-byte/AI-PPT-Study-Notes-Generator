import re
from collections import Counter

def clean_text(text):

    text = str(text)

    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    text = re.sub(
        r"\n+",
        "\n",
        text
    )

    return text.strip()

def remove_noise(text):

    lines = []

    for line in text.splitlines():

        line = line.strip()

        if not line:
            continue

        if len(line) <= 1:
            continue

        lines.append(
            line
        )

    return lines

def is_heading(line):

    line = line.strip()

    if not line:
        return False

    words = line.split()

    if len(words) <= 7:

        if not line.endswith(
            (".", ",", ";", ":")
        ):

            return True

    if line.isupper() and len(line) < 100:
        return True

    if re.match(
        r"^\d+[\.\)]\s+",
        line
    ):
        return True

    return False

def make_bullets(lines):

    bullets = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        line = re.sub(
            r"^[•●▪◦\-*]+\s*",
            "",
            line
        )

        line = re.sub(
            r"\s+",
            " ",
            line
        )

        if line:

            bullets.append(
                line
            )

    return bullets

def split_into_sections(lines):

    sections = []

    current_heading = "Main Topic"
    current_content = []

    for line in lines:

        if is_heading(line):

            if current_content:

                sections.append(
                    {
                        "heading": current_heading,
                        "content": make_bullets(
                            current_content
                        )
                    }
                )

            current_heading = line
            current_content = []

        else:

            current_content.append(
                line
            )

    if current_content:

        sections.append(
            {
                "heading": current_heading,
                "content": make_bullets(
                    current_content
                )
            }
        )

    return sections

def extract_definitions(lines):

    definitions = []

    for line in lines:

        match = re.match(
            r"^(.{2,40})\s*:\s*(.{5,})$",
            line
        )

        if match:

            term = match.group(
                1
            ).strip()

            meaning = match.group(
                2
            ).strip()

            if len(term.split()) <= 6:

                definitions.append(
                    {
                        "term": term,
                        "definition": meaning
                    }
                )

    return definitions[:15]

def extract_keywords(text):

    words = re.findall(
        r"\b[A-Za-z]{4,}\b",
        text.lower()
    )

    stop_words = {
        "this",
        "that",
        "these",
        "those",
        "with",
        "from",
        "have",
        "will",
        "which",
        "their",
        "there",
        "about",
        "using",
        "into",
        "also",
        "than",
        "then",
        "they",
        "them",
        "were",
        "been",
        "being",
        "such",
        "some",
        "more",
        "when",
        "where",
        "what",
        "your",
        "you",
        "for",
        "and",
        "the",
        "are",
        "was",
        "not",
        "can"
    }

    words = [
        word
        for word in words
        if word not in stop_words
    ]

    frequency = Counter(
        words
    )

    return [
        word
        for word, count
        in frequency.most_common(8)
    ]

def generate_notes(text):

    text = clean_text(
        text
    )

    lines = remove_noise(
        text
    )

    sections = split_into_sections(
        lines
    )

    definitions = extract_definitions(
        lines
    )

    keywords = extract_keywords(
        text
    )

    quick_revision = []

    for section in sections:

        for item in section.get(
            "content",
            []
        ):

            if len(
                quick_revision
            ) >= 8:

                break

            quick_revision.append(
                item
            )

    if sections:

        title = sections[0].get(
            "heading",
            "Study Notes"
        )

    else:

        title = "Study Notes"

    return {
        "title": title,
        "sections": sections,
        "definitions": definitions,
        "keywords": keywords,
        "quick_revision": quick_revision
    }