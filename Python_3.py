print("Введите букву")
ch=str(input())
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
    print("Гласная")
elif ch == 'y':
    print("Может быть и гласной и согласной")
else: 
    print("Согласная")
