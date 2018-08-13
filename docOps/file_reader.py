import pandas as pd
import json
from pandas.io.json import json_normalize
import xml.etree.ElementTree as ET


class documentHandler:

    def __init__(self):
        pass

    def get_csv(self, path):
        self.reader = pd.read_csv(path)
        return self.reader

    def get_json(self, path):
        with open(path) as self.reader:
            file = json.load(self.reader)
            return file

    def get_tsv(self, path):
        self.reader = pd.read_csv(path, delimiter="\t")
        return self.reader

    def json_to_df(self, normalizer, path):

        # with open(path) as self.reader:
        #     file = json.load(self.reader)
        # self.get_json(path)

        data_frame = json_normalize(self.get_json(path)[normalizer])
        return data_frame

    def xml_reader(self, path):
        tree = ET.parse(path)
        root = tree.getroot()
        for elem in root:

            print(elem.tag, ': ', elem.text)
            for subelem in elem:
                print('    ', subelem.tag, ': ', subelem.text)

                for subsubelem in subelem:
                    print('         ', subsubelem.tag, ': ', subsubelem.text)

    def get_text(self, path):
        f = open(path)
        yourList = f.readlines()
        return yourList

    def read_doc(self, ek):

        if ek.split(".",1)[1] == 'csv':
            return self.get_csv(ek)

        elif ek.split(".",1)[1] == 'json':
            return self.get_json(ek)

        elif ek.split(".",1)[1] == 'tsv':
            return self.get_tsv(ek)

        elif ek.split(".",1)[1] == 'xml':
            return self.xml_reader(ek)
        else:
            return self.get_text(ek)


    def show(self, doc):
        print(doc)








dh = documentHandler()
ax = dh.read_doc('C:\\workspace\\notebook\\data\\oldu.csv')
dh.show(ax)
# ax = dh.get_json('C:\\workspace\\notebook\\data\\DE_category_id.json')
# axx = dh.json_to_df('items', 'data\\DE_category_id.json')
# axxx = dh.xml_reader('C:\\workspace\\config.xml')

# axxx.show(limit=10)
