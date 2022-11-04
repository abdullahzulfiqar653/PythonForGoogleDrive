# Get Authentication for Google Service API through the attached PDF.
# Download client_secrets.json from Google API Console and OAuth2.0 is done in two lines.
# You can customize the behavior of OAuth2 in one settings file settings.yaml
# upload file to google drive and add the file in list you want to upload
def upload_files_to_gdrive(upload_file_list, drive, driveId):
    for upload_file in upload_file_list:
        # Note that we need to provide the id of the corresponding Google Drive folder.
        # In this example, the test folder's ID is 1pzschX3uMbxU0lB5WZ6IlEEeAUE8MZ-t.
        # You can get the Google Drive folder ID from the browser.
        # For example: when we open the test folder in my Google Drive, the browser shows the
        # address as https://drive.google.com/drive/folders/1MVjVp-O-vIth4dynbOiPZ0AOFRQNYq22.
        # Then the corresponding ID for the test folder is the part after the last \ symbol,
        # which is 1MVjVp-O-vIth4dynbOiPZ0AOFRQNYq22.
        gfile = drive.CreateFile(
            {'parents': [{'id': driveId}]})
        # Read file and set it as the content of this instance.
        gfile.SetContentFile(upload_file)
        gfile.Upload() # Upload the file.
