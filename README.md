# Udemy: Complete Python Course

This repository contains exercises and tests for the Udemy course [Complete Python Course]() by Shehab Abdel-Salam.

The course is divided into chapters, each containing exercises and tests. The exercises are designed to help students practice Python programming concepts, while the tests are used to verify the correctness of their solutions.

## 1. Structure
The repository has the following structure:
```
├── chapters/
│   ├── chapter1/
│   │   ├── exercises/
│   │   │   ├── exercise_ch1_01.py
│   │   │   ├── exercise_ch1_02.py
│   │   │   └── ...
│   │   └── tests/
│   │       └── test_ch01.py
│   ├── chapter2/
│   │   ├── exercises/
│   │   │   ├── exercise_ch2_01.py
│   │   │   ├── exercise_ch2_02.py
│   │   │   └── ...
│   │   └── tests/
│   │       └── test_ch02.py
│   └── ...
├── ninja_challenges/
│   ├── exercises/
│   │   ├── challenge_01.py
│   │   ├── challenge_02.py
│   │   └── ...
│   └── tests/
│       └── test_ninja_challenges.py
```

The `chapters` directory contains subdirectories for each chapter in the course. Each chapter directory contains an `exercises` directory for the exercises, a `tests` directory for the tests, and a `main.py` file for testing your code.

The `ninja_challenges` directory contains additional challenges for you to practice more once you complete the course. It also has an `exercises` directory for the challenges and a `tests` directory for the tests.

---

## 2. Getting Started
### 2.1 Prerequisites
Before you begin, ensure you have the following installed on your machine:
- Python **3.12** or higher
- `pip` package manager
- `pytest` testing framework

To check if you have Python installed, run the following command in your terminal:

```bash
python --version
```

To check if you have `pip` installed, run the following command in your terminal:

```bash
pip --version
```

To install **`pytest`**, run the following command in your terminal:

```bash
pip install pytest
```
---
### 2.2 Setup
First, make sure to clone the repository to your local machine using the following command:
```bash
git clone https://github.com/shehab-as/Udemy-Complete-Python.git
```

Afterwards, navigate to the repository directory:
```bash
cd Udemy-Complete-Python
```
---
### 2.3 Running the Exercises

1. Navigate to the chapter you are working on:

   ```bash
   cd chapters/chapter01_intro
   ```

2. Edit the main.py file to write your solution or test your code.

   ```bash
   python main.py
   ```

3. Run the test to verify the correctness of your solution.
   > Note: Always use the `-k` flag to run a specific test.

   ```bash
   pytest -k ch01_e01
   ```
   You should see the following output if the test passes:

   ```bash
   tests/test_ch_01.py .                                                                                [100%]

   =========================================== 1 passed in 0.01s =============================================
   ```

   **Optional: You can run all the tests for the chapter you are currently working on:**

   ```bash
   pytest tests/
   ```

4. If the test fails, you will see an error message indicating the reason for the failure. Fix the issue in your code and run the test again.

5. Repeat **steps 2-4** for each exercise in the chapter.

6. Once you have completed all the exercises in the chapter, you can move on to the next chapter and repeat the process.
   ```bash
   cd ../chapter02_variables
   ```

---
## 3. [Optional] Running the Ninja Challenges

1. Navigate to the ninja challenges directory:

   ```bash
   cd ninja_challenges/
   ```
2. Edit the main.py file to write your solution or test your code.

   ```bash
   python main.py
   ```
3. Run the test to verify the correctness of your solution.
   > Note: Always use the `-k` flag to run a specific test.

   ```bash
   pytest -k challenge_01
   ```

---
## 4. Contributing

If you have any questions or would like to report an issue, feel free to raise an issue on the repository.
Contributions are always welcome! If you would like to contribute, you can submit a pull request with your proposed changes and improvements and I'll make sure to review them as soon as possible.

Happy coding! 🐍
