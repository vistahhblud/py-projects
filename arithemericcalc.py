# basic functions only.

def m(a, b, s):
    if s == "+": return a + b
    if s == "-": return a - b
    if s == "*": return a * b
    if s == "/": return a / b

while True:
    try:
        x = input(">>> ")
        if x.lower() in ["q", "quit", "exit"]:
            break
        p = x.split()
        print(m(float(p[0]), float(p[2]), p[1]))
    except:
        print("enter number and calculation, example: 6 + 7")
