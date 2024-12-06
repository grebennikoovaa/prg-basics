word = input('Enter a word in English: ')

translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
if word in translations:
    result = translations[word]
else :
    result = False

print(result)