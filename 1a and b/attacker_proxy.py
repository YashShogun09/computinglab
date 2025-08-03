import asyncio
import websockets

async def attacker_handler(websocket_client):
    async with websockets.connect("ws://localhost:8766") as websocket_server:
        original_message = await websocket_client.recv()
        print(f"[ATTACKER] Intercepted: {original_message}")

        # Simulate message tampering
        tampered_message = "Mid exams are postponed"
        print(f"[ATTACKER] Modified to: {tampered_message}")

        await websocket_server.send(tampered_message)

async def main():
    async with websockets.serve(attacker_handler, "localhost", 8765):
        print("[ATTACKER] Listening on ws://localhost:8765 (intercepts client)")
        await asyncio.Future()

asyncio.run(main())
