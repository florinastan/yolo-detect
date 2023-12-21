# save_data.py
import os
from shutil import move

def save_data(filename, folder_path, group_obj):
    # move image
    src = os.path.join('data_images', filename)
    dst = os.path.join(folder_path, filename)
    move(src, dst)  # move image to the destination folder

    # save the labels
    text_filename = os.path.join(folder_path, os.path.splitext(filename)[0] + '.txt')
    group_obj.get_group(filename).set_index('filename').to_csv(text_filename, sep=' ', index=False, header=False)
