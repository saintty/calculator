import re

VARIABLE_PATTERN = re.compile("^[A-Za-z][A-Za-z0-9]*$")
OPERATION_PATTERN = re.compile("^[+\-*/^()]$")
OPERATION_PRIORITY = {"+": 2, "-": 2, "(": 0, ")": 1, "*": 3, "/": 3, "^": 4}


class Token:
    variable = "Variable"
    number = "Operand"
    operation = "Operation"

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return "({}: {})".format(self.type, self.value)

    def __add__(self, other_token):
        return Token(Token.number, self.value + other_token.value)

    def __sub__(self, other_token):
        return Token(Token.number, self.value - other_token.value)

    def __pow__(self, other_token):
        return Token(Token.number, self.value ** other_token.value)

    def __mul__(self, other_token):
        return Token(Token.number, self.value * other_token.value)

    def __truediv__(self, other_token):
        return Token(Token.number, self.value / other_token.value)


def readFile(file_name):
    f = open(file_name, "r")
    vars = dict()
    while True:
        line = f.readline()
        if not line:
            break

        try:
            handle_line(line, vars)
        except Exception as e:
            error_file = open("error.txt", "w")
            error_file.write(str(e))
            return None

    f.close()

    return vars


def handle_line(line, vars):
    assign_position = line.find("=")

    if assign_position == -1:
        result_token = calculate(
            make_rpn(line.strip()), vars)
        result_file = open("result.txt", "w")
        result_file.write("Calculation result: {}".format(
            str(result_token.value)))
    elif line.rfind("=") != assign_position:
        raise Exception(
            "Error in variable definition: >=2 '=' symbols")
    else:
        variable_name = line[:assign_position].strip()
        if not re.match(VARIABLE_PATTERN, variable_name):
            raise Exception(
                "Error in variable definition: varName contains not allowed symbols")

        vars[variable_name] = calculate(
            make_rpn(line[assign_position + 1:].strip()), vars)


def make_tokens(line):
    num = ""
    var_name = ""
    is_negative = False

    tokens = []

    line = line.replace(" ", "")
    i = 0
    l = len(line)

    while i < l:
        char = line[i]

        if char.isalpha():
            var_name += char
            i += 1

        elif char.isdigit():
            if len(var_name):
                var_name += char
            else:
                num += char

            i += 1

        elif char == ".":
            if len(num) and num.find(".") == -1:
                i += 1
                num += char
            else:
                raise Exception("Syntax error: '.' in incorrect position")

        elif re.match(OPERATION_PATTERN, char):
            if (len(var_name)):
                tokens.append(Token(Token.variable, var_name))
                var_name = ""
            elif (len(num)):
                tokens.append(Token(Token.number, float(num)))
                num = ""

            tokens.append(Token(Token.operation, char))
            i += 1
        else:
            raise Exception("Unknown symbol")

    if len(var_name):
        tokens.append(Token(Token.variable, var_name))

    if len(num):
        tokens.append(Token(Token.number, float(num)))

    return tokens


def make_rpn(line):
    tokens = make_tokens(line)
    stack = []
    result_expression = []

    for token in tokens:
        if token.type == Token.number or token.type == Token.variable:
            result_expression.append(token)
        elif token.value == "(":
            stack.append(token)
        elif token.value == ")":
            while len(stack):
                top = stack.pop(-1)

                if top.value == "(":
                    break

                result_expression.append(top)

        else:
            if len(stack) == 0 or OPERATION_PRIORITY[stack[-1].value] < OPERATION_PRIORITY[token.value]:
                stack.append(token)
            else:
                while True:
                    if len(stack) and OPERATION_PRIORITY[stack[-1].value] >= OPERATION_PRIORITY[token.value]:
                        result_expression.append(stack.pop(-1))
                    else:
                        break
                stack.append(token)

    while len(stack):
        result_expression.append(stack.pop(-1))

    return result_expression


def get_operands(stack, n):
    operands = []

    try:
        for i in range(n):
            operands.append(stack.pop(-1))
        return operands
    except Exception:
        raise Exception("RNP Error: can`t get required operands")


def calculate(rpn, vars):
    stack = []
    for token in rpn:
        if token.type == Token.number:
            stack.append(token)
        elif token.type == Token.variable:
            if token.value not in vars:
                raise Exception(
                    "Syntax error: try to access undefined variable {}".format(token.value))
            else:
                stack.append(vars[token.value])
        else:
            if token.value == "+":
                a, b = get_operands(stack, 2)
                stack.append(a + b)
            elif token.value == "-":
                a, b = get_operands(stack, 2)
                stack.append(b - a)
            elif token.value == "*":
                a, b = get_operands(stack, 2)
                stack.append(a * b)
            elif token.value == "/":
                a, b = get_operands(stack, 2)
                stack.append(b / a)
            elif token.value == "^":
                a, b = get_operands(stack, 2)
                stack.append(b ** a)

    return stack[0]
