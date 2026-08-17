from playwright.sync_api import sync_playwright
import os

def capture_dealer_reviews_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})

        base_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone"
        server_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone/server"

        # Navigate to dealer 15 first to establish origin
        page.goto("http://localhost:8000/dealer/15")
        page.evaluate("sessionStorage.setItem('username', 'root')")
        page.goto("http://localhost:8000/dealer/15")
        page.wait_for_selector(".review_panel")
        page.wait_for_timeout(1500)

        page.screenshot(path=os.path.join(base_dir, "dealer_id_reviews.png"))
        page.screenshot(path=os.path.join(server_dir, "dealer_id_reviews.png"))

        browser.close()
        print("Captured dealer_id_reviews.png successfully.")

if __name__ == "__main__":
    capture_dealer_reviews_screenshot()
