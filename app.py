import os
import logging
import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

logger = logging.getLogger("uvicorn.server")
handler = logging.StreamHandler()
logger.addHandler(handler)

hostname = os.getenv("HOSTNAME", "unknown")


async def get(request):
    return JSONResponse(
        {
            "greeting": "Hello World!",
            "host": hostname,
        }
    )


async def post(request):
    request_data = await request.json()
    logger.info(f"Received payload for host '{hostname}': {request_data}")

    name = request_data.get("name", "World")
    return JSONResponse(
        {
            "greeting": f"Hello {name}!",
            "host": hostname,
        }
    )


routes = [
    Route("/", endpoint=get, methods=["GET"]),
    Route("/greet", endpoint=post, methods=["POST"]),
]

app = Starlette(routes=routes)


# Uvicorn
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        log_level=logging.DEBUG,
    )
