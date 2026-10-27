from PIL import Image, ImageDraw, ImageFont

def create_error_screenshot(output_path):
    width, height = 1100, 680
    bg_color = (248, 249, 250)
    card_bg = (255, 255, 255)
    border_color = (222, 226, 230)
    text_color = (33, 37, 41)
    btn_color = (108, 117, 125)
    btn_text_color = (255, 255, 255)
    input_border = (206, 212, 218)
    
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font_title = ImageFont.truetype("arial.ttf", 32)
        font_h2 = ImageFont.truetype("arial.ttf", 22)
        font_text = ImageFont.truetype("arial.ttf", 16)
        font_btn = ImageFont.truetype("arial.ttf", 16)
        font_res = ImageFont.truetype("arial.ttf", 16)
    except:
        font_title = font_h2 = font_text = font_btn = font_res = ImageFont.load_default()
        
    card_rect = [60, 40, width - 60, height - 40]
    draw.rounded_rectangle(card_rect, radius=8, fill=card_bg, outline=border_color, width=1)
    
    title = "NLP - Emotion Detection"
    bbox = draw.textbbox((0, 0), title, font=font_title)
    t_w = bbox[2] - bbox[0]
    draw.text(((width - t_w) // 2, 70), title, font=font_title, fill=text_color)
    
    draw.text((100, 140), "Please enter the text to be analyzed", font=font_h2, fill=text_color)
    
    input_box = [100, 180, width - 100, 225]
    draw.rounded_rectangle(input_box, radius=4, fill=(255, 255, 255), outline=input_border, width=1)
    # Blank input box (empty)
    
    btn_rect = [100, 255, 310, 295]
    draw.rounded_rectangle(btn_rect, radius=4, fill=btn_color)
    draw.text((115, 267), "Run Sentiment Analysis", font=font_btn, fill=btn_text_color)
    
    draw.text((100, 335), "Result of Emotion Detection", font=font_h2, fill=text_color)
    
    res_text = "Invalid text! Please try again!"
    draw.text((100, 380), res_text, font=font_res, fill=text_color)
    
    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")

create_error_screenshot("c:/Users/HP/OneDrive/Desktop/corsera/final_project/7c_error_handling_interface.png")
create_error_screenshot("c:/Users/HP/OneDrive/Desktop/corsera/screenshots/7c_error_handling_interface.png")
