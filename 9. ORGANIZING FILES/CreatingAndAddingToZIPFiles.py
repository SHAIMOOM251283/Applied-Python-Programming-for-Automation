#import zipfile
#newZip = zipfile.ZipFile('new.zip', 'w')
#newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
#newZip.close()

import os
import zipfile

file_to_zip = 'spam.txt'
output_zip_file = 'new.zip'

# Check if the file exists
if os.path.exists(file_to_zip):
    with zipfile.ZipFile(output_zip_file, 'w') as newZip:
        # Write the file to the zip archive
        newZip.write(file_to_zip, compress_type=zipfile.ZIP_DEFLATED)
    print(f"File '{file_to_zip}' successfully added to '{output_zip_file}'.")
else:
    print(f"Error: File '{file_to_zip}' not found.")
