import re


from TokenClass.Token import Token
from fractionalClass.RationalFraction import RationalFraction
from VectorClass.Vector import Vector

VARIABLE_PATTERN = re.compile("^[A-Za-z][A-Za-z0-9]*$")
OPERATION_PATTERN = re.compile("^[+\-*/^()]$")
OPERATION_PRIORITY = {"+": 2, "-": 2,
                      "(": 0, ")": 1, "*": 3, "/": 3, "^": 4, "-u": 5}


def readFile(file_name):
    f = open(file_name, "r")
    vars = dict()
    line_number = 1

    while True:
        line = f.readline()
        if not line:
            break

        try:
            handle_line(line, vars)
            line_number += 1
        except Exception as e:
            error_file = open("error.txt", "w")
            error_file.write("line {}:  ".format(line_number) + str(e))
            return None

    f.close()
    return vars


def handle_line(line, vars):
    assign_position = line.find("=")

    if assign_position == -1:
        result = calculate(
            make_rpn(line.strip()), vars)
        result_file = open("result.txt", "w")
        result_file.write("Calculation result: {}".format(
            str(result)))
    elif line.rfind("=") != assign_position:
        raise Exception(
            "Error in variable definition: >=2 '=' symbols")
    else:
        variable_name = line[:assign_position].strip()
        if not re.match(VARIABLE_PATTERN, variable_name):
            raise Exception(
                "Error in variable definition: varName contains not allowed symbols")

        vars[variable_name] = calculate(
            make_rpn(line[assign_position + 1:].strip()), vars).value


def check_vector_syntax(is_inside_vector, current_char):
    if is_inside_vector and not (current_char.isdigit() or current_char.isalpha() or current_char == "}" or current_char == "," or current_char == "-"):
        raise Exception("Unknown symbol '{}' in vector definition".format(
            current_char))


def make_tokens(line):
    num = ""
    var_name = ""
    is_negative = False
    is_vector = False
    vector = []

    tokens = []

    line = line.replace(" ", "")
    i = 0
    l = len(line)

    while i < l:
        char = line[i]

        check_vector_syntax(is_inside_vector=is_vector, current_char=char)

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

        elif char == "-":
            if is_vector:
                vector.append(Token(Token.unary_operation, "-u"))
            elif i == 0 or re.match(OPERATION_PATTERN, line[i - 1]):
                is_negative = True

            else:
                if (len(var_name)):
                    tokens.append(Token(Token.variable, var_name))
                    var_name = ""
                elif (len(num)):
                    tokens.append(Token(Token.number, RationalFraction(num)))
                    num = ""
                tokens.append(Token(Token.operation, char))

            i += 1

        elif re.match(OPERATION_PATTERN, char):
            if (len(var_name)):
                tokens.append(Token(Token.variable, var_name))
                var_name = ""
            elif (len(num)):
                tokens.append(Token(Token.number, RationalFraction(num)))
                num = ""

            if is_negative:
                is_negative = False
                tokens.append(Token(Token.unary_operation, "-u"))
            tokens.append(Token(Token.operation, char))
            i += 1

        elif char == "{":
            if is_vector:
                raise Exception("Nested vector not supported")

            is_vector = True
            i += 1

        elif char == "}":
            if not is_vector:
                raise Exception("Incorrect vector syntax - } symbol before {")

            if (len(var_name)):
                vector.append(Token(Token.variable, var_name))
                var_name = ""
            elif len(num):
                vector.append(Token(Token.number, RationalFraction(num)))
                num = ""

            tokens.append(Token(Token.vector, vector))
            is_vector = False
            vector = []
            i += 1

        elif char == ",":
            if not is_vector:
                raise Exception(
                    "Unknown symbol '{}' in vector definition".format(char))

            if (len(var_name)):
                vector.append(Token(Token.variable, var_name))
                var_name = ""
            elif len(num):
                vector.append(Token(Token.number, RationalFraction(num)))
                num = ""

            i += 1

        else:
            raise Exception("Unknown symbol")

    if len(var_name):
        tokens.append(Token(Token.variable, var_name))

    if len(num):
        tokens.append(Token(Token.number, RationalFraction(num)))

    if is_negative:
        is_negative = False
        tokens.append(Token(Token.unary_operation, "-u"))

    return tokens


def make_rpn(line):
    tokens = make_tokens(line)
    stack = []
    result_expression = []

    for token in tokens:
        if token.type == Token.number or token.type == Token.variable or token.type == Token.vector:
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


def prepared_vector(vector, vars):
    result = []
    is_negative = False
    for token in vector:
        if (token.type == Token.unary_operation):
            is_negative = True
        elif token.type == Token.number:
            if is_negative:
                result.append(token.value * RationalFraction("-1"))
            else:
                result.append(token.value)

            is_negative = False
        elif token.type == Token.variable:
            if not token.value in vars:
                raise Exception(
                    "Syntax error: try to access undefined variable {} inside vector".format(token.value))

            variable_value = vars[token.value]
            if isinstance(variable_value, Vector):
                raise Exception("Nested vector not supported")

            if is_negative:
                result.append(variable_value * RationalFraction("-1"))
            else:
                result.append(variable_value)

            is_negative = False

    if is_negative:
        raise Exception(
            "Can`t apply unary minus operation inside vector definition")

    return Vector(result)


def calculate(rpn, vars):
    stack = []
    for token in rpn:
        if token.type == Token.number:
            stack.append(token)
        elif token.type == Token.vector:
            stack.append(
                Token(Token.vector, prepared_vector(token.value, vars)))
        elif token.type == Token.variable:
            if token.value not in vars:
                raise Exception(
                    "Syntax error: try to access undefined variable {}".format(token.value))
            else:
                stack.append(vars[token.value])
        elif token.type == Token.unary_operation:
            if token.value == "-u":
                a = get_operands(stack, 1)[0]
                stack.append(a * Token(Token.number, RationalFraction("-1")))
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
