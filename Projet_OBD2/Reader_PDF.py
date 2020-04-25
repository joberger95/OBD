# sudo apt-get install python3-pypdf2
from PyPDF2 import PdfFileReader


# def pdf_text_extractor(path):
#     with open(path, "rb") as f:
#         pdf = PdfFileReader(f)
#         # get the first page
#         page = pdf.getPage(32)
#         # print(page)
#         # print("Page type: {}".format(str(type(page))))
#         text = page.extractText()
#         index = text.find("P")
#         text = text[index:]
#         print("Indice de la lettre 'P' = ", index)
#         print("Texte =\n", text)


class Pdf_extractor:
    def __init__(self, file):
        with open(file, "rb") as file:
            pdf = PdfFileReader(file)
            text = pdf.getPage(32).extractText()
            index = text.find("P")
            text = text[index:]
            print(text)


if __name__ == "__main__":
    file_path = "/home/jordan/Téléchargements/OBD2_error_codes.pdf"
    Pdf_extractor(file_path)
