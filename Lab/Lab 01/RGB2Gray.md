To convert an RGB image to grayscale in Python, you can use either **Pillow**, **OpenCV**, or **NumPy**. Here's how to do it with each method:

---

### 🧱 1. **Using Pillow (PIL)**

```python
from PIL import Image
import matplotlib.pyplot as plt

# Load the image
img = Image.open('your_image.jpg')

# Convert to grayscale
gray_img = img.convert('L')

# Display the grayscale image
plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image (Pillow)")
plt.axis('off')
plt.show()
```

- `'L'` mode stands for **luminance**, which is an 8-bit grayscale.

---

### 🧪 2. **Using OpenCV**

```python
import cv2
import matplotlib.pyplot as plt

# Read the image in color (BGR)
img = cv2.imread('your_image.jpg')

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display using matplotlib
plt.imshow(gray_img, cmap='gray')
plt.title("Grayscale Image (OpenCV)")
plt.axis('off')
plt.show()
```

- OpenCV loads images in **BGR** format by default, so conversion is done using `cv2.COLOR_BGR2GRAY`.

---

### 🧮 3. **Using NumPy (Manual Conversion)**

```python
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load image and convert to NumPy array
img = Image.open('your_image.jpg')
img_np = np.array(img)

# Manual grayscale conversion using luminosity method
gray_np = 0.2989 * img_np[:, :, 0] + 0.5870 * img_np[:, :, 1] + 0.1140 * img_np[:, :, 2]

# Display grayscale image
plt.imshow(gray_np, cmap='gray')
plt.title("Grayscale Image (NumPy)")
plt.axis('off')
plt.show()
```

- This uses the standard formula:  
  **Gray = 0.2989 × R + 0.5870 × G + 0.1140 × B**

---
