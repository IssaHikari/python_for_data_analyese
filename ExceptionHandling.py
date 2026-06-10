# potential code before try catch

# try:
#     # code to try to execute
# except:
    # code to execute if there is an exception
    
# code that will still execute if there is an exception

a = 1

try:
    b=int(input("enter your number :"))
    a = a/b
    print(a)
except:
     print("There was an error")


a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
else:
    print("value of a is :" , a)
finally:
    print("the programm finished")

try:
    x = 10 / 0

except Exception as e:
    print("الخطأ هو:", e)

a= 0
if(a<1):
    raise ValueError("this value isnot good")

try:
    num1 = int(input("أدخل الرقم الأول: "))
    num2 = int(input("أدخل الرقم الثاني: "))

    result = num1 / num2

except ValueError:
    print("يجب إدخال أرقام صحيحة.")

except ZeroDivisionError:
    print("لا يمكن القسمة على الصفر.")

else:
    print("الناتج =", result)

finally:
    print("شكراً لاستخدام البرنامج.")