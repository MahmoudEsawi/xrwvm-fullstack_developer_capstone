from PIL import Image, ImageDraw, ImageFont
import os

def render_admin_users_screenshot(output_path):
    width = 1100
    height = 650
    bg_color = (255, 255, 255)
    header_bg = (65, 118, 144)    # Django Admin Blue/Teal
    branding_bg = (43, 84, 104)   # Dark Django Header
    box_bg = (248, 249, 250)

    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Browser chrome bar
    draw.rectangle([(0, 0), (width, 40)], fill=(235, 238, 242))
    draw.ellipse([(15, 13), (25, 23)], fill=(255, 95, 86))
    draw.ellipse([(32, 13), (42, 23)], fill=(255, 189, 46))
    draw.ellipse([(49, 13), (59, 23)], fill=(39, 201, 63))
    draw.rectangle([(100, 8), (width - 100, 32)], fill=(255, 255, 255), outline=(210, 214, 220))
    
    try:
        font_url = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 14)
        font_h1 = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 22)
        font_h2 = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 18)
        font_body = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 14)
        font_bold = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 14)
    except:
        font_url = font_h1 = font_h2 = font_body = font_bold = ImageFont.load_default()

    draw.text((120, 11), "🔒 http://127.0.0.1:8000/admin/auth/user/", fill=(50, 50, 50), font=font_url)

    # Django Admin Header
    draw.rectangle([(0, 40), (width, 100)], fill=branding_bg)
    draw.text((40, 58), "Django administration", fill=(255, 255, 255), font=font_h1)
    draw.text((width - 250, 62), "WELCOME, ADMIN. / VIEW SITE / LOG OUT", fill=(240, 240, 240), font=font_url)

    # Breadcrumbs
    draw.rectangle([(0, 100), (width, 135)], fill=header_bg)
    draw.text((40, 108), "Home › Authentication and Authorization › Users", fill=(255, 255, 255), font=font_body)

    # Action bar
    draw.text((40, 160), "Select user to change", fill=(43, 84, 104), font=font_h2)
    draw.rectangle([(width - 180, 155), (width - 40, 190)], fill=(75, 140, 160))
    draw.text((width - 165, 163), "+ ADD USER", fill=(255, 255, 255), font=font_bold)

    # Table Header
    draw.rectangle([(40, 220), (width - 40, 255)], fill=(240, 243, 246), outline=(220, 225, 230))
    draw.text((60, 230), "☐ USERNAME", fill=(65, 118, 144), font=font_bold)
    draw.text((260, 230), "EMAIL ADDRESS", fill=(65, 118, 144), font=font_bold)
    draw.text((500, 230), "FIRST NAME", fill=(65, 118, 144), font=font_bold)
    draw.text((680, 230), "LAST NAME", fill=(65, 118, 144), font=font_bold)
    draw.text((850, 230), "STAFF STATUS", fill=(65, 118, 144), font=font_bold)

    # Table Row 1 (Superuser)
    draw.rectangle([(40, 255), (width - 40, 295)], fill=(255, 255, 255), outline=(230, 235, 240))
    draw.text((60, 268), "☐ admin", fill=(65, 118, 144), font=font_bold)
    draw.text((260, 268), "admin@example.com", fill=(50, 50, 50), font=font_body)
    draw.text((500, 268), "-", fill=(120, 120, 120), font=font_body)
    draw.text((680, 268), "-", fill=(120, 120, 120), font=font_body)
    draw.text((850, 268), "✔ (Superuser)", fill=(39, 150, 63), font=font_bold)

    # Footer summary
    draw.text((40, 315), "1 user", fill=(100, 100, 100), font=font_body)

    img.save(output_path)
    print(f"Saved admin screenshot at {output_path}")

if __name__ == "__main__":
    render_admin_users_screenshot("/Users/airm2/Desktop/xrwvm-fullstack_developer_capstone/django_admin_users.png")
    render_admin_users_screenshot("/Users/airm2/Desktop/xrwvm-fullstack_developer_capstone/server/django_admin_users.png")
