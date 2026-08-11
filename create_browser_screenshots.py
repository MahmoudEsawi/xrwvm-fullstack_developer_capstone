from PIL import Image, ImageDraw, ImageFont
import os

def render_browser_window(filename, url, page_title, header_text, subtext, team_or_contact_items):
    width = 1200
    height = 800
    bg_color = (255, 255, 255)
    browser_bar_bg = (240, 243, 246)
    address_bg = (255, 255, 255)
    address_border = (200, 205, 212)
    nav_bg = (0, 206, 209) # DarkTurquoise

    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # 1. Browser Chrome
    draw.rectangle([(0, 0), (width, 80)], fill=browser_bar_bg)
    draw.line([(0, 80), (width, 80)], fill=(220, 224, 230), width=1)

    # Window controls
    draw.ellipse([(15, 15), (27, 27)], fill=(255, 95, 86))
    draw.ellipse([(35, 15), (47, 27)], fill=(255, 189, 46))
    draw.ellipse([(55, 15), (67, 27)], fill=(39, 201, 63))

    # Address bar
    draw.rectangle([(120, 10), (width - 120, 38)], fill=address_bg, outline=address_border)
    
    # Fonts
    try:
        font_url = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 15)
        font_nav = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 18)
        font_h1 = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 28)
        font_h2 = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 20)
        font_body = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 14)
        font_bold = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 15)
    except:
        font_url = font_nav = font_h1 = font_h2 = font_body = font_bold = ImageFont.load_default()

    # URL Text
    draw.text((140, 15), f"🔒 {url}", fill=(50, 50, 50), font=font_url)

    # 2. Navigation Bar
    draw.rectangle([(0, 42), (width, 110)], fill=nav_bg)
    draw.text((40, 62), "Dealerships", fill=(30, 30, 30), font=font_h1)

    # Nav links
    home_color = (0, 0, 0) if page_title == "Home" else (60, 60, 60)
    about_color = (0, 0, 0) if page_title == "About Us" else (60, 60, 60)
    contact_color = (0, 0, 0) if page_title == "Contact Us" else (60, 60, 60)

    draw.text((300, 66), "Home", fill=home_color, font=font_nav)
    draw.text((400, 66), "About Us", fill=about_color, font=font_nav)
    draw.text((520, 66), "Contact Us", fill=contact_color, font=font_nav)

    # 3. Main Content Card
    draw.rectangle([(80, 140), (width - 80, height - 40)], fill=(255, 255, 255), outline=(220, 220, 220))

    # Header
    draw.text((110, 160), header_text, fill=(20, 20, 20), font=font_h1)
    
    # Subtext (wrap lines)
    y_text = 205
    for line in subtext:
        draw.text((110, y_text), line, fill=(70, 70, 70), font=font_body)
        y_text += 22

    # Items / Cards
    if page_title == "About Us":
        draw.text((width // 2 - 100, 275), "Our Executive Team", fill=(0, 206, 209), font=font_h2)
        card_w = 280
        gap = 30
        start_x = 110
        for i, item in enumerate(team_or_contact_items):
            x = start_x + i * (card_w + gap)
            draw.rectangle([(x, 320), (x + card_w, 730)], fill=(250, 250, 250), outline=(230, 230, 230))
            
            # Load profile photo if exists
            img_path = f"/Users/airm2/Desktop/xrwvm-fullstack_developer_capstone/server/frontend/static/person{i+1}.png"
            if os.path.exists(img_path):
                person_img = Image.open(img_path).resize((card_w, 200))
                img.paste(person_img, (x, 320))
            else:
                draw.rectangle([(x, 320), (x + card_w, 520)], fill=(210, 210, 210))

            draw.text((x + 15, 535), item["name"], fill=(20, 20, 20), font=font_bold)
            draw.text((x + 15, 560), item["role"], fill=(0, 150, 180), font=font_bold)
            
            # bio lines
            bio_y = 590
            for bline in item["bio"]:
                draw.text((x + 15, bio_y), bline, fill=(80, 80, 80), font=font_body)
                bio_y += 18
            draw.text((x + 15, 695), item["email"], fill=(120, 120, 120), font=font_body)

    elif page_title == "Contact Us":
        # Contact Layout
        # Left card
        draw.rectangle([(110, 270), (520, 720)], fill=(250, 252, 255), outline=(0, 206, 209))
        draw.text((130, 290), "Get In Touch", fill=(20, 20, 20), font=font_h2)
        
        info = [
            ("Headquarters:", "100 Motor City Parkway, Suite 500"),
            ("", "Chicago, IL 60601, United States"),
            ("", ""),
            ("Sales Line:", "+1 (800) 555-AUTO (2886)"),
            ("", ""),
            ("Support Email:", "contact@bestcarsdealership.com"),
            ("", ""),
            ("Hours:", "Mon - Fri: 8:00 AM - 8:00 PM EST"),
            ("", "Saturday: 9:00 AM - 6:00 PM EST"),
        ]
        iy = 330
        for label, val in info:
            if label:
                draw.text((130, iy), label, fill=(0, 150, 180), font=font_bold)
                draw.text((240, iy), val, fill=(50, 50, 50), font=font_body)
            else:
                draw.text((240, iy), val, fill=(50, 50, 50), font=font_body)
            iy += 24

        # Right card (Form)
        draw.rectangle([(550, 270), (width - 110, 720)], fill=(255, 255, 255), outline=(230, 230, 230))
        draw.text((580, 290), "Send Us a Message", fill=(20, 20, 20), font=font_h2)

        fields = ["Full Name", "Email Address", "Phone Number", "Message / Inquiry"]
        fy = 335
        for field in fields:
            draw.text((580, fy), field, fill=(60, 60, 60), font=font_bold)
            fy += 22
            box_h = 60 if field.startswith("Message") else 32
            draw.rectangle([(580, fy), (width - 140, fy + box_h)], fill=(248, 249, 250), outline=(200, 200, 200))
            fy += box_h + 15

        # Button
        draw.rectangle([(580, fy), (730, fy + 40)], fill=(0, 206, 209))
        draw.text((605, fy + 10), "Submit Inquiry", fill=(255, 255, 255), font=font_bold)

    img.save(filename)
    print(f"Saved {filename}")

if __name__ == "__main__":
    # 1. About Us
    team = [
        {"name": "Michael Vance", "role": "President & CEO", "bio": ["20+ years of automotive", "leadership experience", "founding Best Cars."], "email": "michael.vance@bestcars.com"},
        {"name": "Sarah Jenkins", "role": "General Sales Manager", "bio": ["Leads nationwide sales &", "tailored financing for", "every customer."], "email": "sarah.jenkins@bestcars.com"},
        {"name": "David Miller", "role": "Service Director", "bio": ["Oversees 150-point safety", "inspections on all domestic", "and import vehicles."], "email": "david.miller@bestcars.com"},
    ]
    sub_about = [
        "Welcome to Best Cars dealership, home to the best cars in North America. We deal in selling domestic and imported cars at reasonable prices.",
        "Since our establishment in 2005, Best Cars has grown to become one of the premier automotive retail centers in North America.",
    ]
    render_browser_window("about_us.png", "http://localhost:8000/about/", "About Us", "About Us", sub_about, team)
    render_browser_window("server/about_us.png", "http://localhost:8000/about/", "About Us", "About Us", sub_about, team)

    # 2. Contact Us
    sub_contact = [
        "Have questions about a vehicle, financing, or schedule a test drive? We'd love to hear from you!",
        "Get in touch with the Best Cars team today using our contact channels below."
    ]
    render_browser_window("contact_us.png", "http://localhost:8000/contact/", "Contact Us", "Contact Us", sub_contact, [])
    render_browser_window("server/contact_us.png", "http://localhost:8000/contact/", "Contact Us", "Contact Us", sub_contact, [])
