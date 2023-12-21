# data_preprocessing.py
import pandas as pd
from functools import reduce

from xml_parser import extract_text


def preprocess_data(xmlfiles):
    # Check if xmlfiles is not empty
    if not xmlfiles:
        print("No XML files found.")
        return pd.DataFrame()

    parser_all = list(map(extract_text, xmlfiles))

    # Check if parser_all is not empty
    if not parser_all or all(not parser for parser in parser_all):
        print("No data extracted from XML files.")
        return pd.DataFrame()

    data = reduce(lambda x, y: x + y, parser_all)
    df = pd.DataFrame(data, columns=['filename', 'width', 'height', 'name', 'xmin', 'xmax', 'ymin', 'ymax'])

    return df