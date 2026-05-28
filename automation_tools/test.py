#autmation tool for auto file organiser
import os  #for device drives
import shutil #files input and output
#path to organise
path_to_organise = "/Users/jagritisrivastava/Desktop"
#define all filetypes
file_types = {
   "Images":[".jpg",".png",".jpeg",".gif",".bmp"],
   "Documents":[".pdf",".doc",".docx",".ppt",".pptx"],
   "Videos":[".mp4",".mov",".avi",".wmv"],
   "Archives":[".zip",".tar",".tar.gz",".tar.bz"],
   "Music":[".mp3",".m4a",".flac"]
}
#loop through my path where i need to organise and list them
for filename in os.listdir(path_to_organise):

   print(filename)
   file_path = os.path.join(path_to_organise, filename)
   print(file_path)
   #no need to use folders
   if os.path.isdir(file_path):
       continue


   #check for each file extension and then move to respective created folders
   moved = False
   for folder, extensions in file_types.items():
       if filename.lower().endswith(tuple(extensions)):
           folder_path = os.path.join(path_to_organise, folder)
           #if there is no folder then create
           if not os.path.exists(folder_path):
               os.makedirs(folder_path)


           #move the files to folder
           shutil.move(file_path,folder_path)
           moved = True
           break
       if not moved:
           others_path = os.path.join(path_to_organise, "others_files")
           if not os.path.exists(others_path):
               os.makedirs(others_path)
           shutil.move(file_path,others_path)
   print("files moved successfully")