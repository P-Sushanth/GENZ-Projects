import cv2
import numpy as np

# Load the image
image_path = r"C:\Users\Admin\Documents\Projects\GENZ-Projects\images\homepage\logo.webp"
img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

alpha_channel = img[:, :, 3]
_, thresh = cv2.threshold(alpha_channel, 1, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

main_path_str = ""
window_path_str = ""

for i, cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    x,y,w,h = cv2.boundingRect(cnt)
    
    approx = cnt
    
    if len(approx) > 2:
        path = f"M {approx[0][0][0]} {approx[0][0][1]} "
        for j in range(1, len(approx)):
            path += f"L {approx[j][0][0]} {approx[j][0][1]} "
        path += "Z "
        
        # Windows: small squares in the middle. Let's find them by size and shape (square-ish).
        # We can just print and test. The image is 1717x1236.
        # Let's say windows have area < 10000 but > 100, and w, h < 100
        aspect = float(w)/h if h > 0 else 0
        if 1900 < area < 2100 and w < 60 and h < 60:
            print(f"Possible window: idx {i}, area {area}, w {w}, h {h}, aspect {aspect}")
            window_path_str += path
        else:
            main_path_str += path

svg_path = r"C:\Users\Admin\Documents\Projects\GENZ-Projects\images\homepage\logo.svg"
color = "#FFD700"
window_color = "#FFFFFF"

with open(svg_path, "w") as f:
    f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {img.shape[1]} {img.shape[0]}">\n')
    f.write(f'<path d="{main_path_str}" fill="{color}" fill-rule="evenodd" />\n')
    f.write(f'<path d="{window_path_str}" fill="{window_color}" fill-rule="evenodd" />\n')
    f.write('</svg>\n')

print(f"SVG written to {svg_path}")
