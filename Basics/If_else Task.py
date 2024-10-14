# 1
"""years=int(input('Enter Years Service = '))
rating=str(input("Enter Rating : (Good,Excellent,Average)"))
salary=int(input('Enter Salary : '))

if years>10 and rating=="Excellent":
    print(f"{years} , {rating} , {salary+((salary*20)/100)}")
elif  5<years<10 and rating=="Good":
    print(f"{years} , {rating} , {salary+((salary*10)/100)}")
else :
    print(f"{years} , {rating} , {salary+((salary*5)/100)}")
"""
# 2
"""score = int(input("Enter Avg Score : "))

if score > 90:
    print("Got A Grade")
elif 80 < score <= 90:
    print("Got B Grade")
elif 70 < score <= 80:
    print("Got C Grade")
elif 60 < score <= 70:
    print("Got D Grade")
elif 50 < score <= 60:
    print("Got E Grade")
else:
    print("Failed!..")"""

# 3

"""weight=int(input("Enter Weight of Goods : "))
destination=str(input("Enter Destination : "))

if weight<5 and destination=="domestic":
    print("Shipping Cost Is 5$")
elif 5<weight<20 and destination=="domestic":
    print("Shipping Cost Is 10$")
elif weight>20 and destination=="domestic":
    print("Shipping Cost Is 20$")
elif destination=="international":
    print("Shipping Cost Is 30$")
else:
    print("Sorry😟")"""

# 4
"""usr="Deep_85"
ps="Deep_0106"
user=input("Enter UserName : ")
passw=input("Enter Password : ")

if user==usr and passw==ps:
    print("Access Granted")
elif user==usr and passw!=ps:
    print("Enter Correct Password")
else:
    print("Invalid Username and Password")"""

# 5

"""unit = int(input("Enter Units: "))
total = 0

# Calculate for the first 100 units
if unit > 100:
    total += 100 * 0.5
    unit -= 100
else:
    total += unit * 0.5
    unit = 0

# Calculate for the next 100 units (101-200)
if unit > 100:
    total += 100 * 0.75
    unit -= 100
else:
    total += unit * 0.75
    unit = 0

# Calculate for units above 200
if unit > 0:
    total += unit * 1.0

# Add a 10% surcharge if total exceeds $100
if total > 100:
    total += total * 0.10

if total < 20:
    total-=total*0.5
    
    
print(f"Total Cost is: ${total:.2f}")
"""


# 6
x = 7
y = 8

if x > 0 and y > 0:
    print("First Quadrant")
elif x < 0 and y > 0:
    print("Second Quadrant")
elif x < 0 and y < 0:
    print("Third Quadrant")
elif x > 0 and y < 0:
    print("Fourth Quadrant")
elif x == 0 and y != 0:
    print("Lies on the Y-axis")
elif y == 0 and x != 0:
    print("Lies on the X-axis")
else:
    print("Origin")
