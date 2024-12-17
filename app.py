from playwright.sync_api import sync_playwright

def run_playwright():
    with sync_playwright() as p:
        # 启动 Chromium 浏览器的无头模式
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://playwright.dev")
        print("Page title:", page.title())
        browser.close()

if __name__ == "__main__":
    run_playwright()