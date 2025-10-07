import sys

def create_instance(type):
 if type == "t2.micro":
    print("okay, instance is creating, charge : $5")
 elif type == "t2.small":
    print("okay, crreating samll instance, charge : $10")
 elif type == "t2.medium": 
    print("okay, creating medium instance, charge : $15")

 else:
    print("no permission, choose right instance type")

def confirmation(type, confirm):
   if confirm == "yes":
      create_instance(type)
   else:
     print("under 18 - access not granted")

type = sys.argv[1]
confirm = input("are you 18+? (yes/no): ").strip().lower()
confirmation(type, confirm)

###########################




