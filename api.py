from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from generator import generate_bulk, process_single_certificate
import os

app = FastAPI()

class SoloRequest(BaseModel):
    name: str

@app.post("/generate/solo")
async def api_solo_generate(request: SoloRequest):
    try:
        result = process_single_certificate(request.name)
        result["download_url"] = f"/download/{request.name.replace(' ', '_')}"
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/download/{safe_name}")
async def download_pdf(safe_name: str):
    pdf_path = f"certificates/{safe_name}/{safe_name}.pdf"
    
    if os.path.exists(pdf_path):
        return FileResponse(
            path=pdf_path, 
            filename=f"{safe_name}.pdf", 
            media_type='application/pdf'
        )
    raise HTTPException(status_code=404, detail="Certificate not found")

@app.post("/generate/bulk")
async def api_bulk_generate():
    try:
        results = generate_bulk()
        return {"status": "success", "count": len(results)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))