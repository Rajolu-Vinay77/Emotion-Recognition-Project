## Instructions to Run the Code

### Prerequisites
- Python 3.9 - 3.11
- Git

### 1. Clone the Repository
First, clone this repository to your local machine using the following command:
- https://github.com/Rajolu-Vinay77/Emotion-Recognition-Project.git

### 2. Create a Virtual Environment
It is highly recommended to create a virtual environment to manage the project's dependencies.
- For Windows
  - python -m venv venv
  - .\venv\Scripts\activate
 
- For macOS/Linux
  - python3 -m venv venv
  - source venv/bin/activate
    
### 3. Install Required Libraries
Install all the necessary Python packages using the **requirements.txt** file. This single command will handle all dependencies.
  - pip install -r requirements.txt

### 4. Run the Application
Execute the main script to start the webcam and begin emotion recognition.
  - python EmotionDetection.py

#### A window will appear showing your webcam feed. When a face is detected, a green box will be drawn around it with the predicted emotion and a confidence score. Press the 'q' key to close the application.
