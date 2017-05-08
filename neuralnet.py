w1 = float(input("weight 1 (w1):"))
w2 = float(input("weight 2 (w2):"))
b = float(input("bias (b):"))
a = float(input("learning rate (a):"))
print("activation: threshold")
print()
while True:
    x1 = float(input("value 1 (x1):"))
    x2 = float(input("value 2 (x2):"))
    d = float(input("desired output (d):"))
    net = w1 * x1 + w2 * x2 + b
    if net >= 0:
        y = 1
    else:
        y = 0
    print("net =",round(net,3))
    print("output =",round(y,3))
    w1 = w1 + a * (d - y) * x1
    w2 = w2 + a * (d - y) * x2
    b = b + a * (d - y)
    print("new weight 1 (w1):",round(w1,3))
    print("new weight 2 (w2):",round(w2,3))
    print("new bias (b):",round(b,3))
    print()
