print("******************** Expances ********************")
expances=0.0
food=0.0
shopping=0.0
traveling=0.0
other=0.0

while True:
    value=float(input("Enter your amount :"))
    if value==-1:
         break
    categroy=input("Enter your categroy(food/shopping/traveling/other)").lower()


    if categroy=="food":
         food+=value
    elif categroy=="shopping":
         shopping+=value
    elif categroy=="traveling":
         traveling+=value
    elif categroy=="other":
         other+=value
    else :
         print("Invalid category!")
         continue

    expances += value

print("**************** Expences Summary ")

print("food       :",food)
print("shopping   :",shopping)
print("traveling  :",traveling)
print("other      :",other)
print("Total Expences :",expances)
