import math
def calc(a, b, op):

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b

def MinAndMax(M, m, i, j, operators):

    mini = math.inf
    maxi = -math.inf
    for k in range(i, j):
        p = calc(M[i][k], M[k+1][j], operators[k])
        q = calc(M[i][k], m[k+1][j], operators[k])
        r = calc(m[i][k], M[k+1][j], operators[k])
        s = calc(m[i][k], m[k+1][j], operators[k])
        mini = min(mini, p, q, r, s)
        maxi = max(maxi, p, q, r, s)
    return mini, maxi

def get_maximum_value(operands, operators):

    n = len(operands)
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(M, m, i, j, operators)

    return M[0][n-1]


if __name__ == "__main__":
    expression = input()
    operators, operands = [], []

    for i in expression:
        if i in ['+', '-', '*']:
            operators.append(i)
        else:
            operands.append(int(i))

    print(get_maximum_value(operands, operators))
