current=int(input("Enter the current year"))
final=int(input("Enter the final year"))
for num in (range(current,final)):
    if num % 4==0:
        print(num)