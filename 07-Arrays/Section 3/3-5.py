# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   sum = 0
   for row in cinema_seats : 
      for item in row : 
        sum += 1
   return sum

def seats_available(seats):
   available = 0
   for row in cinema_seats:
      for item in row:
         if item == 'A':
            available += 1
   return available

def seats_booked(seats):
   booked = 0
   for row in cinema_seats:
      for item in row:
         if item == 'B':
            booked += 1
   return booked

def seat_status(seats, row, place):
   row -= 1 
   place -= 1 
   if cinema_seats[row][place] == "A" : 
       result = "Available"
   else : 
       result = "Booked"
   return result

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(1, 1, 1))
print('Seat in row 5, place 5:', seat_status(25, 5, 5))
print('Seat in row 3, place 5:', seat_status(15, 3, 3))