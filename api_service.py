import socket
import uvicorn
from loguru import logger
from fastapi import Request
from fastapi.responses import JSONResponse, Response
from fastapi import FastAPI
from inference import ChatGPT

app = FastAPI()
gpt = ChatGPT()


def get_host_ip() -> str:
    """
    :return: ip
    """
    s = None
    ip = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception as e:
        logger.info(e)
    finally:
        s.close()
        return ip


@app.post("/v1/completions")
async def completions(request: Request) -> Response:
    request_dict = await request.json()
    prompt = request_dict.pop("prompt")

    answer = gpt.chat(prompt)
    return JSONResponse(answer)


if __name__ == "__main__":
    uvicorn.run(app, host=get_host_ip(), port=8000)
