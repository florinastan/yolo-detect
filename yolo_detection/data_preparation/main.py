# main.py
from glob import glob
import warnings
from xml_parser import extract_text
from data_preprocessing import preprocess_data
from label_encoding import label_encoding
from save_data import save_data
import os
import pandas as pd

warnings.filterwarnings('ignore')

# step-1: get path of each xml file
xmlfiles = glob('./data_images/*.xml')

# replace \\ with /
replace_text = lambda x: x.replace('\\', '/')
xmlfiles = list(map(replace_text, xmlfiles))

# step-2: read xml files
df = preprocess_data(xmlfiles)

# type conversion
cols = ['width', 'height', 'xmin', 'xmax', 'ymin', 'ymax']
df[cols] = df[cols].astype(int)

# center x, center y
df['center_x'] = ((df['xmax'] + df['xmin']) / 2) / df['width']
df['center_y'] = ((df['ymax'] + df['ymin']) / 2) / df['height']

# w
df['w'] = (df['xmax'] - df['xmin']) / df['width']

# h
df['h'] = (df['ymax'] - df['ymin']) / df['height']

# split data into train and test
images = df['filename'].unique()

img_df = pd.DataFrame(images, columns=['filename'])
img_train = tuple(img_df.sample(frac=0.8)['filename'])  # shuffle and pick 80% of images
img_test = tuple(img_df.query(f'filename not in {img_train}')['filename'])  # take rest 20% images

train_df = df.query(f'filename in {img_train}')
test_df = df.query(f'filename in {img_test}')

# Assign id number to object names
train_df['id'] = train_df['name'].apply(label_encoding)
test_df['id'] = test_df['name'].apply(label_encoding)

# Save Image and Labels in text
train_folder = 'data_images/train'
test_folder = 'data_images/test'

os.mkdir(train_folder)
os.mkdir(test_folder)

cols = ['filename', 'id', 'center_x', 'center_y', 'w', 'h']
groupby_obj_train = train_df[cols].groupby('filename')
groupby_obj_test = test_df[cols].groupby('filename')

filename_series = pd.Series(groupby_obj_train.groups.keys())
filename_series.apply(save_data, args=(train_folder, groupby_obj_train))

filename_series_test = pd.Series(groupby_obj_test.groups.keys())
filename_series_test.apply(save_data, args=(test_folder, groupby_obj_test))
