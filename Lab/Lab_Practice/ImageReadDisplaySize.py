from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image_path = 'image1_lena.jpg'  # Replace with your image path
img = Image.open(image_path)

# Display the image
plt.imshow(img)
plt.title("Displayed Image")
plt.axis('off')  # Hide axes
plt.show()

# Get image size
width, height = img.size
print(f"Image Size: {width} x {height} (Width x Height)")

# Convert image to NumPy array (matrix)
img_matrix = np.array(img)
print("Image Matrix:")
print(img_matrix)
print(f"Matrix Shape: {img_matrix.shape}")