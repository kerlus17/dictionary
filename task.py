contacts={}
contacts["kero"]="01201020304"
contacts["omr"]="012090807005"
contacts["lili"]="01204356304"

for name in contacts:
    print (name)

search=input("enter name: ")

if search in contacts:
    print (f"phone number for   {search}:{contacts[search]}")
else:
    print ("not found")