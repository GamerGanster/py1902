number =int(input("enter the number: "))
sum = (number // 10000) + (number // 10 // 10 // 10 % 10) + (number // 10 // 10 % 10) + (number // 10 % 10) + (number % 10)
print (sum)
mult = (number // 10000) * (number // 10 // 10 // 10 % 10) * (number // 10 // 10 % 10) * (number // 10 % 10) * (number % 10)
print (mult)
# print (number // 10000)
# print (nunber // 10 // 10 // 10 % 10)
# print (number // 10 // 10 % 10)



