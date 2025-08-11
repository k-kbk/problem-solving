import sys

H, W = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())


def can_place(H, W, a1, b1, a2, b2):
    return (max(b1, b2) <= H and a1 + a2 <= W) or (max(a1, a2) <= W and b1 + b2 <= H)


for w1, h1 in [(x1, y1), (y1, x1)]:
    for w2, h2 in [(x2, y2), (y2, x2)]:
        if can_place(H, W, w1, h1, w2, h2) or can_place(W, H, w1, h1, w2, h2):
            print("YES")
            sys.exit(0)
else:
    print("NO")
