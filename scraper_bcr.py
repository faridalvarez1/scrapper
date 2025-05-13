
import asyncio
from playwright.async_api import async_playwright
import pandas as pd
import datetime

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.bcr.com.ar/es/mercados/mercado-de-granos/cotizaciones/cotizaciones-locales-0")
        await page.wait_for_selector("table")
        content = await page.content()
        await browser.close()
        df = pd.read_html(content)[0]

        # Guardar con fecha
        fecha = datetime.datetime.now().strftime('%Y-%m-%d')
        df.to_csv(f"cotizaciones_bcr_{fecha}.csv", index=False)
        print(f"Archivo guardado: cotizaciones_bcr_{fecha}.csv")

# Ejecutar
asyncio.run(run())
