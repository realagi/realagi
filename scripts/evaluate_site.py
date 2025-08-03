import os
from pathlib import Path
import asyncio

try:
    import openhands
except Exception:
    openhands = None

from playwright.async_api import async_playwright

DEVPLAN_PATH = Path("docs/devplans/devplan.nextsteps.md")

async def evaluate(url: str) -> None:
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        content = await page.content()
        await browser.close()
    plan_text = "# Dev Plan: Next Steps\n\n"
    if openhands:
        try:
            # Assume openhands provides a 'generate_plan' helper
            plan_text += openhands.generate_plan(content)
        except Exception as exc:
            plan_text += f"OpenHands analysis failed: {exc}\n"
    else:
        plan_text += "OpenHands not available; review manually.\n"
    DEVPLAN_PATH.write_text(plan_text)

if __name__ == "__main__":
    url = os.environ.get("WEBSITE_URL", "http://localhost")
    asyncio.run(evaluate(url))
