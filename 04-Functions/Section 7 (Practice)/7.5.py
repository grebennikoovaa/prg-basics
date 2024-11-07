import cards

card_number = input("Enter card number (16 digits) : ")
if len(card_number) != 16:
    print("Incorrect card number :(")

hiden_card = cards.hide(card_number)
print(hiden_card)