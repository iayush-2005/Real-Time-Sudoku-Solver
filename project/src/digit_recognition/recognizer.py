import cv2
import numpy as np
import pytesseract

class DigitRecognizer:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

    def process_cell(self, cell):
        # Preprocess the cell image
        gray = cv2.cvtColor(cell, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY_INV, 11, 2)
        
        # Find the largest contour (should be the digit)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                     cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return None
        
        digit_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(digit_contour)
        
        # If the contour is too small, ignore it
        if w * h < 100:
            return None
            
        # Extract the digit
        digit = thresh[y:y+h, x:x+w]
        
        # Pad and resize the digit
        pad = 10
        digit = cv2.copyMakeBorder(digit, pad, pad, pad, pad,
                                 cv2.BORDER_CONSTANT, value=0)
        digit = cv2.resize(digit, (28, 28))
        
        return digit

    def recognize_digit(self, cell):
        processed_cell = self.process_cell(cell)
        if processed_cell is None:
            return 0
            
        # Configure tesseract for digits only
        config = '--psm 10 --oem 3 -c tessedit_char_whitelist=123456789'
        try:
            digit = pytesseract.image_to_string(processed_cell,
                                              config=config).strip()
            return int(digit) if digit.isdigit() else 0
        except:
            return 0