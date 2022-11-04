# Get Authentication for Google Service API through the attached PDF.

# Download client_secrets.json from Google API Console and OAuth2.0 is done in two lines.
# You can customize the behavior of OAuth2 in one settings file settings.yaml
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)

# upload file to google drive
# add the file in list you want to upload
upload_file_list = ['samplefile1.txt', 'samplefile2.txt']
for upload_file in upload_file_list:
    # Note that we need to provide the id of the corresponding Google Drive folder.
    # In this example, the test folder's ID is 1pzschX3uMbxU0lB5WZ6IlEEeAUE8MZ-t.
    # You can get the Google Drive folder ID from the browser.
    # For example: when we open the test folder in my Google Drive, the browser shows the
    # address as https://drive.google.com/drive/folders/1MVjVp-O-vIth4dynbOiPZ0AOFRQNYq22.
    # Then the corresponding ID for the test folder is the part after the last \ symbol,
    # which is 1MVjVp-O-vIth4dynbOiPZ0AOFRQNYq22.
	gfile = drive.CreateFile(
		{'parents': [{'id': '1MVjVp-O-vIth4dynbOiPZ0AOFRQNYq22'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.