from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def id_generator(name, user_id, host_name, company, uploaded_photo, uploaded_qr):
    # Open images using PIL
    photo = Image.open(uploaded_photo).resize((100, 100))
    qr = Image.open(uploaded_qr).resize((100, 100))

    # Create an ID card image
    card_width, card_height = 330, 420
    id_card = Image.new("RGB", (card_width, card_height), "white")
    draw = ImageDraw.Draw(id_card)

    # Add border
    border_thickness = 5
    draw.rectangle([border_thickness, border_thickness, card_width-border_thickness, card_height-border_thickness], outline="black", width=border_thickness)


    # Calculate center positions for photo and QR
    photo_x = (card_width - photo.width) // 2
    qr_x = (card_width - qr.width) // 2

    # Paste images at the centered positions
    id_card.paste(photo, (photo_x, 20))
    id_card.paste(qr, (qr_x, 270))


    # Add text
    font = None
    try:
        font = ImageFont.truetype("arial.ttf", 12)
    except:
        font = ImageFont.load_default()

    text_width = draw.textbbox((0, 0), f"Name: {name}", font=font)[2]
    x_position = (card_width - text_width) // 2
    draw.text((x_position, 160), f"Name: {name}", fill="black", font=font)
    
    text_width = draw.textbbox((0, 0), f"User ID: {user_id}", font=font)[2] 
    x_position = (card_width - text_width) // 2  
    draw.text((x_position, 190), f"User ID: {user_id}", fill="black", font=font)

    text_width = draw.textbbox((0, 0), f"Company: {company}", font=font)[2]  
    x_position = (card_width - text_width) // 2 
    draw.text((x_position, 220), f"Company: {company}", fill="black", font=font)
    
    text_width = draw.textbbox((0, 0), f"Host: {host_name}", font=font)[2] 
    x_position = (card_width - text_width) // 2  
    draw.text((x_position, 250), f"Host: {host_name}", fill="black", font=font)
    text = "Scan QR for more info"
    text_width = draw.textbbox((0, 0), text, font=font)[2] 
    x_position = (card_width - text_width) // 2  

    draw.text((x_position, 380), text, fill="black", font=font)

    return id_card 
