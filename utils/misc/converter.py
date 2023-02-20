from pdf2docx import Converter



def convert_docx(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file)

    cv.close()
