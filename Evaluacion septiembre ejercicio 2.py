import numpy as np
import matplotlib.pyplot as plt


imagen_negro = np.zeros((256, 256), dtype=np.uint8)


num_lineas = 20

for _ in range(num_lineas):
    
    x1, y1 = np.random.randint(0, 256, 2)
    x2, y2 = np.random.randint(0, 256, 2)
    
  
    num_points = max(abs(x2 - x1), abs(y2 - y1)) + 1
    x_p = np.linspace(x1, x2, num_points).astype(int)
    y_p = np.linspace(y1, y2, num_points).astype(int)
    
   
    for x, y in zip(x_p, y_p):
        if 0 <= x < 256 and 0 <= y < 256:
            imagen_negro[y, x] = 255

# Display the image
plt.figure(figsize=(8, 8))
plt.imshow(imagen_negro, cmap='gray', vmin=0, vmax=255)
plt.title('256×256 Black Image with 20 Random Lines')
plt.axis('off')
plt.show()