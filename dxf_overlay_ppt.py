from PIL import Image


# Open the base image

base_image = Image.open("Layers.png")
#base_image.show()

###................X AXIS OVERLAY....................
# Open the image to be overlayed
overlay_image = Image.open("overlay_x.PNG")
# Define the position to overlay the image
x_position = 142    # 142
y_position = 1050   #  1050
# Paste the overlay image onto the base image
base_image.paste(overlay_image, (x_position, y_position), overlay_image)
# Save or display the resulting image
base_image.save("new_axis_image.png")

###................Y AXIS OVERLAY....................
overlay_image = Image.open("overlay_y.PNG")
# Define the position to overlay the image
x_position = 99     # 99
y_position = 133    # 133
# Paste the overlay image onto the base image
base_image.paste(overlay_image, (x_position, y_position), overlay_image)
# Save or display the resulting image
base_image.save("new_axis_image.png")


base_image.show()