from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# ─────────────────────────────────────────────
# App setup
# ─────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parent

STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"


app = FastAPI(
    title="Fantasy League App",
    version="1.0.0",
)


# ─────────────────────────────────────────────
# Static files
# ─────────────────────────────────────────────

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static",
)


# ─────────────────────────────────────────────
# Templates
# ─────────────────────────────────────────────

templates = Jinja2Templates(
    directory=str(TEMPLATES_DIR)
)


# ─────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "fantasy-league-app"
    }