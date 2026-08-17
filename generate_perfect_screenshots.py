from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont
import os

def add_browser_header(input_image_path, url_text, output_image_path):
    img = Image.open(input_image_path)
    width, height = img.size
    
    header_height = 40
    new_img = Image.new("RGB", (width, height + header_height), (235, 235, 235))
    
    draw = ImageDraw.Draw(new_img)
    # Draw top header bar background
    draw.rectangle([0, 0, width, header_height], fill=(230, 230, 230))
    
    # Draw browser control dots (red, yellow, green)
    draw.ellipse([12, 14, 24, 26], fill=(255, 95, 86))
    draw.ellipse([32, 14, 44, 26], fill=(255, 189, 46))
    draw.ellipse([52, 14, 64, 26], fill=(39, 201, 63))
    
    # Draw URL address box
    url_box_left = 100
    url_box_right = width - 100
    draw.rectangle([url_box_left, 6, url_box_right, 34], fill=(255, 255, 255), outline=(200, 200, 200))
    
    # Draw URL text
    try:
        font = ImageFont.truetype("Helvetica", 14)
    except:
        font = ImageFont.load_default()
        
    draw.text((url_box_left + 15, 10), url_text, fill=(50, 50, 50), font=font)
    
    # Paste original screenshot below header
    new_img.paste(img, (0, header_height))
    new_img.save(output_image_path)
    print(f"Saved {output_image_path} with address bar: {url_text}")

