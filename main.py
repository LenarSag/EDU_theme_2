import asyncio

from app.db.database import init_models


if __name__ == "__main__":
    asyncio.run(init_models())
