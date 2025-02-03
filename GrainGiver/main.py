from random import randint as r  # Importing randint function from random module and naming the function it as 'r'

while True:  # Infinite loop to keep the program running until the user chooses to exit
    print("Welcome to Orphanage app")
    print("1. Donate")
    print("2. Buy grains")
    
    # Taking user input and removing any extra spaces by accident
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "2":  # If the user chooses to buy grains
        print("1. Rice")
        print("2. Wheat")
        print("3. Sugar")
        print("4. Milk")
        print("5. Oil")
        print("6. Dal")
        print("7. Pulses")
        print("8. Salt")
        print("9. Spices")
        print("10. Tea")
        print("11. Coffee")
        
        # Taking user input for grain selection and number of people
        grain_choice = int(input("Select the grain/spice you want to buy (use the number on the left): "))
        num_people = int(input("Enter the number of people: "))
        
        # Defining weight per person for each item
        rice_weight = 0.5
        wheat_weight = 0.5
        sugar_weight = 0.2
        milk_weight = 1.0
        oil_weight = 0.5
        dal_weight = 0.3
        pulses_weight = 0.3
        salt_weight = 0.1
        spices_weight = 0.05
        tea_weight = 0.1
        coffee_weight = 0.1
        
        # Calculating total weight needed based on user choice
        if grain_choice == 1:
            total_weight = rice_weight * num_people
        elif grain_choice == 2:
            total_weight = wheat_weight * num_people
        elif grain_choice == 3:
            total_weight = sugar_weight * num_people
        elif grain_choice == 4:
            total_weight = milk_weight * num_people
        elif grain_choice == 5:
            total_weight = oil_weight * num_people
        elif grain_choice == 6:
            total_weight = dal_weight * num_people
        elif grain_choice == 7:
            total_weight = pulses_weight * num_people
        elif grain_choice == 8:
            total_weight = salt_weight * num_people
        elif grain_choice == 9:
            total_weight = spices_weight * num_people
        elif grain_choice == 10:
            total_weight = tea_weight * num_people
        elif grain_choice == 11:
            total_weight = coffee_weight * num_people
        else:
            total_weight = 0  # If an invalid choice is made, set weight to 0
            raise ValueError("Invalid choice.")  # Raise an error if an invalid choice is made
        
        print("Total weight needed: ", total_weight, "kg/liters")  # Output total weight
        
    elif choice == "1":  # If the user chooses to donate
        mode = input("Pickup or Drop at our outlet? (pickup, drop): ").strip().lower()
        
        if mode == "drop":  # If user selects drop option
            outlet = input("1 - BTM Layout, 2 - J P Nagar: ").strip()
            if outlet == "1":
                print("#123, 3rd Cross, 13th Main Road, BTM Layout 1st Stage, Bengaluru, Karnataka 560029")
                    
                print("You can drop it at:", r(6, 12), "PM")  # Generating random drop time
            elif outlet == "2":
                print("456, 2nd Main Road, J P Nagar 3rd Phase, Bengaluru, Karnataka 560078")
                    
                print("You can drop it at:", r(8, 12), "AM")  # Generating random pickup time
            else:
                print("Invalid number selected.")
        
        elif mode == "pickup":  # If user selects pickup option
            location = str(input("Enter your location: "))  # Taking location input
            time = r(8, 10)  # Generating a random time between 8 to 10
            ap = r(1, 2)  # Randomly selecting AM or PM
            if ap == 1:
                set_ = "AM"
            else:
                set_ = "PM"
            print("A person will pick up your extra food at", location, "at", time, set_)  # Output pickup details
        else:
            print("Invalid mode selected.")  # Handling invalid input for mode
    else:
        print("Invalid input.")  # Handling invalid input for choice
    
    # Asking user if they want to repeat the process
    repeat = input("Do you want to repeat again? (yes/no): ").strip().lower()
    if repeat != "yes":  # If user inputs anything other than 'yes', exit the loop
        print("Thank you for using Orphanage app!")
        break
# This code is long, isn,t it? But it is very useful.Please give it a try and let me know what you think at my email.
# adityacukkemane@ekyaschools.com
# Authors - Aditya Cukkemane
# Flowchart - Jayant Chatterjee
# Algorithm - Surya Nambiar