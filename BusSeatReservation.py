bus=[["a","a","a"],
     ["a","a","a"],
     ["a","a","a"],
     ["a","a","a"],
     ["a","a","a"]]

print("\n")

for i in  range(5):
    print(bus[i])

print("\n---------select your seat--------\n")
row=int(input("Enter Row Number :"))
seat=int(input("Enter Seat Number :"))
print("\n---------------------------------")

if bus[row-1][seat-1]=="a":
    bus[row-1][seat-1]="r"
    print("Your Seat Is Reserve.")
else:
    print("Seat Is Already Reserve.")
print("----------------------------------")

for i in  range(5):
    print(bus[i])
