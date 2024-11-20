# Real-time Sudoku Solver

This application uses your computer's camera to detect, solve, and overlay solutions onto Sudoku puzzles in real-time.

## Pre Requisites

- Python 3.8 or higher
- OpenCV
- Tesseract OCR
- NumPy

## Installation

1. Install Tesseract OCR on Ubuntu:
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Open the project in PyCharm
2. Make sure your virtual environment is selected
3. Run `src/main.py`
4. Point your camera at a Sudoku puzzle
5. Press 'q' to quit the application

## Project Structure

```
sudoku-solver/
├── requirements.txt
├── README.md
└── src/
    ├── main.py
    ├── sudoku_solver/
    │   └── solver.py
    ├── image_processing/
    │   └── grid_detector.py
    └── digit_recognition/
        └── recognizer.py
```