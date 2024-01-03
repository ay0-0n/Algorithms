inp = open("input1a.txt","r")
out = open("output1a.txt", "w")

t = int(inp.readline())

for i in range(t):
    n = "\n" if i!=t-1 else ""
    num = int(inp.readline())
    if num%2 == 0:
        out.write(f"{num} is an Even number{n}")
    else:
        out.write(f"{num} is a Odd number{n}")

inp.close()
out.close()