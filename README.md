# Quiz App

## Overview

The Quiz App is a Python application that offers users an interactive quiz experience. The app presents questions, records answers, and provides instant feedback on correctness. It also features text-to-speech capabilities to enhance the user experience.

## Features

- Interactive multiple-choice quiz.
- Text-to-speech functionality for questions and choices.
- Progress tracking and instant feedback.
- User-friendly interface with "Next" and "Quit" buttons.
- Data loaded from a JSON file for flexibility.

## Getting Started

1. **Installation**:

   - Make sure you have Python installed on your system.
   - Clone this repository or download the source code file.
   - Install the required packages using `pip install gtts playsound`.

2. **Usage**:

   - Run the Python script to launch the quiz app.
   - Answer the questions by selecting options.
   - Click "Next" to move to the next question or "Quit" to exit the app.
   - Enjoy text-to-speech narration for questions and choices.

## Features Explained

- **Text-to-Speech**: The app utilizes the Google Text-to-Speech (gTTS) library to convert questions and answer choices into speech, enhancing the user experience.

- **User Feedback**: Instant feedback is provided based on the correctness of user-selected answers.

- **Data Flexibility**: Quiz questions, options, and answers are loaded from a JSON file, allowing for easy customization and expansion of the quiz content.

## Dependencies

This application relies on the following Python libraries and packages:

- `tkinter`: Used for creating the graphical user interface.
- `gtts`: Utilized for text-to-speech functionality.
- `playsound`: Used to play audio files.

Please ensure that you have these libraries and packages installed in your Python environment.

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script with the command `python quiz_app.py`.

## License

This project is open-source and available under the MIT License. Refer to the [LICENSE](LICENSE) file for complete details.

## Enjoy Learning!

Use the Quiz App to enhance your skills while having an interactive and engaging quiz experience. Start learning today!
