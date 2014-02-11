# Purpose:
#     Print folder/subfolder tree structure into a text file
# -----------------------------------------------------------------------------

import sys
import os

of = open('filestructure.txt', "w")

root = r"C:\Users\DimitriosKiousis\000-assignments\004-rosemount\PO-527-166571"
path = os.path.join(root, "PO-527-166571")

for path, subdirs, files in os.walk(root):
    for name in files:
        print(os.path.join(path, name))
        of.write(os.path.join(path, name) + "\n")