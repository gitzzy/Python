print("Voter eligibilty")
Name = input("Enter Your Name : ")
Age = int(input("Enter Your Age : "))

if Age >= 18:
    print("Congratulations! "+Name+" you can Vote.")
elif Age <= 0:
    print("Unfortunately! "+Name+" that is not possible.")
else:
    print("Sorry! "+Name+" you can't Vote.")
    print("Try Some other time")

if(Age==18):
    print("SO it is your first time votning")