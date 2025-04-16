
from playwright.sync_api import sync_playwright

def get_streaming_link(anime_episode_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto(anime_episode_url)
        page.wait_for_timeout(5000)  # Allow JS to render

        iframe = page.query_selector("iframe")
        if iframe:
            return iframe.get_attribute("src")
        return None
