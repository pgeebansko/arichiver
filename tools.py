import os
import glob

# get all files inside a specific folder
dir_path = r'C:\ggb\GEORGI\DZI_22_23'
for path in os.scandir(dir_path):
    if path.is_file():
        print(path.name)


# search all files inside a specific folder
# *.* means file name with any extension
dir_path = r'C:\ggb\GEORGI\DZI_22_23\*.*'
res = glob.glob(dir_path, recursive=True)
print(res)
for path in res:
    print(path)
