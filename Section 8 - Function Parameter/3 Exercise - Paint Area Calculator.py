import math

def paint_calc(height, width, cover):
    Number_of_Cans = (height * width) / cover
    cans = math.ceil(Number_of_Cans)
    print(f"You need to buy {cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w= int(input("Width of wall: "))
coverage = 5

paint_calc(height = test_h, width = test_w , cover = coverage)