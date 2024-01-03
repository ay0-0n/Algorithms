inp = open('input3_2.txt', 'r')
out = open('output3_2.txt', 'w')

n, k = map(int, inp.readline().split())
circle = {i: [i] for i in range(1, n + 1)}

def find_circle(person):
    return circle[person]

def merge_circles(circle_a, circle_b):
    if len(circle_a) < len(circle_b):
        circle_a, circle_b = circle_b, circle_a
    circle_a += circle_b
    for person in circle_b:
        circle[person] = circle_a
    return circle_a

for i in range(k):
    a, b = map(int, inp.readline().split())
    a_circle = find_circle(a)
    b_circle = find_circle(b)

    if a_circle != b_circle:
        new_circle = merge_circles(a_circle, b_circle)
        out.write(f"{len(new_circle)}\n")
    else:
        out.write(f"{len(a_circle)}\n")

inp.close()
out.close()