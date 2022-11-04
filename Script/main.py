from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from src import (
    upload_files_to_gdrive,
    list_out_file_from_gdrive,
    download_files_from_gdrive,
    create_file_and_write_text_init,
    )


gauth = GoogleAuth()           
drive = GoogleDrive(gauth)
driveId = '1MVjVp-O-vIth4dynbOiPZ0AOFRQNYq22' #folderId og Google Drive you are working with
upload_file_list = ['samplefile1.txt', 'samplefile2.txt'] #List of file to be uploaded.


upload_files_to_gdrive(upload_file_list, drive, driveId)
file_list_in_drive = list_out_file_from_gdrive(drive, driveId) #List of files to List from gdrive
download_files_from_gdrive(file_list_in_drive)
create_file_and_write_text_init(drive, driveId)