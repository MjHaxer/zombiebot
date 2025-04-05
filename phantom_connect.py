from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

app = FastAPI()

connected_wallets = {}

@app.get("/connect_callback")
async def connect_callback(request: Request):
    params = dict(request.query_params)
    wallet_address = params.get("public_key")
    user_id = params.get("state", "demo_user")

    connected_wallets[user_id] = wallet_address

    return RedirectResponse(url="https://t.me/ZombieBundler_bot")

@app.get("/get_wallet/{user_id}")
async def get_wallet(user_id: str):
    return {"wallet": connected_wallets.get(user_id, "Not connected")}
