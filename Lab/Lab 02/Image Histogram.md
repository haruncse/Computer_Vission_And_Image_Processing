**image histograms in Python**, using both **built-in library functions** and a **manual approach**.

---

## 🛠️ Built-in Method with OpenCV

```python
import cv2
import matplotlib.pyplot as plt

# Load image in grayscale
img = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot histogram
plt.plot(hist)
plt.title('Grayscale Histogram (OpenCV)')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
```

### 🔎 Key Functions:
- `cv2.imread()` loads the image.
- `cv2.calcHist()` computes the histogram.
- `plt.plot()` visualizes it.

---

## 🧮 Manual Method Using NumPy

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
img = cv2.imread('your_image.jpg', cv2.IMREAD_GRAYSCALE)

# Flatten the image into a 1D array
flat = img.flatten()

# Initialize histogram array
hist_manual = np.zeros(256, dtype=int)

# Count pixel intensities
for pixel in flat:
    hist_manual[pixel] += 1

# Plot manual histogram
plt.plot(hist_manual)
plt.title('Grayscale Histogram (Manual)')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
```

---

## ⚡️ Bonus: With Pillow

```python
from PIL import Image
import matplotlib.pyplot as plt

# Load and convert image to grayscale
img = Image.open('your_image.jpg').convert('L')

# Get histogram
hist = img.histogram()

# Plot it
plt.plot(hist)
plt.title('Grayscale Histogram (Pillow)')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')
plt.show()
```

---