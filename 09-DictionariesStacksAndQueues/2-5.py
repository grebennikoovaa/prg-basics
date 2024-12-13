import json

with open('reservations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

    def num_of_rooms(data):
        reservation = data['reservations']
        room_numbers = set()
        for item in reservation:
            for key, value in item.items():
                if key == "room_number":
                   room_numbers.add(value)
        return len(room_numbers) 
    
    def paid_reservations(data):
        reservation = data['reservations']
        paid_reservations = 0
        for item in reservation:
            if item.get('paid') == True:
                    paid_reservations += 1
        return (paid_reservations)
    
    def unpaid_reservations(data):
        reservation = data['reservations']
        unpaid_reservations = 0
        for item in reservation:
            if item.get('paid') != True:
                    unpaid_reservations += 1
        return (unpaid_reservations)

        
    print(num_of_rooms(data))
    print(paid_reservations(data))
    print(unpaid_reservations(data))
