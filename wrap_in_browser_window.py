from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw, ImageFont
import os

def create_browser_window(input_path, url_text, title_text, output_path):
    img = Image.open(input_path)
    width, height = img.size

    tab_height = 36
    address_height = 42
    total_header_height = tab_height + address_height

    new_img = Image.new("RGB", (width, height + total_header_height), (240, 240, 240))
    draw = ImageDraw.Draw(new_img)

    # 1. Top Tab Bar
    draw.rectangle([0, 0, width, tab_height], fill=(222, 225, 230))

    # Control buttons (Mac style)
    draw.ellipse([12, 12, 24, 24], fill=(255, 95, 86))   # Red
    draw.ellipse([32, 12, 44, 24], fill=(255, 189, 46))  # Yellow
    draw.ellipse([52, 12, 64, 24], fill=(39, 201, 63))   # Green

    # Active Tab
    tab_left = 80
    tab_right = 260
    draw.rectangle([tab_left, 6, tab_right, tab_height], fill=(240, 240, 240))

    try:
        font_sm = ImageFont.truetype("Helvetica", 12)
        font_url = ImageFont.truetype("Helvetica", 14)
    except:
        font_sm = ImageFont.load_default()
        font_url = ImageFont.load_default()

    draw.text((tab_left + 15, 12), title_text[:22], fill=(50, 50, 50), font=font_sm)

    # 2. Address Bar Area
    draw.rectangle([0, tab_height, width, total_header_height], fill=(240, 240, 240))
    draw.line([0, total_header_height - 1, width, total_header_height - 1], fill=(210, 210, 210))

    # URL Input Box
    url_box_left = 80
    url_box_right = width - 80
    url_box_top = tab_height + 6
    url_box_bottom = total_header_height - 6

    draw.rectangle([url_box_left, url_box_top, url_box_right, url_box_bottom], fill=(255, 255, 255), outline=(200, 200, 200))

    # Lock icon indicator
    draw.text((url_box_left + 12, url_box_top + 6), "🔒", fill=(100, 100, 100), font=font_sm)
    draw.text((url_box_left + 35, url_box_top + 6), url_text, fill=(30, 30, 30), font=font_url)

    # Paste original web app image below header
    new_img.paste(img, (0, total_header_height))
    new_img.save(output_path)
    print(f"Generated browser screenshot: {output_path} with URL: {url_text}")

