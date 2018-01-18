Apple = 25
Tuna = 2
Rice = 1.5
Tilapia = 3
Bangus = 4
grand_total = 0
catfood = 7

def grocery_compute(Apple, Tuna, Rice, Tilapia = 4, Bangus = 1):
    grocery_total = Tilapia + Bangus + int(Apple) + int(Tuna) + float(Rice)
    print grocery_total
    return grocery_total

grand_total = grocery_compute(Apple, Tuna, Rice)
grand_total += catfood
print grand_total
