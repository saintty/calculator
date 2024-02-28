import re

VARIABLE_PATTERN = re.compile("^[A-Za-z][A-Za-z0-9]*$")
OPERATION_PATTERN = re.compile("^[+\-*/^()]$")


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
        print(make_tokens(line[assign_position + 1:].strip()))


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
                tokens.append(var_name)
                var_name = ""
            elif (len(num)):
                tokens.append(float(num))
                num = ""

            tokens.append(char)
            i += 1
        else:
            raise Exception("Unknown symbol")

    if len(var_name):
        tokens.append(var_name)

    if len(num):
        tokens.append(float(num))

    return tokens
