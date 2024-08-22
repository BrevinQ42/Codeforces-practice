t = int(input())

for case in range(t):
    x_c, y_c, k = [int(i) for i in input().split()]
    
    offset = 1
    
    if k % 2 == 1:
        print(x_c, y_c)
        k -= 1
        
    for i in range(k):
        if i % 2 == 0:
            print(x_c + offset, y_c + offset)
        else:
            print(x_c - offset, y_c - offset)
            offset += 1