import os
import glob

# search all files inside a specific folder
# *.* means file name with any extension
dir_path = r'C:\ggb\GEORGI\DZI_22_23\projects\arichiver\*.txt'
res = glob.glob(dir_path, recursive=True)
print(res)
for path in res:
    print('*****'+path)



