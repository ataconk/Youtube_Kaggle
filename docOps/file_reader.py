import pandas as pd
import json
from pandas.io.json import json_normalize
import xml.etree.ElementTree as ET


class DocumentHandler:

    def __init__(self):
        pass

    def get_csv(self, path):
        reader = pd.read_csv(path)
        return reader

    def get_json(self, path):
        with open(path) as reader:
            file = json.load(reader)
            return file

    def get_tsv(self, path):
        reader = pd.read_csv(path, delimiter="\t")
        return reader

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
            for sub_elem in elem:
                print('\t', sub_elem.tag, ': ', sub_elem.text)

                for subsubelem in sub_elem:
                    print('\t\t', subsubelem.tag, ': ', subsubelem.text)

    def get_text(self, path):
        f = open(path)
        your_list = f.readlines()
        return your_list

    def read_doc(self, ek):

        if ek.split(".", 1)[1] == 'csv':
            return self.get_csv(ek)

        elif ek.split(".", 1)[1] == 'json':
            return self.get_json(ek)

        elif ek.split(".", 1)[1] == 'tsv':
            return self.get_tsv(ek)

        elif ek.split(".", 1)[1] == 'xml':
            return self.xml_reader(ek)
        else:
            return self.get_text(ek)

    def show(self, doc):
        print(doc)


# ax = dh.get_json('C:\\workspace\\notebook\\data\\DE_category_id.json')
# axx = dh.json_to_df('items', 'data\\DE_category_id.json')
# axxx = dh.xml_reader('C:\\workspace\\config.xml')

# axxx.show(limit=10)
