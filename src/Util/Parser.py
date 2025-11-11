import pymupdf
from datetime import datetime
class Parser:

    def __init__(self, file_location):
        self.file_location = file_location


    def parse(self):
        reader = pymupdf.open(self.file_location)
        text_lines = []
        for page in reader: 
            text_lines.extend(page.get_text().splitlines())

        for i in range(len(text_lines)):
            if "Page 1" in text_lines[i]:
                date = self.get_date(text_lines[i+1])

    def get_date(self, text):
        months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
        }
        date = text.split(" ")
        if date[1] in months:
            date_string = f'{date[2]}-{months[date[1]]}-{date[0]}'
            datetime_object = datetime.strptime(date_string, "%Y-%m-%d")
            return datetime_object