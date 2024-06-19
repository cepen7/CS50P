text = input("Expression: ")

x, y, z = text.split(" ", 2)
x = float(x)
z = float(z)

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        if z=="0": print("Not even you can devide by zero.")
        else: print(round(x / z, 1)

