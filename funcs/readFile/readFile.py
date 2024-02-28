import re

VARIABLE_PATTERN = re.compile("^[A-Za-z][A-Za-z0-9]+$")


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
