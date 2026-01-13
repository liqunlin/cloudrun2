import os
import torch
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/health")
def health():
    return PlainTextResponse("ok")

@app.get("/")
def root():
    # GPU 检查
    cuda_available = torch.cuda.is_available()
    gpu_count = torch.cuda.device_count()
    gpu_name = torch.cuda.get_device_name(0) if cuda_available else "N/A"

    msg = f"hello-ai-test | CUDA: {cuda_available} | GPU count: {gpu_count} | GPU name: {gpu_name}"
    return PlainTextResponse(msg)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
