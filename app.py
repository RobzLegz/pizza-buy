price1 = float(input("Enter price 1: "))
size1 = 25

price2 = float(input("Enter price 2: "))
size2 = 30

pi = 3.14

def get_area(size):
    area = (size / 2) ** 2 * pi

    return area

area1 = get_area(size1)
area2 = get_area(size2)

def get_value(price, area):
    value = price / area
    
    return value

val1 = get_value(price1, area1)
val2 = get_value(price2, area2)

def compare(val1, val2):
    if val1 > val2:
        print(f"{val1} > {val2}")
    else:
        print(f"{val1} < {val2}")

compare(val1, val2)
