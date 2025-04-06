import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

def draw_text(draw, text, position, font, max_width):
    """Draw text on an image, wrapping if it's too long."""
    lines = []
    words = text.split(' ')
    current_line = ''

    for word in words:
        # Check if adding the next word would exceed the width
        test_line = f"{current_line} {word}".strip()
        width = draw.textlength(test_line, font=font)
        
        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)  # Add the last line
    return lines

def create_character_card(id, name, story, image_path, output_path):
    # Load a font that supports Chinese characters
    font_path = "font.ttf"  # Change this to your font path
    font = ImageFont.truetype(font_path, 20)
    
    # Create a blank image with dynamic height
    card_width = 400
    max_text_width = card_width - 170
    lines = draw_text(ImageDraw.Draw(Image.new('RGB', (1, 1))), f"Story: {story}", (0, 0), font, max_text_width)
    
    text_height = len(lines) * 25  # Adjust line spacing
    card_height = max(200 + text_height, 300)  # Ensure minimum height
    card = Image.new('RGB', (card_width, card_height), 'white')
    draw = ImageDraw.Draw(card)
    
    # Load the character image
    try:
        character_image = Image.open(image_path).resize((100, 100))  # Resize to fit
        card.paste(character_image, (20, 20))
    except FileNotFoundError:
        print(f"Image not found for ID {id}: {image_path}")
    
    # Draw name on the card
    draw.text((150, 30), f"Name: {name}", fill="black", font=font)
    
    # Draw story with automatic line breaks
    y_text = 70
    for line in lines:
        draw.text((150, y_text), line, font=font, fill="black")
        y_text += 25
    
    # Save the card
    card.save(output_path)

def generate_character_cards(csv_file, images_folder, output_folder):
    # Read the CSV file
    characters = pd.read_csv(csv_file)

    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Generate cards for each character
    for index, row in characters.iterrows():
        id = row['ID']
        name = row['Name']
        story = row['Story']
        image_path = os.path.join(images_folder, f"{id:03}.jpg")  # Format ID with leading zeros
        output_path = os.path.join(output_folder, f"character_card_{id:03}.jpg")

        create_character_card(id, name, story, image_path, output_path)

# Example usage
generate_character_cards('data.csv', 'images', 'output')
