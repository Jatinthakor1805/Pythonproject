while True:
# Step 1
    print("Welcome to the pattern Generator and Number Analyzer !")
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
# Step 2

    if choice == 1:
        row = int(input("Enter rows: "))

        print("Pattern")
        for i in range(1, 6):
            print("* " * i)
# Step 3

    elif choice == 2:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        total = 0
        for i in range(start, end+1):
            if i % 2 == 0:
                print(i, "is Even")

            else:
                print(i, "is Odd")
                total = total + i
        print("Sum of all numbers", total)
        
#step 4
    elif choice == 3:
        print("Goodby!")
        break
    else:
        print("Invalid Choice")
        

