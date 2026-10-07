import os
import streamlit as st

from ppt_processor import extract_text_from_ppt
from notes_generator import generate_notes
from pdf_generator import create_pdf

st.set_page_config(
    page_title="AI PPT Study Notes Generator",
    page_icon="📚",
    layout="wide"
)

st.title("AI PPT Study Notes Generator")
st.write(
    "Upload a PPTX file and generate organized study notes "
    "with OCR, mind map and quick revision."
)

uploaded_file = st.file_uploader(
    "Upload your PowerPoint file",
    type=["pptx"]
)

if uploaded_file is not None:

    os.makedirs("output", exist_ok=True)

    ppt_path = os.path.join(
        "output",
        uploaded_file.name
    )

    with open(ppt_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PPT uploaded successfully!")

    if st.button(
        "Generate Study Notes",
        type="primary"
    ):

        with st.spinner(
            "Processing PPT and generating notes..."
        ):

            try:

                extracted_text = extract_text_from_ppt(
                    ppt_path
                )

                if not extracted_text.strip():

                    st.error(
                        "No text could be extracted from the PPT."
                    )

                    st.stop()

                notes = generate_notes(
                    extracted_text
                )

                st.success(
                    "Study notes generated successfully!"
                )

                st.subheader("Notes Preview")

                for section in notes.get(
                    "sections",
                    []
                ):

                    st.markdown(
                        f"### {section.get('heading', 'Topic')}"
                    )

                    for item in section.get(
                        "content",
                        []
                    ):

                        st.write(
                            f"• {item}"
                        )

                definitions = notes.get(
                    "definitions",
                    []
                )

                if definitions:

                    st.subheader(
                        "Important Definitions"
                    )

                    for definition in definitions:

                        if isinstance(
                            definition,
                            dict
                        ):

                            term = definition.get(
                                "term",
                                ""
                            )

                            meaning = definition.get(
                                "definition",
                                ""
                            )

                            st.write(
                                f"**{term}:** {meaning}"
                            )

                        else:

                            st.write(
                                f"• {definition}"
                            )

                keywords = notes.get(
                    "keywords",
                    []
                )

                if keywords:

                    st.subheader(
                        "Important Keywords"
                    )

                    st.write(
                        ", ".join(
                            map(str, keywords)
                        )
                    )

                pdf_name = (
                    os.path.splitext(
                        uploaded_file.name
                    )[0]
                    + "_Study_Notes.pdf"
                )

                pdf_path = os.path.join(
                    "output",
                    pdf_name
                )

                create_pdf(
                    notes,
                    pdf_path
                )

                st.success(
                    "PDF created successfully!"
                )

                with open(
                    pdf_path,
                    "rb"
                ) as pdf_file:

                    st.download_button(
                        label="Download Study Notes PDF",
                        data=pdf_file,
                        file_name=pdf_name,
                        mime="application/pdf"
                    )

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )