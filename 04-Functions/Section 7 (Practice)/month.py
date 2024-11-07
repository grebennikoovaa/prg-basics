###
# write a program to print the name of the month 7
##

def months(n):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if 1 <= n <= 12:
        return months[n - 1]