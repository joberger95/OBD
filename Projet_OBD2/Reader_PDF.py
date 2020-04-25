# sudo apt-get install python3-pypdf2
from PyPDF2 import PdfFileReader


class Pdf_extractor:
    def __init__(self, file):
        with open(file, "rb") as file:
            pdf = PdfFileReader(file)
            text = pdf.getPage(32).extractText()
            index = text.find("P0001")
            text = text[index:]
            # print(text)
            # print("Index de la lettre P:", index)
            carac = ("P", "-")

            self.extract_line(text)

    def extract_line(self, text):
        while self.text:
            line_feed = text.find("\n")
            # print(line_feed)
            line = text[:line_feed]
            # print(line)
            self.extract_code(line, ("P", "-"))
            self.text = text[line_feed:]
            # print("Le texte est:\n", text)
            return self.text

    def extract_code(self, line, carac):
        index = 0
        while index < len(line):
            if line[index] == carac[0] or carac[1]:

                space_separator = line.find(" ")
                code_number = line[:space_separator]
                print("Le numero de code est:\n", code_number)

                line = line[space_separator:]
                # print("Sans le code erreur: \n", line)

                while index < len(line):
                    if line[index] == carac[1]:
                        error_message = line[:index]
                        print("Le message d'erreur est:\n", error_message)

                        describe_message = line[index + 2 :]
                        print("Description de l'erreur:\n", describe_message)

                    index += 1
                return -1

            index += 1
        return -1


if __name__ == "__main__":
    file_path = "/home/jordan/Téléchargements/OBD2_error_codes.pdf"
    Pdf_extractor(file_path)
