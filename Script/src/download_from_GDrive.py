# method downloading files from Google Drive as follows.
# Note - after listing the files only we can download the file.

def download_files_from_gdrive(file_list_in_drive):
    length_of_files = len(file_list_in_drive)
    for i, file in enumerate(sorted(file_list_in_drive, key = lambda x: x['title']), start=1):
        print('Downloading {} file from GDrive ({}/{})'.format(file['title'], i, length_of_files))
        file.GetContentFile(file['title'])
    

