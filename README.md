# Calculator Interpreter

A simple interpreter for a calculator, developed in Python as part of the *Principles of Programming Languages* course. This project parses mathematical expressions, builds an expression tree, and evaluates operations dynamically.

## Features
- Supports basic arithmetic operations: addition, subtraction, multiplication, division, exponentiation, and modulo.
- Parses expressions using a recursive descent approach.
- Handles both symbolic (`+`, `-`, `*`, `/`, `^`, `%`) and named (`add`, `sub`, `mul`, `div`, `power`, `modolo`) operators.
- Implements error handling for syntax errors, division by zero, and incorrect input.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/shulamitmorjossef/Calculator-InterpeterDemo.git
   cd calculator-interpreter
   ```
2. Ensure you have Python installed (version 3.x recommended).

## Usage
Run the interpreter with:
```sh
python calculator.py
```
Then, enter expressions in the following format:
```
calc> add(2, 3)
5
calc> power(4, 2)
16
calc> div(10, 2)
5.0
```
To exit, use `Ctrl+D` or `Ctrl+C`.

## Example Expressions
```sh
calc> add(10, mul(2, 3))  # 10 + (2 * 3)
16
calc> sub(20, 5, 3)       # 20 - 5 - 3
12
calc> div(8, 0)           # Error handling
ZeroDivisionError: division by zero
```

## Future Improvements
- Extend support for additional mathematical functions.
- Add support for variables and assignment.
- Implement a GUI version for easier interaction.

## Contributing
Pull requests are welcome! If you’d like to contribute, feel free to fork the repository and submit a PR.

