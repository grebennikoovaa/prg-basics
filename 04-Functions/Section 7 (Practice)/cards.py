def hide(card_number):
    first_let = card_number[0:2]
    last_let = card_number[12:16]
    hidden = f"{first_let}**********{last_let}"
    return hidden