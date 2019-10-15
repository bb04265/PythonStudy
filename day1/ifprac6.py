purchasePrice = int(input("구입 금액을 입력하시오 : "))
discountRate = float(0.95)
discountPrice = purchasePrice * discountRate

if purchasePrice > 100000 :
    print("지불 금액은 ", discountPrice, "입니다.")

else:
    print("지불 금액은 ", purchasePrice, "입니다.")



total = int(input("계산내용 : "))
if total >= 100000 :
    print("지불 금액은 ", total - (total * 0.05), "입니다.")

else :
    pass