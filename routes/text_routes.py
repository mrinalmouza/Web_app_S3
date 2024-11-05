from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from pathlib import Path
from ..services.text_processor import TextProcessor
from ..models.text_state import TextState

router = APIRouter()
text_state = TextState()
text_processor = TextProcessor()

@router.get("/", response_class=HTMLResponse)
async def get_index():
    html_file = Path("app/templates/index.html").read_text()
    return html_file

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(('.txt', '.rtf')):
        raise HTTPException(status_code=400, detail="Only .txt and .rtf files are supported")
    
    content = await file.read()
    file_extension = Path(file.filename).suffix
    text_state.current_text = text_processor.decode_content(content, file_extension)
    
    return {"message": "File uploaded successfully", "text": text_state.current_text}

@router.post("/preprocess")
async def preprocess():
    text_state.processed_text = text_processor.preprocess_text(text_state.current_text)
    return {"message": "Text preprocessed successfully", "text": text_state.processed_text}

@router.post("/transform")
async def transform():
    text_state.augmented_text = text_processor.transform_text(text_state.processed_text)
    return {"message": "Text transformed successfully", "text": text_state.augmented_text} 