from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


g_login = GoogleAuth()
g_login.LocalWebserverAuth()
drive = GoogleDrive(g_login)

file_path = r"C:\Users\Owner\Desktop\Tutoring\skylight.jpg"
with open(file_path,"r") as file:
    file_drive = drive.CreateFile({'title': os.path.basename(file.name), 'mimeType': 'image/jpeg'})
    file_drive.SetContentFile(file_path)
    file_drive.Upload()
    print("Id:", file_drive.get('id'))

file_path = r"C:\Users\Owner\Desktop\Tutoring\skylight1.jpg"
with open(file_path,"r") as file:
    file_drive = drive.CreateFile({'title': os.path.basename(file.name), 'mimeType': 'image/jpeg'})
    file_drive.SetContentFile(file_path)
    file_drive.Upload()
    print("Id:", file_drive.get('id'))

