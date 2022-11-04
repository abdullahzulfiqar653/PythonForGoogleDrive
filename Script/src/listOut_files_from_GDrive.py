# *** List out files from Google Drive ***

def list_out_file_from_gdrive(drive, driveId):
    file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(
        driveId)}).GetList()
    for file in file_list:
        print('title: %s, id: %s' % (file['title'], file['id']))

    return file_list