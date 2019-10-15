account_num = input("계좌번호를 입력하시오: ")
result_num = ""
for x in account_num:
    if x != "-":
         result_num += x
print(result_num)