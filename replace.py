from docxtpl import DocxTemplate
import jinja2
import pandas as pd


def replace_text(context):
    doc = DocxTemplate('static/TENDER_DOCS/combined_file1.docx')
    doc.render(context)
    doc.save("static/TENDER_DOCS/final.docx")
