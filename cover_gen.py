from PIL import Image, ImageDraw, ImageFont

width, height = 1920, 1080  # TODO: pass by flags
background_color = (255, 255, 255)
image = Image.new("RGB", (width, height), background_color)

logo_path = "logo.png"
logo = Image.open(logo_path)

background_for_logo = Image.new("RGBA", logo.size, (255, 255, 255, 255))
logo_with_background = Image.alpha_composite(background_for_logo, logo)
logo = logo_with_background

logo = logo.resize(
    (int(width / 3), int(width / 3 * logo.height / logo.width))
)  # resize logo to 1/3 of width
image.paste(
    logo, (int((width - logo.width) / 2), int((height - logo.height) / 2))
)  # center logo both horizontally and vertically

# Add text
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", 64)  # San Francisco font
text = "SGL Dev Sync - Sept 21, 2024"
text_width, text_height = draw.textbbox((0, 0), text, font=font)[2:]
text_y_position = height - (height / 4)
draw.text(((width - text_width) / 2, text_y_position), text, font=font, fill="black")

image.save("gen/video_cover_image.png")
