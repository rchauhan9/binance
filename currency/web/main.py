import asyncio
import json
import websockets
import os
from binance import AsyncClient, BinanceSocketManager

api_key = os.environ.get('BINANCE_API_KEY')
api_secret = os.environ.get('BINANCE_SECRET_KEY')


async def currency(websocket, path):
    client = await AsyncClient.create()
    bm = BinanceSocketManager(client)
    ts = bm.multiplex_socket([path[1:]+'@ticker'])
    async with ts as tscm:
        while True:
            res = await tscm.recv()
            await websocket.send(json.dumps(res))

if __name__ == "__main__":
    start_server = websockets.serve(currency, "127.0.0.1", 5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()