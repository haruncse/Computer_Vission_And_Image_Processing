# import sys
# print(sys.executable)

# import os
# print(os.environ.get('VIRTUAL_ENV'))

from PIL import Image

img = Image.new('RGB', (150, 150), color='green')
img.save('check_venv_image.png')
print("Image created successfully inside the virtual environment!")

