To read and display an image in Python, along with showing its size and matrix representation, you can use libraries like `matplotlib`, `PIL` (Pillow), or `OpenCV`. Here's a complete example using both Pillow and Matplotlib:

---

### 🖼️ Using Pillow and Matplotlib

```python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
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
```

---

### 📌 Notes

- `img.size` returns a tuple `(width, height)`.
- `np.array(img)` converts the image into a matrix (NumPy array). For RGB images, the shape will be `(height, width, 3)`.
- If the image is grayscale, the shape will be `(height, width)`.

---

### 🧪 Optional: Using OpenCV (if you prefer)

```python
import cv2

# Read image using OpenCV
img = cv2.imread('your_image.jpg')  # BGR format
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB

# Display using matplotlib
plt.imshow(img_rgb)
plt.title("OpenCV Image")
plt.axis('off')
plt.show()

# Image size and matrix
print(f"Image Shape: {img.shape}")  # (height, width, channels)
print("Image Matrix:")
print(img_rgb)
```