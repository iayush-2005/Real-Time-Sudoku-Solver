
---

# 🧩 Real-Time Sudoku Solver  
*A Python application to solve Sudoku puzzles in real-time using OpenCV and Keras.*  

---

## ✨ Overview  
This project leverages computer vision and deep learning techniques to solve Sudoku puzzles efficiently in real-time. A **Greedy Best-First Search Algorithm** is used to solve puzzles, and the solutions are seamlessly overlaid onto the video feed.  

---

## 🔍 Features  

- **Real-Time Processing**: Captures Sudoku grids from live camera feeds or videos.  
- **Grid Preprocessing**: Uses OpenCV to preprocess the grid by removing noise and isolating the Sudoku matrix.  
- **AI-Driven Prediction**: Utilizes a pre-trained Keras model for number recognition.  
- **Efficient Solving**: Employs a Greedy Best-First Search Algorithm for optimized puzzle-solving.  
- **Real-Time Overlay**: Displays the computed solution over the original grid in the live feed.  

---

## 📸 Workflow & Output  

### Step-by-Step Process  

| **Step**                     | **Description**                  |              
|-------------------------------|-----------------------------------|
| **1. Input**                 | Captures Sudoku grid.            | 
| **2. Preprocessing**          | Converts to grayscale, applies thresholding, and removes noise. | 
| **3. Grid Detection**         | Extracts the Sudoku grid from the image. |  
| **4. Number Detection**       | Identifies numbers in the grid cells. |   
| **5. Prediction**             | Recognizes detected numbers.    |  
| **6. Overlay Solution**       | Displays solution on the grid.  |

---

## 🚀 Quick Start  

### Prerequisites  

Ensure the following are installed:  
- **Python** >= 3.7  
- **Required Libraries**: Install them with the command:  
  ```bash  
  pip install -r requirements.txt  
  ```  

### Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-repo-link  
   cd Real-Time-Sudoku-Solver  
   ```  

2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

### Usage  

1. Open the Jupyter notebook:  
   ```bash  
   jupyter notebook "Sudoku testing.ipynb"  
   ```  

2. Run all cells in the notebook.  

3. Position the Sudoku puzzle in front of your camera and see the solution overlaid in real-time!  

4. To stop the camera, press **`Q`**.  

---

## 📖 How It Works  

### **Step 1: Preprocessing**  
- Converts the input to grayscale and applies thresholding to isolate the Sudoku grid.  

### **Step 2: Grid Extraction**  
- Identifies the largest contour in the image, which corresponds to the Sudoku grid.  

### **Step 3: Number Detection**  
- Extracts numbers from individual grid cells using contour analysis.  

### **Step 4: Number Recognition**  
- Predicts the detected numbers using a pre-trained neural network in Keras.  

### **Step 5: Sudoku Solving**  
- Solves the Sudoku grid using a **Greedy Best-First Search Algorithm**, prioritizing cells with the fewest possible candidates.  

### **Step 6: Solution Overlay**  
- Aligns and overlays the solution directly onto the video feed.  

---

## 🧠 Algorithm  

### **Why Greedy Best-First Search?**  
- This approach optimizes the search process by solving cells with the least number of candidates first.  
- Reduces the overall time complexity compared to naive backtracking.  

For more details, refer to [Norvig’s Sudoku Solver](https://norvig.com/sudoku.html).  

---

## 📚 References  

- **Sudoku Solving Concepts**:  
  - [Norvig's Sudoku Solver](https://norvig.com/sudoku.html)  
  - [Medium - Sudoku Extraction from Images](https://medium.com/@neshpatel/solving-sudoku-part-ii-9a7019d196a2)  

- **Inspirations**:  
  - [Tech With Tim - Sudoku Solver](https://www.youtube.com/watch?v=lK4N8E6uNr4)  
  - [Taha Emara - Real-Time Sudoku Solver](https://github.com/tahaemara/real-time-sudoku-solver)  

---

## 🙌 Acknowledgements  

Special thanks to:  
- [Taha Emara](https://github.com/tahaemara/real-time-sudoku-solver) for inspiring this project.  
- The OpenCV and Keras communities for providing excellent tools.  

---

## 🛠 Future Work  

- **Enhance Number Recognition**: Use more robust models for increased accuracy.  
- **Broader Compatibility**: Extend the functionality for more complex Sudoku variations.  

---

