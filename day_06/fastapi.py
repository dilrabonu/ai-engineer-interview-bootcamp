from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio 

app = FastApi(title="Demo AI")

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/detect", response_model=DetectResponse)

async def grad_cam():
    if file is None:
        raise HTTPException(status_code=400, detail="Not found file")
    grad_csm_result = await asyncio.to_thread(grad_cam_model, file)
    return {"result": grad_csm_result}

@app.post("/copilot")
async def copilot():
    payload = body.model_dump()
    result = generate_paln(payload)
    return JSONResponse(result)

@app.put("/copilot")
async def update_copilot():
    pass

@app.delete("/copilot")
async def delete_copilot():
    pass

# streamlit

st.set_page_config(page_title="balzeVeritas AI", layout="wide")
API_URL_BASE= os.environ.get("API_URL_BASE", "http://localhost:8000")
st.markdown
"""

"""

tabs = st.tabs(["Home", "About", "Contact"])

tab1, tab2, tab3 = tabs
tab1.write("Home")
tab2.write("About")
tab3.write("Contact")

with tab1:
    st.write("Home")

def chunk_text(text, chunk_size=500, chunk_overlap=50):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunks.append(" ".join(words[i:i+chunk_size]))
        i += chunk_size - chunk_overlap
    return chunks


