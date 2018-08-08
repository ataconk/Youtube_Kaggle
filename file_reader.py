import pandas as pd
import json

class CSVread(object):


    def __init__(self, file):
        # self.file = file


    def get_file(self):

        self.reader = pd.read_csv(self.file)
        return self.reader


    def printdata(self):
        print(self.reader)



class JsonRead(object):
    def __init__(self, file):
        self.file = file

    def get_file(self):
        with open(self.file) as self.reader:
            self.file = json.load(self.reader)
            return self.reader

    def printJson(self):
        print(self.reader)


#
# import nltk
#
# nltk.data.


#
denek = CSVread('bakalim.csv')
denek.get_file()
# print(denek)

# json_deneme = JsonRead('DE_category_id.json')
# json_deneme = json_deneme.get_file()
# json_deneme.printdata()
# for x in range(45):
#     for item in json_deneme['items'][x]['id'].splitlines():
#             print('ID:' + item)