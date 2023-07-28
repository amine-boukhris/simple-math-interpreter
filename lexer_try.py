import json

# let code the lexer
# having an expression like this: "5 + 3 - 1"

def lexer(expression: str) -> list:
    tokens = []

    for i in range(len(expression)):
        char = expression[i]
        
        if char == " ":
            continue
        elif char == '+' or char == '-':
            token = {
                "type": "OP",
                "value": char
            }
            tokens.append(token)
        elif char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            token = {
                "type": "INTEGER",
                "value": char
            }
            tokens.append(token)
        else:
            raise ValueError(f"Invalid character '{char}' at position {i}")

    # check for invalid tokens sequence
    for i in range(len(tokens)-1):
        if tokens[i]['type'] == tokens[i+1]['type']:
            wrong = tokens[i+1]['value']
            raise ValueError(f"Invalid expression: Unexpected Term '{wrong}'")

    return tokens

expression = "5 + 1 - 1"
try:
    tokens = lexer(expression)
    print(json.dumps(tokens, indent=4))
except ValueError as e:
    print(f"Error: {e}")