price = int(input("구입 금액 : "))
dc_price = 0
if price >= 100000:
    dc_price = price*0.95
else:
    dc_price = price

print(dc_price)