from playwright.sync_api import sync_playwright
import os

def capture_review_submission():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 850})

        base_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone"
        server_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone/server"

        # Establish origin and session storage
        page.goto("http://localhost:8000/postreview/15")
        page.evaluate("sessionStorage.setItem('username', 'root')")
        page.evaluate("sessionStorage.setItem('firstname', 'Root')")
        page.evaluate("sessionStorage.setItem('lastname', 'Admin')")

        page.goto("http://localhost:8000/postreview/15")
        page.wait_for_selector("textarea#review")
        page.wait_for_timeout(1000)

        # Fill out review form
        page.fill("textarea#review", "Outstanding customer service and fantastic dealership experience!")
        page.fill("input[type='date']", "2023-10-15")
        page.select_option("select#cars", index=1)
        page.fill("input[type='int']", "2023")

        page.wait_for_timeout(1000)

        # 1. Screenshot BEFORE submitting review
        page.screenshot(path=os.path.join(base_dir, "dealership_review_submission.png"))
        page.screenshot(path=os.path.join(server_dir, "dealership_review_submission.png"))

        # Submit review
        page.click("button.postreview")
        page.wait_for_timeout(3000)

        # 2. Screenshot AFTER review is posted and redirected to dealer page
        page.screenshot(path=os.path.join(base_dir, "added_review.png"))
        page.screenshot(path=os.path.join(server_dir, "added_review.png"))

        browser.close()
        print("Captured dealership_review_submission.png and added_review.png successfully.")

if __name__ == "__main__":
    capture_review_submission()
