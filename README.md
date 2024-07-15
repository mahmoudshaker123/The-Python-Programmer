# My Python Course

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/my_python_course.git
   cd my_python_course
   ```

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```
pip install -r requirements.txt
```

Running the Exercises
Navigate to the chapter you are working on:

```
cd chapters/chapter1
```
Edit the main.py file to write your solution or test your code.

Run the main.py file:

```bash
python main.py
```


Running the Tests
To run the tests for all chapters:

```bash
pytest
```

To run tests for a specific chapter:

```
pytest chapters/chapter1/tests/
```

### Summary

This setup provides a clear structure for students to follow, ensuring that they can write and test their code efficiently. The `pytest` framework will help verify the correctness of their solutions, providing instant feedback and facilitating a smooth learning experience.