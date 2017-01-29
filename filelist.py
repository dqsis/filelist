# Purpose:
#     Print folder/subfolder tree structure into a text file
# -----------------------------------------------------------------------------

import sys
import os

of = open('filestructure.txt', "w")

root = r"C:\Users\DimitriosKiousis\filepath"
path = os.path.join(root, "filename")

for path, subdirs, files in os.walk(root):
    for name in files:
        print(os.path.join(path, name))
        of.write(os.path.join(path, name) + "\n")