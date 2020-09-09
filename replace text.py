from docxtpl import DocxTemplate
import jinja2
import pandas as pd


doc = DocxTemplate('combined_file1.docx')
doc.render(context)
doc.save("static/TENDER_DOCS/final.docx")
