import utime

# 100000 in 38s (32s in C)
def display(i):
    tick = utime.ticks_ms()
    print(f"{int((tick - start)/1000)}s: {i}")
    
print("Prime number calculation")
start = utime.ticks_ms()
i = 2
display(2)
i += 1
while True:
    is_prime = True
    for div in range(2, int(i ** 0.5) + 1):
        if i % div == 0:
            is_prime = False
            break
    if is_prime:
        display(i)
    i += 2
        
