from docxcompose.composer import Composer
from docx import Document as Document_compose
# filename_master is name of the file you want to merge the docx file into

#files_list = ["static/TENDER_DOCS/Cover_index_profile.docx",
#             "static/TENDER_DOCS/Business Licenses.docx", "static/TENDER_DOCS/references.docx"]
filename_master = 'static/TENDER_DOCS/BLANK.docx'


def combine_all_docx(filename_master, files_list):
    number_of_sections = len(files_list)
    master = Document_compose(filename_master)
    composer = Composer(master)
    for i in range(0, number_of_sections):
        doc_temp = Document_compose(files_list[i])
        composer.append(doc_temp)
    composer.save("static/TENDER_DOCS/combined_file1.docx")


#combine_all_docx(filename_master, files_list)

resume_master = "static/temp/last_doc.docx"
last = "static/TENDER_DOCS/thankyou_page.docx"


def combine_resumes_and_other_stuff(resume_list):
    number_of_sections = len(resume_list)
    master = Document_compose(filename_master)
    composer = Composer(master)
    for i in range(0, number_of_sections):
        doc_temp = Document_compose(resume_list[i])
        composer.append(doc_temp)
    composer.append(Document_compose(last))
    composer.save(resume_master)
