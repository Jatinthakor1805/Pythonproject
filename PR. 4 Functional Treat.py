data = []
data_summary = {}

def input_data():
    global data

    print("\n Data input")
    print("1. Enter 1D Array")
    print("2. Enter 2D Array")

    choice = int(input("Please Enter Your Choice: "))
    choice == "1"
    value = input("Enter data for a 1D array (separated by spaces):")
    data = list(map(int, value.split()))
    if len(data) == 0:
        print("Pls enter at least one value. ")
                          
# while True:
#     print("Welcome to the data Analyzer and Transformer Program")

#     print("\nMain Menu:")
#     print("1. Input Data")
#     print("2. Display Data Summary (Built-in Functons)")
#     print("3. Calculate Factorial (Recursion)")
#     print("4. Filter Data by Threshold (Lambda Function)")
#     print("5. Sort Data")
#     print("6. Display dataset statistics (Return Multiple Values)")
#     print("7. Exit program")

#     choice = int(input("Please Enter Your Choice: "))
    