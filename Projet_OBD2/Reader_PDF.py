# sudo apt-get install python3-pypdf2
from PyPDF2 import PdfFileReader


class Pdf_extractor:
    def __init__(self, file):
        with open(file, "rb") as file:
            pdf = PdfFileReader(file)
            text = pdf.getPage(32).extractText()
            index = text.find("P")
            text = text[index:]
            # print(text)
            self.extract_code(text, index)

    def extract_code(self, text, index):
        # for i in text:
        line_feed = text.find("\n")
        # print(line_feed)
        text = text[:line_feed]
        print(text)


if __name__ == "__main__":
    file_path = "/home/jordan/Téléchargements/OBD2_error_codes.pdf"
    Pdf_extractor(file_path)
