from PIL import Image
import tkinter as tk
from tkinter import filedialog
from customtkinter import *


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


def on_generate_button_click():
    # Get the text from the entry widget
    input_text = text_entry.get()

    # Generate the image based on the input text
    generate_image_from_text(input_text)


# Create the main tkinter window
# root = tk.Tk()
root = CTk()
root.geometry("500x400")
root.title("GROUP 4 - TEXT TO HAND-WRITING FORMAT")
set_appearance_mode("light")


# # Label and entry widget for entering text
CTkLabel(root, text="Enter Text:", font=("Arial", 20)).pack(pady=10)
text_entry = CTkEntry(root, width=300) 
text_entry.pack(pady=20)


# Button to trigger image generation
generate_button = CTkButton(root, text="Convert Text", corner_radius=32, fg_color="#C850C0", hover_color="#4158D0", command=on_generate_button_click)
generate_button.pack()


# Run the main event loop
root.mainloop()