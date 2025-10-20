import os
import shutil # Used for file copy operations (copyfileobj)
from fastapi import UploadFile # File object submitted by the user in FastAPI
import tempfile

# Saving one or more files (PDF, txt, etc.) uploaded by the user to the server and returning the paths of the saved files.

UPLOAD_DIR="./uploaded_pdfs"

def save_uploaded_files(files:list[UploadFile]) -> list[str]:  # def save_uploaded_files(files):  we can write it like that too
    os.makedirs(UPLOAD_DIR,exist_ok=True)
    file_paths=[]
    for file in files:
        temp_path=os.path.join(UPLOAD_DIR,file.filename)
        with open(temp_path,"wb") as f:
            shutil.copyfileobj(file.file,f)
        file_paths.append(temp_path)
    return file_paths