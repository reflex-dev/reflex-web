from pcweb.constants import RX_BUILD_BACKEND
from pcweb.utils.http import default_client

BASE_URL = RX_BUILD_BACKEND.rstrip("/")


async def fetch_all_templates() -> list[dict]:
    client = default_client()
    async with client.get(f"{BASE_URL}/api/v1/flexgen/templates/details") as resp:
        resp.raise_for_status()
        return await resp.json()


async def fetch_template_detail(template_id: str) -> dict:
    client = default_client()
    async with client.get(f"{BASE_URL}/api/v1/flexgen/templates/{template_id}") as resp:
        resp.raise_for_status()
        return await resp.json()
