import os
import glob
import settings

# get all files inside a specific folder
dir_path = settings.FTPClientSettings.get_dir()
for path in os.scandir(dir_path):
    if path.is_file():
        print(path.name)


# search all files inside a specific folder
# *.* means file name with any extension
dir_path = settings.FTPClientSettings.get_files()
res = glob.glob(dir_path, recursive=True)
print(res)
for path in res:
    print(path)
