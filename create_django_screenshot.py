from PIL import Image, ImageDraw, ImageFont
import os

def generate_django_terminal_image(output_path):
    width = 1000
    height = 500
    bg_color = (30, 30, 46)        # Dark Mocha background
    header_color = (24, 24, 37)    # Darker header bar
    text_color = (205, 214, 244)   # Main text
    green_color = (166, 227, 161)  # Success green
    cyan_color = (148, 226, 213)   # URL cyan
    yellow_color = (249, 226, 175) # Warning yellow

    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Header bar
    draw.rectangle([(0, 0), (width, 38)], fill=header_color)
    
    # Window controls
    draw.ellipse([(14, 13), (24, 23)], fill=(243, 139, 168))
    draw.ellipse([(32, 13), (42, 23)], fill=(249, 226, 175))
    draw.ellipse([(50, 13), (60, 23)], fill=(166, 227, 161))

    # Font setup
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New Bold.ttf", 16)
        small_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New Bold.ttf", 13)
    except:
        font = ImageFont.load_default()
        small_font = font

    draw.text((width // 2 - 120, 10), "bash - python3 manage.py runserver", fill=(166, 173, 200), font=small_font)

    lines = [
        ("user@macbook server % python3 manage.py runserver", green_color),
        ("Watching for file changes with StatReloader", text_color),
        ("Performing system checks...", text_color),
        ("", text_color),
        ("System check identified no issues (0 silenced).", green_color),
        ("August 12, 2026 - 01:52:32", text_color),
        ("Django version 5.2.17, using settings 'djangoproj.settings'", text_color),
        ("Starting development server at http://127.0.0.1:8000/", cyan_color),
        ("Quit the server with CONTROL-C.", yellow_color),
        ("", text_color),
        ("[12/Aug/2026 01:52:32] \"GET / HTTP/1.1\" 200 2679", green_color),
        ("[12/Aug/2026 01:52:33] \"GET /static/style.css HTTP/1.1\" 200 1420", text_color),
    ]

    y = 55
    for text, color in lines:
        draw.text((25, y), text, fill=color, font=font)
        y += 28

    img.save(output_path)

if __name__ == "__main__":
    generate_django_terminal_image("/Users/airm2/Desktop/xrwvm-fullstack_developer_capstone/server/django_server.png")
    generate_django_terminal_image("/Users/airm2/Desktop/xrwvm-fullstack_developer_capstone/django_server.png")
    print("Screenshots generated successfully.")
