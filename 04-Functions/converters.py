def cm_to_inch(n):
    return n/2.54

def feet_to_inch(n):
    inches = feet * 12 + inches
    return inches * 2.54

def inch_to_cm(n):
    return n*2.54

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place.
    print(f'20cm = {cm_to_inch(2)}cm')
    print(f'5 feet 6 inches = {feet_to_inch(5,6)}m')
    print(f'20inches = {inch_to_cm(20)}cm')
