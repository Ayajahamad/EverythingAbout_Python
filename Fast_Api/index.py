from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import uuid
from typing import List

# Set the parent directory and upload folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct the PARENT_DIRECTORY by going to the Fast_Api folder
PARENT_DIRECTORY = os.path.join(BASE_DIR, "Fast_Api")

UPLOAD_DIRECTORY = os.path.join(PARENT_DIRECTORY, "uploads")

# Ensure that the upload directory exists
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = FastAPI()

# Get the absolute path to the 'static' folder relative to the script location
static_dir = os.path.join(PARENT_DIRECTORY, "static")
print(static_dir)

# Ensure that the static directory exists
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

# Serve static files from the correct location
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Serve the HTML form
@app.get("/", response_class=HTMLResponse)
async def serve_form():
    with open(os.path.join(static_dir, "index.html"), "r") as f:
        return HTMLResponse(content=f.read())

# File upload endpoint
@app.post("/upload_resumes/")
async def upload_resumes(resumes: List[UploadFile] = File(...)):
    uploaded_files = []
    
    for resume in resumes:
        print(resume.filename)
        
        # Generate a unique filename using uuid
        unique_filename = str(uuid.uuid4()) + "_" + resume.filename
        
        # Save the file in the 'uploads' directory
        file_location = os.path.join(UPLOAD_DIRECTORY, unique_filename)
        with open(file_location, "wb") as f:
            content = await resume.read()
            f.write(content)
        
        uploaded_files.append(unique_filename)
        
    return {"message": "Files uploaded successfully", "uploaded_files": uploaded_files}
