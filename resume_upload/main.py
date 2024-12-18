from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import os
from typing import List

app = FastAPI()

PARENT_DIRECTORY = os.path.abspath("./resume_upload")
UPLOAD_DIRECTORY = os.path.join(PARENT_DIRECTORY, "uploads")

print(UPLOAD_DIRECTORY)

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <body>
            <h1>Resume Upload</h1>
            <form action="/upload_resumes/" method="post" enctype="multipart/form-data">
                <input type="file" name="resumes" multiple>
                <input type="submit">
            </form>
        </body>
    </html>
    """

@app.post("/upload_resumes/")
async def upload_resumes(resumes: List[UploadFile] = File(...)):
    uploaded_files = []
    
    for resume in resumes:
        print(resume.filename)
        
        file_location = os.path.join(UPLOAD_DIRECTORY, resume.filename)
        with open(file_location, "wb") as f:
            content = await resume.read()
            f.write(content)
        
        print(resume)
        uploaded_files.append(resume.filename)
        
    return {"message": "Files uploaded successfully", "uploaded_files": uploaded_files}

