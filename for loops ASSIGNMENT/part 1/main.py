while True:  # Start an infinite loop
    valuelimit = int(input("Enter the number limit to prevent the python IDLE/IDE to crash: ")) # Ask's the user for a limit
    n = int(input("Enter the number of multiples you want: ")) # Enter the number of multiples from the user
    if n > valuelimit:
        raise ValueError("Enter a number under your limit which is:", valuelimit)
    print(f"The first {n} multiples of 35 are:") # Tells the person what he has chosen
    for i in range(1, n + 1): # Does the for action for the number given (multiple and 35)
        multiple = 35 * i # Multiplies 35 with the multiple
        print("35 X ", i, "=", multiple) # Shows the multiple on the screen
    
    # Ask if the user wants to repeat
    repeat = input("Do you want to repeat the process? (yes/no): ").strip().lower()
    if repeat != 'yes':  # Exit the loop if the user doesn't want to repeat
        break
