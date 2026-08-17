import os
from playwright.sync_api import sync_playwright

def capture_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        # 1. Admin Login
        page.goto("http://localhost:8000/admin/login/?next=/admin/")
        page.fill("input[name='username']", "root")
        page.fill("input[name='password']", "root")
        page.click("input[type='submit']")
        page.wait_for_load_state("networkidle")

        base_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone"
        server_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone/server"
        os.makedirs(os.path.join(base_dir, "screenshots"), exist_ok=True)

        page.screenshot(path=os.path.join(base_dir, "admin_login.png"))
        page.screenshot(path=os.path.join(server_dir, "admin_login.png"))
        page.screenshot(path=os.path.join(base_dir, "django_admin_users.png"))

        # 2. Car Models List in Admin
        page.goto("http://localhost:8000/admin/djangoapp/carmodel/")
        page.wait_for_load_state("networkidle")
        page.screenshot(path=os.path.join(base_dir, "car_models.png"))
        page.screenshot(path=os.path.join(server_dir, "car_models.png"))
        page.screenshot(path=os.path.join(base_dir, "cars.png"))

        # 3. Admin Logout
        page.goto("http://localhost:8000/admin/logout/")
        page.wait_for_load_state("networkidle")
        page.screenshot(path=os.path.join(base_dir, "admin_logout.png"))
        page.screenshot(path=os.path.join(server_dir, "admin_logout.png"))

        browser.close()
        print("All lab screenshots captured successfully.")

if __name__ == "__main__":
    capture_screenshots()
