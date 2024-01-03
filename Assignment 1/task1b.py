inp = open("input1b.txt","r")
out = open("output1b.txt", "w")

t = int(inp.readline())

for i in range(t):
    n = "\n" if i!=t-1 else ""
    c, num1, sign, num2 = inp.readline().split()
    if sign == '+':
      out.write(f"The result of {num1} {sign} {num2} is {int(num1) + int(num2)}{n}")
    elif sign == '-':
      out.write(f"The result of {num1} {sign} {num2} is {int(num1) - int(num2)}{n}")
    elif sign == '/':
      out.write(f"The result of {num1} {sign} {num2} is {int(num1) / int(num2)}{n}")
    elif sign == '*':
      out.write(f"The result of {num1} {sign} {num2} is {int(num1) * int(num2)}{n}")

inp.close()
out.close()
