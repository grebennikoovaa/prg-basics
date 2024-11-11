def calculate(text, target_letter):
    count = 0 
    for char in text:
        if char == target_letter:
            count += 1
    return count