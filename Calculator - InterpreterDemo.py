
# List of valid operations in calculator (both string names and symbols).
known_operators = ["add", "sub", "mul", "div", "power", "modolo", "+", "-", "*", "/", "^", "%"]


class Exp(object):
    """A call expression in Calculator."""

    def __init__(self, operator, operands):
        self.operator = operator  # Operator as a string (e.g., '+', 'mul')
        self.operands = operands  # List of operand expressions

    def __repr__(self):
        return "Exp({0},{1})".format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ", ".join(map(str, self.operands))
        return "{0}({1})".format(self.operator, operand_strs)

def calc_eval(exp):
    """Evaluate a Calculator expression."""
    if type(exp) in (int, float):  # Base case: direct number input
        return exp
    elif type(exp) == Exp:  # Recursive case: evaluate expression tree
        arguments = list(map(calc_eval, exp.operands))
    return calc_apply(exp.operator, arguments)

def calc_apply(operator, args):
    """Apply the named operator to a list of args."""
    if operator in ("add", "+"):
        return sum(args)   # Sum all arguments
    if operator in ("sub", "-"):
        if len(args) == 0:
            raise TypeError(operator + " requires at least 1 argument")
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])  # Subtract all but the first
    if operator in ("mul", "*"):
        return reduce(mul, args, 1)  # Multiply all arguments
    if operator in ("div", "/"):
        if len(args) != 2:
            raise TypeError(operator + " requires exactly 2 arguments")
        numer, denom = args
        return numer / denom  # Division of two numbers
    if (operator in ("modolo", "%")):
        if len(args) != 2:
            raise TypeError(operator + " requires exactly 2 arguments")
        numer, denom = args
        return numer % denom  # Modulo operation
    if operator in ("power", "^"):
        if len(args) != 2:
            raise TypeError(operator + " requires exactly 2 arguments")
        base, pow = args
        return base ** pow  # Exponentiation

def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            expression_tree = calc_parse(input("calc> "))  # Read input and parse
            print(calc_eval(expression_tree))  # Evaluate and print result
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ":", err)  # Handle errors
        except (KeyboardInterrupt, EOFError):  # <Control>-D
            print("Calculation completed.")
            return

def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)  # Convert input string into tokens
    expression_tree = analyze(tokens)  # Analyze tokens into an expression tree
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))  # Ensure no leftover tokens
    return expression_tree  # Return the parsed expression tree

def tokenize(line):
    """Convert a string into a list of tokens."""
    spaced = line.replace("(", " ( ").replace(")", " ) ").replace(",", " , ")  # Add spaces around delimiters
    return spaced.split()  # Split the string into individual tokens

def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens."""
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    else:
        tokens.pop(0)  # Remove (
        return Exp(token, analyze_operands(tokens))  # Create an expression node

def analyze_operands(tokens):
    """Read a list of comma-separated operands."""
    operands = []
    while tokens[0] != ')':  # Process tokens until closing parenthesis
        if operands:
            tokens.pop(0)  # Remove ,
        operands.append(analyze(tokens))   # Recursively analyze each operand
    tokens.pop(0)  # Remove )
    return operands

def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token."""
    try:
        return int(token)  # Try converting to an integer
    except (TypeError, ValueError):
        try:
            return float(token)  # Try converting to a float
        except (TypeError, ValueError):
            return token  # Return as is if not a number

def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens."""
    assert_non_empty(tokens)  # Ensure tokens are not empty
    token = analyze_token(tokens.pop(0))
    if isinstance(token, (int, float)):
        return token  # Return numbers as-is
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != "(":
            raise SyntaxError("expected ( after " + token)
        return Exp(token, analyze_operands(tokens))  # Create an expression
    else:
        raise SyntaxError("unexpected " + token)  # Invalid token

def analyze_operands(tokens):
    """Analyze a sequence of comma-separated operands."""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ")":
        if operands and tokens.pop(0) != ",":
            raise SyntaxError("expected ,")  # Expected comma between operands
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands

def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')

if __name__ == '__main__':
    read_eval_print_loop()
