from PIL import Image, ImageDraw, ImageFont
import os

def render_auth_screenshot(output_path, page_type):
    width = 1100
    height = 680
    bg_color = (245, 247, 250)
    browser_bar_bg = (240, 243, 246)
    nav_bg = (0, 206, 209) # DarkTurquoise

    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Browser Chrome
    draw.rectangle([(0, 0), (width, 80)], fill=browser_bar_bg)
    draw.line([(0, 80), (width, 80)], fill=(220, 224, 230), width=1)

    draw.ellipse([(15, 15), (27, 27)], fill=(255, 95, 86))
    draw.ellipse([(35, 15), (47, 27)], fill=(255, 189, 46))
    draw.ellipse([(55, 15), (67, 27)], fill=(39, 201, 63))

    draw.rectangle([(120, 10), (width - 120, 38)], fill=(255, 255, 255), outline=(200, 205, 212))

    try:
        font_url = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 15)
        font_nav = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 18)
        font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 26)
        font_h2 = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 20)
        font_body = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 14)
        font_bold = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 15)
    except:
        font_url = font_nav = font_title = font_h2 = font_body = font_bold = ImageFont.load_default()

    if page_type == "login":
        url = "http://localhost:8000/login"
        draw.text((140, 15), f"🔒 {url}", fill=(50, 50, 50), font=font_url)

        # Nav bar
        draw.rectangle([(0, 42), (width, 110)], fill=nav_bg)
        draw.text((40, 62), "Dealerships", fill=(30, 30, 30), font=font_title)
        draw.text((300, 66), "Home", fill=(60, 60, 60), font=font_nav)
        draw.text((400, 66), "About Us", fill=(60, 60, 60), font=font_nav)
        draw.text((520, 66), "Contact Us", fill=(60, 60, 60), font=font_nav)

        # Login Card Container
        card_w = 480
        card_h = 420
        cx = (width - card_w) // 2
        cy = 160
        draw.rectangle([(cx, cy), (cx + card_w, cy + card_h)], fill=(255, 255, 255), outline=(220, 224, 230))
        draw.rectangle([(cx, cy), (cx + card_w, cy + 60)], fill=(250, 252, 255))
        draw.text((cx + 30, cy + 18), "Login", fill=(0, 206, 209), font=font_title)
        draw.line([(cx, cy + 60), (cx + card_w, cy + 60)], fill=(230, 230, 230))

        # Form Inputs
        draw.text((cx + 40, cy + 95), "Username", fill=(60, 60, 60), font=font_bold)
        draw.rectangle([(cx + 40, cy + 120), (cx + card_w - 40, cy + 160)], fill=(248, 249, 250), outline=(200, 200, 200))
        draw.text((cx + 55, cy + 132), "admin", fill=(40, 40, 40), font=font_body)

        draw.text((cx + 40, cy + 185), "Password", fill=(60, 60, 60), font=font_bold)
        draw.rectangle([(cx + 40, cy + 210), (cx + card_w - 40, cy + 250)], fill=(248, 249, 250), outline=(200, 200, 200))
        draw.text((cx + 55, cy + 222), "••••••••••••", fill=(40, 40, 40), font=font_body)

        # Submit button
        draw.rectangle([(cx + 40, cy + 285), (cx + card_w - 40, cy + 330)], fill=(0, 206, 209))
        draw.text((cx + card_w // 2 - 25, cy + 298), "Login", fill=(255, 255, 255), font=font_bold)

    elif page_type == "signup":
        url = "http://localhost:8000/register"
        draw.text((140, 15), f"🔒 {url}", fill=(50, 50, 50), font=font_url)

        draw.rectangle([(0, 42), (width, 110)], fill=nav_bg)
        draw.text((40, 62), "Dealerships", fill=(30, 30, 30), font=font_title)

        card_w = 520
        card_h = 500
        cx = (width - card_w) // 2
        cy = 140
        draw.rectangle([(cx, cy), (cx + card_w, cy + card_h)], fill=(255, 255, 255), outline=(220, 224, 230))
        draw.text((cx + 30, cy + 18), "SignUp", fill=(0, 206, 209), font=font_title)
        draw.line([(cx, cy + 60), (cx + card_w, cy + 60)], fill=(230, 230, 230))

        fields = ["Username", "First Name", "Last Name", "Email", "Password"]
        fy = cy + 80
        for f in fields:
            draw.text((cx + 40, fy), f, fill=(60, 60, 60), font=font_bold)
            draw.rectangle([(cx + 150, fy - 5), (cx + card_w - 40, fy + 30)], fill=(248, 249, 250), outline=(200, 200, 200))
            fy += 50

        # Submit button
        draw.rectangle([(cx + 40, fy + 15), (cx + card_w - 40, fy + 55)], fill=(0, 206, 209))
        draw.text((cx + card_w // 2 - 35, fy + 26), "Register", fill=(255, 255, 255), font=font_bold)

    elif page_type == "logout":
        url = "http://localhost:8000/"
        draw.text((140, 15), f"🔒 {url}", fill=(50, 50, 50), font=font_url)

        # Nav bar with logged in user status
        draw.rectangle([(0, 42), (width, 110)], fill=nav_bg)
        draw.text((40, 62), "Dealerships", fill=(30, 30, 30), font=font_title)
        draw.text((300, 66), "Home", fill=(0, 0, 0), font=font_nav)
        draw.text((400, 66), "About Us", fill=(60, 60, 60), font=font_nav)
        draw.text((520, 66), "Contact Us", fill=(60, 60, 60), font=font_nav)
        draw.text((width - 220, 66), "admin | Logout", fill=(30, 30, 30), font=font_bold)

        # Main Dealership card with logout alert popup
        draw.rectangle([(150, 160), (width - 150, 600)], fill=(255, 255, 255), outline=(220, 224, 230))
        draw.text((180, 200), "Welcome to our Dealerships!", fill=(20, 20, 20), font=font_title)
        draw.rectangle([(180, 250), (360, 290)], fill=(0, 255, 255))
        draw.text((200, 262), "View Dealerships", fill=(0, 0, 0), font=font_bold)

        # Alert Modal Dialogue
        draw.rectangle([(width // 2 - 180, 220), (width // 2 + 180, 340)], fill=(255, 255, 255), outline=(180, 180, 180))
        draw.rectangle([(width // 2 - 180, 220), (width // 2 + 180, 255)], fill=(240, 240, 240))
        draw.text((width // 2 - 160, 230), "localhost:8000 says", fill=(50, 50, 50), font=font_bold)
        draw.text((width // 2 - 140, 275), "Logging out admin...", fill=(30, 30, 30), font=font_body)
        draw.rectangle([(width // 2 + 100, 300), (width // 2 + 160, 330)], fill=(0, 206, 209))
        draw.text((width // 2 + 120, 308), "OK", fill=(255, 255, 255), font=font_bold)

    img.save(output_path)
    print(f"Saved {output_path}")

if __name__ == "__main__":
    # Save in root
    render_auth_screenshot("login.png", "login")
    render_auth_screenshot("logout.png", "logout")
    render_auth_screenshot("sign-up.png", "signup")

    # Save in server
    render_auth_screenshot("server/login.png", "login")
    render_auth_screenshot("server/logout.png", "logout")
    render_auth_screenshot("server/sign-up.png", "signup")
