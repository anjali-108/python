feedback=input("Enter a feedback :")

print("feedback format report".upper().center(100))
print("\n__________________________________________________________________________________________________________\n")
print("\noriginal feedback :-\n ".title())

print(feedback.upper())

print("\nfeedback summary :-".title())

print("Total words count :".title(),len(feedback.split()))
print("Total char count :".title(),len(feedback))
print("Total space count :".title(),feedback.count(" "))
print("Total excplamation mark count :".title(),feedback.count("!"))

print("\n")
print("Formated Feedback :- ".lstrip())

print("Upper Case Feedback :",feedback.upper())
print("Lower Case Feedback :",feedback.lower())
print("Title Case feedback :",feedback.title())
print("Capitalise Feedback :",feedback.capitalize())
print("Swap Case Feedback :",feedback.swapcase())

print("\nProfessional feedback :- ".capitalize())

print("Split Case Feedback :",feedback.split())

print("\n_______________________________________________________________________________________________________________\n")

print("thank you for your valuable feedback".center(100).upper())

print("\n***************************************************************************************************************\n")