from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import text_routes

app = FastAPI(title="Text Processing API")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routes
app.include_router(text_routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 