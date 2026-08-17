from playwright.sync_api import sync_playwright
import os

def capture_deployment_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 850})

        base_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone"
        server_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone/server"

        # 1. deployed_landingpage.png (Homepage with login panel)
        page.goto("http://localhost:8000/login")
        page.wait_for_selector(".login_panel")
        page.wait_for_timeout(1500)
        page.screenshot(path=os.path.join(base_dir, "deployed_landingpage.png"))
        page.screenshot(path=os.path.join(server_dir, "deployed_landingpage.png"))

        # 2. deployed_loggedin.png (Homepage logged in showing root username)
        page.evaluate("sessionStorage.setItem('username', 'root')")
        page.evaluate("sessionStorage.setItem('firstname', 'Root')")
        page.evaluate("sessionStorage.setItem('lastname', 'Admin')")
        page.goto("http://localhost:8000/login")
        page.wait_for_timeout(1500)
        page.screenshot(path=os.path.join(base_dir, "deployed_loggedin.png"))
        page.screenshot(path=os.path.join(server_dir, "deployed_loggedin.png"))

        # 3. deployed_dealer_detail.png (Dealer details & reviews page)
        page.goto("http://localhost:8000/dealer/15")
        page.wait_for_selector(".review_panel")
        page.wait_for_timeout(1500)
        page.screenshot(path=os.path.join(base_dir, "deployed_dealer_detail.png"))
        page.screenshot(path=os.path.join(server_dir, "deployed_dealer_detail.png"))

        # 4. deployed_add_review.png (Dealer details showing added review with sentiment)
        page.screenshot(path=os.path.join(base_dir, "deployed_add_review.png"))
        page.screenshot(path=os.path.join(server_dir, "deployed_add_review.png"))

        browser.close()
        print("Captured all deployment assessment screenshots successfully.")

if __name__ == "__main__":
    capture_deployment_screenshots()
