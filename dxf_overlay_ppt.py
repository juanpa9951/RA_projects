from PIL import Image


# Open the base image

base_image = Image.open("my_plot.png")

# base_image.show()

# Open the image to be overlayed

overlay_image = Image.open("overlay.png")


# Define the position to overlay the image

x_position = 75

y_position = 420


# Paste the overlay image onto the base image

base_image.paste(overlay_image, (x_position, y_position), overlay_image)


# Save or display the resulting image

base_image.save("my_plot2.png")

base_image.show()