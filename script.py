import os
from os.path import splitext
from collections import Counter
import shutil
from tqdm import tqdm

if not os.path.exists('annotations'):
    os.makedirs('annotations')

def get_images_with_annotations(path):
    #List containing all file names + their extension in path directory
    myDir = os.listdir(path)
    #List containing all file names without their extension (see splitext doc)
    l = [splitext(filename)[0] for filename in myDir]
    #Count occurences
    a = dict(Counter(l))
    
    for k,v in tqdm(a.items()):
        if v > 1:
            shutil.move(k+".jpeg",os.path.join("annotations"))
            shutil.move(k+".txt",os.path.join("annotations"))


get_images_with_annotations(os.curdir)
