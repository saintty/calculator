# Calculator

## Time tracking

Were used [Figma](https://www.figma.com/file/cmUH30Y4Zhis0PUVC71bnT/Калькулятор?type=whiteboard&node-id=0-1&t=eBH8VO31vn6vHyvn-0) application

## How to run

- install python
- install pypinstaller
- `pyinstaller main.py`
- `cd dist/main`
- run executable file with expression.txt file on input

## Supported operations

- Variable definition
  - `variable1Name2 = -1.15`
  - `variable1Name2 = {1, -2.15}`
  - `variable1Name2 = 2 * 3 - (1 - {1, 2} * {2, -1})`
- Math operation:
  - \+ (addition)
    - `-1.2 + 3.2 = 2/1`
    - `1 + {1, 2} = 2/1 3/1`
    - `{3, 4} + -1.2 = 9/5 14/5`
    - `{0, 0} + {1, 2} = 1/1 2/1`
  - \- (subtraction)
    - `-1.2 - 3.2 = 22/5`
    - `1 - {1, 2}` **Invalid operation**
    - `{3, 4} - -1.2 = 21/5 26/5`
    - `{0, 0} - {1, 2} = -1/1 -2/1`
  - \* (multiplication)
    - `-1.2 * 3.2 = -96/25`
    - `1 * {1, 2} = 1/1 2/1`
    - `{3, 4} \* -1.2 = -18/5 -24/5`
    - `{0, 0} \* {1, 2} = 0/1`
  - / (division)
    - `-1.2 / 3.2 = -3/8`
    - `1 / {1, 2}` **Invalid operation**
    - `{3, 4} / -1.2 = 5/-2 10/-3`
    - `{0, 0} / {1, 2} = 0/1`
  - ^ (exponentiation)
    - `1.5 ^ 2 = 9/4`
    - `1 ^ {1, 2}` **Invalid operation**
    - `{3, 4} ^ -1.2` **Invalid operation**
    - `{0, 0} ^ {1, 2}` **Invalid operation**
  - brackets ( )
    - `(2 + 3) \* 4 = 20/1`

All operations are allowed to use with variables names instead of numbers/vectors literals

## Input files

- `result.txt` display calculation result of last line in expression.txt file. Last line mustn't include = symbol
- `error.txt` display first error occurred during work
