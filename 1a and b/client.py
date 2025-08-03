import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8765"
    message = input("Enter your message to send: ")
    
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        print(f"[CLIENT] Sent: {message}")

asyncio.run(send_message())
