from playwright.sync_api import sync_playwright
import os

def capture_dealers_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 800})

        base_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone"
        server_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone/server"

        # 1. get_dealers.png (Logged out - view all dealers)
        page.goto("http://localhost:8000/dealers/")
        page.wait_for_selector("table")
        page.wait_for_timeout(1500)
        page.screenshot(path=os.path.join(base_dir, "get_dealers.png"))
        page.screenshot(path=os.path.join(server_dir, "get_dealers.png"))

        # 2. dealersbystate.png (Filtered by state - Kansas)
        page.select_option("select#state", value="Kansas")
        page.wait_for_timeout(1500)
        page.screenshot(path=os.path.join(base_dir, "dealersbystate.png"))
        page.screenshot(path=os.path.join(server_dir, "dealersbystate.png"))

        # 3. get_dealers_loggedin.png (Logged in state with review dealer column)
        page.evaluate("sessionStorage.setItem('username', 'root')")
        page.goto("http://localhost:8000/dealers/")
        page.wait_for_selector("table")
        page.wait_for_timeout(1500)
        page.screenshot(path=os.path.join(base_dir, "get_dealers_loggedin.png"))
        page.screenshot(path=os.path.join(server_dir, "get_dealers_loggedin.png"))

        browser.close()
        print("Captured get_dealers.png, dealersbystate.png, and get_dealers_loggedin.png successfully.")

if __name__ == "__main__":
    capture_dealers_screenshots()