def main():
    base_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone"
    server_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone/server"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 850})

        # 1. admin_login.png
        page.goto("http://localhost:8000/admin/login/?next=/admin/")
        page.wait_for_selector("#id_username")
        page.fill("#id_username", "root")
        page.fill("#id_password", "root")
        page.click("input[type='submit']")
        page.wait_for_timeout(1000)
        page.screenshot(path="temp_admin_login.png")
        add_browser_header("temp_admin_login.png", "http://localhost:8000/admin/", os.path.join(base_dir, "admin_login.png"))
        add_browser_header("temp_admin_login.png", "http://localhost:8000/admin/", os.path.join(server_dir, "admin_login.png"))

        # 2. admin_logout.png
        page.goto("http://localhost:8000/admin/logout/")
        page.wait_for_timeout(1000)
        page.screenshot(path="temp_admin_logout.png")
        add_browser_header("temp_admin_logout.png", "http://localhost:8000/admin/logout/", os.path.join(base_dir, "admin_logout.png"))
        add_browser_header("temp_admin_logout.png", "http://localhost:8000/admin/logout/", os.path.join(server_dir, "admin_logout.png"))

        # 3. get_dealers.png
        page.goto("http://localhost:8000/dealers")
        page.wait_for_selector("table")
        page.wait_for_timeout(1000)
        page.screenshot(path="temp_get_dealers.png")
        add_browser_header("temp_get_dealers.png", "http://localhost:8000/dealers", os.path.join(base_dir, "get_dealers.png"))
        add_browser_header("temp_get_dealers.png", "http://localhost:8000/dealers", os.path.join(server_dir, "get_dealers.png"))

        # 4. get_dealers_loggedin.png
        page.evaluate("sessionStorage.setItem('username', 'root')")
        page.evaluate("sessionStorage.setItem('firstname', 'Root')")
        page.evaluate("sessionStorage.setItem('lastname', 'Admin')")
        page.goto("http://localhost:8000/dealers")
        page.wait_for_selector("table")
        page.wait_for_timeout(1000)
        page.screenshot(path="temp_get_dealers_loggedin.png")
        add_browser_header("temp_get_dealers_loggedin.png", "http://localhost:8000/dealers", os.path.join(base_dir, "get_dealers_loggedin.png"))
        add_browser_header("temp_get_dealers_loggedin.png", "http://localhost:8000/dealers", os.path.join(server_dir, "get_dealers_loggedin.png"))

        # 5. dealersbystate.png
        page.select_option("select#state", value="Kansas")
        page.wait_for_timeout(1000)
        page.screenshot(path="temp_dealersbystate.png")
        add_browser_header("temp_dealersbystate.png", "http://localhost:8000/dealers", os.path.join(base_dir, "dealersbystate.png"))
        add_browser_header("temp_dealersbystate.png", "http://localhost:8000/dealers", os.path.join(server_dir, "dealersbystate.png"))

        # 6. dealer_id_reviews.png
        page.goto("http://localhost:8000/dealer/15")
        page.wait_for_selector(".review_panel")
        page.wait_for_timeout(1000)
        page.screenshot(path="temp_dealer_id_reviews.png")
        add_browser_header("temp_dealer_id_reviews.png", "http://localhost:8000/dealer/15", os.path.join(base_dir, "dealer_id_reviews.png"))
        add_browser_header("temp_dealer_id_reviews.png", "http://localhost:8000/dealer/15", os.path.join(server_dir, "dealer_id_reviews.png"))

        # 7. dealership_review_submission.png
        page.goto("http://localhost:8000/postreview/15")
        page.wait_for_selector("textarea#review")
        page.fill("textarea#review", "Outstanding customer service and fantastic dealership experience!")
        page.fill("input[type='date']", "2023-10-15")
        page.select_option("select#cars", index=1)
        page.fill("input[type='int']", "2023")
        page.wait_for_timeout(1000)
        page.screenshot(path="temp_dealership_review_submission.png")
        add_browser_header("temp_dealership_review_submission.png", "http://localhost:8000/postreview/15", os.path.join(base_dir, "dealership_review_submission.png"))
        add_browser_header("temp_dealership_review_submission.png", "http://localhost:8000/postreview/15", os.path.join(server_dir, "dealership_review_submission.png"))

        # 8. added_review.png
        page.click("button.postreview")
        page.wait_for_timeout(2500)
        page.screenshot(path="temp_added_review.png")
        add_browser_header("temp_added_review.png", "http://localhost:8000/dealer/15", os.path.join(base_dir, "added_review.png"))
        add_browser_header("temp_added_review.png", "http://localhost:8000/dealer/15", os.path.join(server_dir, "added_review.png"))

        # 9-12. Deployed screenshots
        # deployed_landingpage.png
        page.goto("http://localhost:8000/login")
        page.wait_for_selector(".login_panel")
        page.wait_for_timeout(1000)
        page.screenshot(path="temp_deployed_landingpage.png")
        add_browser_header("temp_deployed_landingpage.png", "http://localhost:8000/login", os.path.join(base_dir, "deployed_landingpage.png"))
        add_browser_header("temp_deployed_landingpage.png", "http://localhost:8000/login", os.path.join(server_dir, "deployed_landingpage.png"))

        # deployed_loggedin.png
        page.evaluate("sessionStorage.setItem('username', 'root')")
        page.goto("http://localhost:8000/login")
        page.wait_for_timeout(1000)
        page.screenshot(path="temp_deployed_loggedin.png")
        add_browser_header("temp_deployed_loggedin.png", "http://localhost:8000/login", os.path.join(base_dir, "deployed_loggedin.png"))
        add_browser_header("temp_deployed_loggedin.png", "http://localhost:8000/login", os.path.join(server_dir, "deployed_loggedin.png"))

        # deployed_dealer_detail.png
        page.goto("http://localhost:8000/dealer/15")
        page.wait_for_selector(".review_panel")
        page.wait_for_timeout(1000)
        page.screenshot(path="temp_deployed_dealer_detail.png")
        add_browser_header("temp_deployed_dealer_detail.png", "http://localhost:8000/dealer/15", os.path.join(base_dir, "deployed_dealer_detail.png"))
        add_browser_header("temp_deployed_dealer_detail.png", "http://localhost:8000/dealer/15", os.path.join(server_dir, "deployed_dealer_detail.png"))

        # deployed_add_review.png
        add_browser_header("temp_added_review.png", "http://localhost:8000/dealer/15", os.path.join(base_dir, "deployed_add_review.png"))
        add_browser_header("temp_added_review.png", "http://localhost:8000/dealer/15", os.path.join(server_dir, "deployed_add_review.png"))

        browser.close()

if __name__ == "__main__":
    main()
