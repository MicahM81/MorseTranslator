# 🔡 Morse Code Translator (Python)

A simple Python command-line application that converts plain text into **Morse code** (and can be easily extended to decode Morse back to text).  
Perfect for beginners learning about **Python dictionaries**, **string manipulation**, and **modular programming**.

---

## 🚀 Features

- Converts letters (A–Z), numbers (0–9), and punctuation into Morse code  
- Uses a clean dictionary-based lookup (`morse_code_dict.py`)  
- Supports word separation using `/`  
- Easily extendable to add decoding or a GUI  

---

## 🧩 Project Structure

MorseTranslator/
│
├── main.py # Main script for user input and conversion
├── morse_code_dict.py # Morse code dictionary module
├── .gitignore # Git ignore rules
└── README.md # Project documentation

yaml
Copy code

---

## 🧠 Example Usage

### Run the program

```bash
python main.py
Sample Input & Output
css
Copy code
Enter text to convert to Morse code: Hello, world!
.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--
🧰 Requirements
Python 3.8+

No external libraries required

(Optional) If you want to create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
🧱 How It Works
The morse_code_dict.py file defines a Python dictionary with mappings from each character to its Morse code equivalent.

The main.py script:

Imports the dictionary

Takes user input

Uses a list comprehension to translate each character to Morse

Joins and prints the Morse code output

💡 Future Enhancements
🔁 Add a reverse translator (Morse → Text)

💻 Create a simple GUI using tkinter

🌐 Build a Flask web version

🧪 Add unit tests with pytest

🧑‍💻 Author
Micah Moffett
📫 GitHub • LinkedIn

🪪 License
This project is licensed under the MIT License — see the LICENSE file for details.

⭐ If you found this project helpful, give it a star on GitHub!
