from rational import Rational

def parse_token(token):
    token = token.strip()
    if '/' in token:
        return Rational(token)
    else:
        return Rational(int(token))

def evaluate_expression(expr):
    tokens = expr.replace('*', ' * ').replace('-', ' - ').replace('+', ' + ').replace('/', ' / ').split()
    if not tokens:
        return None

    current = parse_token(tokens[0])

    i = 1
    while i < len(tokens):
        op = tokens[i]
        next_token = parse_token(tokens[i + 1])

        if op == '+':
            current = current + next_token
        elif op == '-':
            current = current - next_token
        elif op == '*':
            current = current * next_token
        elif op == '/':
            current = current / next_token
        else:
            raise ValueError(f"Невідомий оператор: {op}")

        i += 2

    return current

def main():
    input_file = 'inputs/input01.txt'
    output_file = 'outputs/output.txt'

    results = []

    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        if line:
            try:
                result = evaluate_expression(line)
                results.append(f"{result} = {result()}")
            except Exception as e:
                results.append(f"Помилка у виразі '{line}': {e}")

    with open(output_file, 'w') as f:
        for res in results:
            f.write(res + '\n')

if __name__ == "__main__":
    main()
