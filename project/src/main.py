import cv2
import numpy as np
from sudoku_solver.solver import SudokuSolver
from image_processing.grid_detector import GridDetector
from digit_recognition.recognizer import DigitRecognizer

def main():
    # Initialize components
    solver = SudokuSolver()
    grid_detector = GridDetector()
    digit_recognizer = DigitRecognizer()

    # Start video capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera")
        return

    print("Camera opened successfully. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame")
            break

        # Create a copy for visualization
        display = frame.copy()

        try:
            # Detect grid
            grid_contour, mask = grid_detector.find_grid(frame)
            corners = grid_detector.get_grid_corners(grid_contour)

            if corners is not None:
                # Draw grid outline
                cv2.drawContours(display, [grid_contour], -1, (0, 255, 0), 2)

                # Get perspective transform
                grid_size = 450
                dst_points = np.array([
                    [0, 0],
                    [grid_size, 0],
                    [grid_size, grid_size],
                    [0, grid_size]
                ], dtype="float32")

                matrix = cv2.getPerspectiveTransform(corners, dst_points)
                warped = cv2.warpPerspective(frame, matrix, (grid_size, grid_size))

                # Split into cells
                cells = np.zeros((9, 9, 50, 50, 3), dtype=np.uint8)
                cell_size = grid_size // 9
                for i in range(9):
                    for j in range(9):
                        cells[i, j] = cv2.resize(
                            warped[i*cell_size:(i+1)*cell_size,
                                  j*cell_size:(j+1)*cell_size],
                            (50, 50)
                        )

                # Recognize digits
                board = np.zeros((9, 9), dtype=np.int32)
                for i in range(9):
                    for j in range(9):
                        board[i, j] = digit_recognizer.recognize_digit(cells[i, j])

                # Solve sudoku
                if solver.solve(board):
                    # Draw solution on the frame
                    for i in range(9):
                        for j in range(9):
                            cell_center = np.mean([
                                corners[0],
                                corners[1],
                                corners[2],
                                corners[3]
                            ], axis=0).astype(int)
                            cv2.putText(display, str(board[i, j]),
                                      (cell_center[0]-10, cell_center[1]+10),
                                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        except Exception as e:
            print(f"Error processing frame: {e}")

        # Show the frame
        cv2.imshow('Sudoku Solver', display)

        # Break the loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()