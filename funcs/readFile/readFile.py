import re

VARIABLE_PATTERN = re.compile("^[A-Za-z][A-Za-z0-9]*$")
OPERATION_PATTERN = re.compile("^[+\-*/^()]$")
OPERATION_PRIORITY = {"+": 2, "-": 2, "(": 0, ")": 1, "*": 3, "/": 3, "^": 4}


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        type = "Operand" if self.type == "operand" else "Operation"
        return "({}: {})".format(type, self.value)


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
            print(e)
            return None

    f.close()

    return vars


def handle_line(line, vars):
    assign_position = line.find("=")

    if assign_position == -1:
        # TODO: final expression calculation
        pass
    elif line.rfind("=") != assign_position:
        raise Exception(
            "Error in variable definition: >=2 '=' symbols")
    else:
        variable_name = line[:assign_position].strip()
        if not re.match(VARIABLE_PATTERN, variable_name):
            raise Exception(
                "Error in variable definition: varName contains not allowed symbols")

        vars[variable_name] = 0
        ops = calculate(line[assign_position + 1:].strip(), vars)


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
                tokens.append(Token("operand", var_name))
                var_name = ""
            elif (len(num)):
                tokens.append(Token("operand", float(num)))
                num = ""

            tokens.append(Token("operation", char))
            i += 1
        else:
            raise Exception("Unknown symbol")

    if len(var_name):
        tokens.append(Token("operand", var_name))

    if len(num):
        tokens.append(Token("operand", float(num)))

    return tokens


def calculate(line, vars):
    tokens = make_tokens(line)
    stack = []
    result_expression = []

    for token in tokens:
        if token.type == "operand":
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
