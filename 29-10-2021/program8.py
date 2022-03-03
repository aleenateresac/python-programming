#program to calculate total and percentage
name=input("Enter your name")
print("Enter your marks out of 100")
sub1=int(input("Enter marks in mathematics"))
sub2=int(input("Enter marks in physics"))
sub3=int(input("Enter marks in chemistry"))
sub4=int(input("Enter marks in English"))
sub5=int(input("Enter marks in malayalam"))
total=sub1+sub2+sub3+sub4+sub5
percentage=(total/500)*100
print("Total marks you gained",total)
print("total percentage:",percentage)