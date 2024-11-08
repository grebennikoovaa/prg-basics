sentence = input('Enter text: ')

def f(sentence):
    withoutspace = sentence.replace(" ", "")
    return withoutspace
print(f(sentence))
