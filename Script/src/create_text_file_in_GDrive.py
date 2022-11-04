# We can also write files directly to Google Drive using the following code:
# Create a GoogleDriveFile instance with title 'test.txt'.

def create_file_and_write_text_init(drive, driveId):
    file = drive.CreateFile({'parents': [{'id': driveId}],'title': 'test.txt'})  
    # Set content of the file from the given string.
    file.SetContentString('Hello World!') 
    file.Upload()