def f(detector):
    current_count = 0
    max_count = 0
    i = 0
    
    while i < len(detector):
        if detector[i] == '+':
            current_count += 1
            max_count = max(max_count, current_count)
            i += 1
        elif detector[i] == '--':
            current_count -= 1
            i += 1
    
    return max_count >= 3

if __name__ == "__main__":
    print(f("+-+++-+---"))
    print(f("+-+-+-+-"))   
    print(f("+-++-+--"))    
    
    