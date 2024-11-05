import re
from fastapi import HTTPException

class TextProcessor:
    @staticmethod
    def decode_content(content, file_extension):
        try:
            text = content.decode('utf-8')
        except UnicodeDecodeError:
            text = content.decode('latin-1')

        if file_extension == '.rtf':
            # Basic RTF cleaning
            text = re.sub(r'[\\\{\}].*?[\\\{\}]', '', text)
        
        return text

    @staticmethod
    def preprocess_text(text):
        if not text:
            raise HTTPException(status_code=400, detail="No text loaded")
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)

    @staticmethod
    def transform_text(text):
        if not text:
            raise HTTPException(status_code=400, detail="No text to transform")
        return text[::-1] 