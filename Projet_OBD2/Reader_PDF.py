# sudo apt-get install python3-pypdf2
# Think to change file path in main
from PyPDF2 import PdfFileReader


class Pdf_extractor:
    def __init__(self, file):
        with open(file, "rb") as file:
            pdfReader = PdfFileReader(file)
            pages = pdfReader.numPages
            for i in range(pages):
                page = pdfReader.getPage(i)
                # print("Page number: ", i)
                text = page.extractText()
                for i in range(len(text)):
                    print(text[i])
                    # print(text[i], end="")
                # print()

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