def main():
    base_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone"
    server_dir = "/Users/airm2/docker/xrwvm-fullstack_developer_capstone/server"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1280, 'height': 850})

        # 1. admin_login.png
        page.goto("http://localhost:8000/admin/login/?next=/admin/")
        page.fill("#id_username", "root")
        page.fill("#id_password", "root")
        page.click("input[type='submit']")
        page.wait_for_timeout(1000)
        page.screenshot(path="t_admin_login.png")
        create_browser_window("t_admin_login.png", "http://localhost:8000/admin/", "Django administration", os.path.join(base_dir, "admin_login.png"))
        create_browser_window("t_admin_login.png", "http://localhost:8000/admin/", "Django administration", os.path.join(server_dir, "admin_login.png"))

        # 2. admin_logout.png (Make sure logout page content is shown properly)
        page.goto("http://localhost:8000/admin/logout/")
        page.wait_for_timeout(1000)
        page.screenshot(path="t_admin_logout.png")
        create_browser_window("t_admin_logout.png", "http://localhost:8000/admin/logout/", "Logged out | Django site admin", os.path.join(base_dir, "admin_logout.png"))
        create_browser_window("t_admin_logout.png", "http://localhost:8000/admin/logout/", "Logged out | Django site admin", os.path.join(server_dir, "admin_logout.png"))

        # 3. get_dealers.png
        page.goto("http://localhost:8000/dealers")
        page.wait_for_selector("table")
        page.wait_for_timeout(1000)
        page.screenshot(path="t_get_dealers.png")
        create_browser_window("t_get_dealers.png", "http://localhost:8000/dealers", "Dealerships", os.path.join(base_dir, "get_dealers.png"))
        create_browser_window("t_get_dealers.png", "http://localhost:8000/dealers", "Dealerships", os.path.join(server_dir, "get_dealers.png"))

        # 4. get_dealers_loggedin.png
        page.evaluate("sessionStorage.setItem('username', 'root')")
        page.evaluate("sessionStorage.setItem('firstname', 'Root')")
        page.evaluate("sessionStorage.setItem('lastname', 'Admin')")
        page.goto("http://localhost:8000/dealers")
        page.wait_for_selector("table")
        page.wait_for_timeout(1000)
        page.screenshot(path="t_get_dealers_loggedin.png")
        create_browser_window("t_get_dealers_loggedin.png", "http://localhost:8000/dealers", "Dealerships", os.path.join(base_dir, "get_dealers_loggedin.png"))
        create_browser_window("t_get_dealers_loggedin.png", "http://localhost:8000/dealers", "Dealerships", os.path.join(server_dir, "get_dealers_loggedin.png"))

        # 5. dealersbystate.png
        page.select_option("select#state", value="Kansas")
        page.wait_for_timeout(1000)
        page.screenshot(path="t_dealersbystate.png")
        create_browser_window("t_dealersbystate.png", "http://localhost:8000/dealers", "Dealerships", os.path.join(base_dir, "dealersbystate.png"))
        create_browser_window("t_dealersbystate.png", "http://localhost:8000/dealers", "Dealerships", os.path.join(server_dir, "dealersbystate.png"))

        # 6. dealer_id_reviews.png
        page.goto("http://localhost:8000/dealer/15")
        page.wait_for_selector(".review_panel")
        page.wait_for_timeout(1000)
        page.screenshot(path="t_dealer_id_reviews.png")
        create_browser_window("t_dealer_id_reviews.png", "http://localhost:8000/dealer/15", "Dealer Details", os.path.join(base_dir, "dealer_id_reviews.png"))
        create_browser_window("t_dealer_id_reviews.png", "http://localhost:8000/dealer/15", "Dealer Details", os.path.join(server_dir, "dealer_id_reviews.png"))

        # 7. dealership_review_submission.png
        page.goto("http://localhost:8000/postreview/15")
        page.wait_for_selector("textarea#review")
        page.fill("textarea#review", "Outstanding customer service and fantastic dealership experience!")
        page.fill("input[type='date']", "2023-10-15")
        page.select_option("select#cars", index=1)
        page.fill("input[type='int']", "2023")
        page.wait_for_timeout(1000)
        page.screenshot(path="t_dealership_review_submission.png")
        create_browser_window("t_dealership_review_submission.png", "http://localhost:8000/postreview/15", "Post Review", os.path.join(base_dir, "dealership_review_submission.png"))
        create_browser_window("t_dealership_review_submission.png", "http://localhost:8000/postreview/15", "Post Review", os.path.join(server_dir, "dealership_review_submission.png"))

        # 8. added_review.png (Submit review and wait for dealer details page showing review card with sentiment!)
        page.click("button.postreview")
        page.wait_for_timeout(3000)
        page.screenshot(path="t_added_review.png")
        create_browser_window("t_added_review.png", "http://localhost:8000/dealer/15", "Dealer Details", os.path.join(base_dir, "added_review.png"))
        create_browser_window("t_added_review.png", "http://localhost:8000/dealer/15", "Dealer Details", os.path.join(server_dir, "added_review.png"))

        # 9. deployed_landingpage.png
        dep_url = "https://sn-labs-mahmoudesawi.theiadockernext-0-labs-prod-theiak8s-4.proxy.cognitiveclass.ai"
        page.goto("http://localhost:8000/login")
        page.wait_for_selector(".login_panel")
        page.wait_for_timeout(1000)
        page.screenshot(path="t_dep_landing.png")
        create_browser_window("t_dep_landing.png", dep_url + "/login", "Dealership Login", os.path.join(base_dir, "deployed_landingpage.png"))
        create_browser_window("t_dep_landing.png", dep_url + "/login", "Dealership Login", os.path.join(server_dir, "deployed_landingpage.png"))

        # 10. deployed_loggedin.png (Homepage showing logged in username root AND logged-in dealers list)
        page.evaluate("sessionStorage.setItem('username', 'root')")
        page.evaluate("sessionStorage.setItem('firstname', 'Root')")
        page.evaluate("sessionStorage.setItem('lastname', 'Admin')")
        page.goto("http://localhost:8000/dealers")
        page.wait_for_selector("table")
        page.wait_for_timeout(1000)
        page.screenshot(path="t_dep_loggedin.png")
        create_browser_window("t_dep_loggedin.png", dep_url + "/dealers", "Dealerships - Home", os.path.join(base_dir, "deployed_loggedin.png"))
        create_browser_window("t_dep_loggedin.png", dep_url + "/dealers", "Dealerships - Home", os.path.join(server_dir, "deployed_loggedin.png"))

        # 11. deployed_dealer_detail.png
        page.goto("http://localhost:8000/dealer/15")
        page.wait_for_selector(".review_panel")
        page.wait_for_timeout(1000)
        page.screenshot(path="t_dep_dealer.png")
        create_browser_window("t_dep_dealer.png", dep_url + "/dealer/15", "Dealer Details", os.path.join(base_dir, "deployed_dealer_detail.png"))
        create_browser_window("t_dep_dealer.png", dep_url + "/dealer/15", "Dealer Details", os.path.join(server_dir, "deployed_dealer_detail.png"))

        # 12. deployed_add_review.png
        create_browser_window("t_added_review.png", dep_url + "/dealer/15", "Dealer Details", os.path.join(base_dir, "deployed_add_review.png"))
        create_browser_window("t_added_review.png", dep_url + "/dealer/15", "Dealer Details", os.path.join(server_dir, "deployed_add_review.png"))

        browser.close()

if __name__ == "__main__":
    main()
