Name=input("Enter your name :")
print("Hello ! "+Name)
print (type(Name))
# Note by Defult  it takes String Datatypes
# How to conver into to integer ,then we have to convert string into integer type casting
# Number=input("Enter your Number :") #this will give an error
Number=  int((input("Enter your Number :"))) #this will not give an error

print("your Number "+Number)
result=Number+1
print (type(Number))