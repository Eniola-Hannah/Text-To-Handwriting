from PIL import Image
import sys
import tkinter as tk
from tkinter import filedialog


def generate_image_from_text(text):
    try:
        # Load the background image
        BG = Image.open("font/bg.png")
        sheet_width = BG.width
        gap, ht = 0, 0

        # Iterate over each character in the input text
        for char in text:
            try:
                # Get the ASCII code of the character
                char_code = ord(char)
                
                # Load the corresponding character image
                char_image = Image.open(f"font/{char_code}.png")
                
                # Paste the character image onto the background image
                BG.paste(char_image, (gap, ht))
                
                # Update the coordinates for the next character
                size = char_image.width
                height = char_image.height
                gap += size

                # Check if the line needs to wrap
                if sheet_width < gap or len(char) * 115 > (sheet_width - gap):
                    gap, ht = 0, ht + 140

            except FileNotFoundError:
                print(f"Could not find an image for character '{char}' (code {char_code})")

        # Display the final composed image
        print("Total gap:", gap)
        print("Sheet width:", sheet_width)
        BG.show()

    except FileNotFoundError:
        print("Could not find the background image (bg.png)")