import cv2
import numpy as np

class GridDetector:
    @staticmethod
    def preprocess_image(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (9, 9), 0)
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 11, 2)
        return cv2.bitwise_not(thresh)

    def find_grid(self, img):
        processed = self.preprocess_image(img)
        contours, _ = cv2.findContours(processed, cv2.RETR_EXTERNAL,
                                     cv2.CHAIN_APPROX_SIMPLE)
        
        grid_contour = max(contours, key=cv2.contourArea)
        mask = np.zeros(img.shape[:2], np.uint8)
        cv2.drawContours(mask, [grid_contour], -1, (255, 255, 255), -1)
        
        return grid_contour, mask

    def get_grid_corners(self, contour):
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        
        if len(approx) == 4:
            corners = np.float32(approx.reshape(4, 2))
            return self.order_corners(corners)
        return None

    @staticmethod
    def order_corners(pts):
        rect = np.zeros((4, 2), dtype="float32")
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]
        
        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]
        return rect