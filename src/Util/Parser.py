from pypdf import PdfReader

class Parser:

    def __init__(self, file_location):
        self.file_location = file_location


    def parse(self):
        reader = PdfReader(self.file_location)
        text = ''
        for i in range(len(reader.pages)):
            text += reader.pages[i].extract_text()
        return text