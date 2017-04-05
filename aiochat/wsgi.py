import asyncio
from aiochat.app import create_app

app = create_app(asyncio.get_event_loop())
