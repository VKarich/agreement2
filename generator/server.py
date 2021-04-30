from typing import Optional
import uvicorn

from template import OUTPUT_FILENAME
from util import generate_file

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

app = FastAPI()


@app.post("/generate/dkp/docx")
async def generate_dkp_docx(r: Request):
    input_json = await r.json()
    generate_file(input_json)
    return FileResponse(OUTPUT_FILENAME, media_type='application/octet-stream')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
