def print_pattern(n):
    
    for x in range(n, 0, -1):  
        for y in range(x, 0, -1):  
            print(y, end=" ")  
        print() 

print_pattern(5)
