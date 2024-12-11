expression = input("Expression: ").lower()
x, y, z = expression.split(" ")
match y:
    case "+":
        print(float(x) + float(z))
    case "*":
        print(float(x) * float(z))
    case "-":
        print(float(x) - float(z))
    case "/":
        print(float(x) / float(z))
