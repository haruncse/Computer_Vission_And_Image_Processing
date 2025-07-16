---

## 🧪 Lab Task: Introduction to Image Processing with OpenCV

### 🎯 Objectives
- Understand image structure and pixel operations
- Learn to read, display, and modify images using OpenCV
- Apply basic filters and transformations

---

### 🔧 Setup Instructions
Before starting:
```bash
pip install opencv-python matplotlib
```

---

### 📚 Task Breakdown

#### 1️⃣ Load and Display an Image
- Load any image (`.jpg`, `.png`) using OpenCV
- Display it using both OpenCV and `matplotlib`

```python
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
cv2.imshow('Original Image', img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Image via matplotlib')
plt.show()
```

---

#### 2️⃣ Convert to Grayscale
- Apply grayscale conversion
- Display and save the result

```python
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.jpg', gray_img)
```

---

#### 3️⃣ Apply Basic Filters
- Perform **Gaussian Blur**, **Edge Detection (Canny)**

```python
blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)
edges = cv2.Canny(gray_img, 50, 150)
```

---

#### 4️⃣ Resize and Crop
- Resize image to half its original dimensions
- Crop the top-left 100x100 pixels

```python
resized = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
cropped = img[0:100, 0:100]
```

---

#### 5️⃣ Bonus Challenge 💡
- Convert grayscale image to **binary threshold**
- Detect and draw contours

```python
_, thresh = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
```

---

### 📊 Evaluation Criteria
| Task                  | Points |
|----------------------|--------|
| Image loading & display | 10     |
| Grayscale & save       | 10     |
| Filtering (blur + edges) | 20     |
| Resize & crop          | 20     |
| Bonus challenge        | 40     |

---

