# label_encoding.py
def label_encoding(x):
    labels = {'person': 0, 'car': 1, 'chair': 2, 'bottle': 3, 'pottedplant': 4, 'bird': 5, 'dog': 6,
              'sofa': 7, 'bicycle': 8, 'horse': 9, 'boat': 10, 'motorbike': 11, 'cat': 12, 'tvmonitor': 13,
              'cow': 14, 'sheep': 15, 'aeroplane': 16, 'train': 17, 'diningtable': 18, 'bus': 19}
    return labels[x]
