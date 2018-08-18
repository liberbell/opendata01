# Zipfile Module
import zipfile

# Open and List
zip = zipfile.ZipFile('archives.zip', 'r')
print(zip.namelist())

# Metadata in the zip folder
for meta in zip.infolist():
    print(meta)

# Access to files in zip folder

# Extracting files

# Closing the zip
