import asyncio
import websockets

async def handle_connection(websocket):
    message = await websocket.recv()
    print(f"[REAL SERVER] Final message received: {message}")

async def main():
    async with websockets.serve(handle_connection, "localhost", 8766):
        print("[REAL SERVER] Listening on ws://localhost:8766")
        await asyncio.Future()

asyncio.run(main())
