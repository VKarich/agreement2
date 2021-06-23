import uvicorn
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse

from generator.template import OUTPUT_FILENAME
from parser.rosreestr import get_result_rossreestr
from util import generate_file

app = FastAPI()


@app.post("/generate/dkp/docx")
async def generate_dkp_docx(r: Request):
    input_json = await r.json()
    generate_file(input_json)
    return FileResponse(OUTPUT_FILENAME, media_type='application/octet-stream')


@app.get("/data/kadastr/{object_id}")
async def read_item(object_id: str):
    return JSONResponse(get_result_rossreestr(object_id))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
