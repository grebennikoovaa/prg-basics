def card_value(card):
    if card in "AKQJT":
        return 10
    
def sum(hand):
    total = 0
    for card in hand:
        total += card_value(card)
        return total

def f(player1, player2):
    if sum(player1) >= sum(player2):
        return True
    
print(f("AJ972", "AQT72"))
print(f("9532", "K8"))