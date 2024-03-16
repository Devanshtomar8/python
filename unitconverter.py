def print_menu():
    print('1.kilometers to miles')
    print('2.miles to kilometers ')
def km_miles():
    km=float(input('Enter a distance in kilometers:'))
    miles=km/100
    print('Distance in miles ',miles)
def miles_km():
    miles=float(input('Enter a distance in miles:'))
    km=miles*100
    print('Distance in kilometers',km)
def meter_feet():
    meter=int(input('Enter a distance in meter:'))
    ft=meter*3.28
    print('Distance in feet}',ft)
def feet_meter():
    feet=float(input('Enter a distance in feet:'))
    meter=feet/3.28
    print('Distance in meter',meter)
print_menu()
miles_km()
km_miles()
meter_feet()
feet_meter()