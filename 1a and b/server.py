import asyncio
import websockets

async def handle_connection(websocket):
    message = await websocket.recv()
    print(f"[SERVER] Received message: {message}")

async def main():
    async with websockets.serve(handle_connection, "localhost", 8765):
        print("[SERVER] Listening on ws://localhost:8765")
        await asyncio.Future()  # run forever

asyncio.run(main())
