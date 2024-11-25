# Python-Quiz-App
# Quiz Application

This is a simple quiz application built using Python's `tkinter` library for the graphical user interface (GUI). The application presents the user with a series of questions, allows them to select answers, and provides feedback on whether the answers are correct or incorrect. At the end of the quiz, the user's score is displayed.

## Features
- Display multiple-choice questions.
- Check if the selected answer is correct or incorrect.
- Provide feedback using `tkinter.messagebox`.
- Track the user's score.
- Display the user's final score after completing all questions.

## Requirements

- Python 3.x
- Tkinter (Tkinter is included with Python, so you don't need to install it separately).

## Installation

1. Ensure you have Python 3.x installed on your machine.
2. Since `tkinter` is bundled with Python, you do not need to install it separately.
3. Download the Python script or clone this repository.
4. Run the script using the command:

    ```bash
    python quiz_app.py
    ```

## How to Use

1. Upon running the script, a GUI window will appear with a quiz question and multiple-choice options.
2. Select an answer by clicking one of the option buttons.
3. After selecting an answer, you will receive feedback on whether your answer is correct or incorrect through a pop-up message.
4. Click the "Next" button to proceed to the next question.
5. Once all the questions have been answered, the quiz will display your total score in a pop-up message and the application will close.

## Code Explanation

The application consists of the following key components:

- **QuizApp class**: This class manages the entire quiz. It initializes the questions, handles user interactions, and displays feedback.
- **UI Elements**:
  - `Label`: Displays the current question.
  - `Button`: Each button represents a multiple-choice option. When clicked, it checks if the answer is correct.
  - `Messagebox`: Provides feedback to the user about whether their answer was correct or incorrect.
  - `Next Button`: Allows the user to proceed to the next question after answering.

## Questions and Answers

The quiz is currently hardcoded with 3 questions, but you can easily modify or extend the question set:

### Example Questions:
1. **What is the capital of France?**
   - A) Berlin
   - B) Madrid
   - C) Paris (Correct)
   - D) Rome

2. **What is 5 + 3?**
   - A) 6
   - B) 7
   - C) 8 (Correct)
   - D) 9

3. **What color is the sky?**
   - A) Blue (Correct)
   - B) Green
   - C) Red
   - D) Yellow

### Example Screenshot
![Screenshot 2024-11-25 165831](https://github.com/user-attachments/assets/5e4c5096-ed1c-4462-a563-d20858a4dea8)

