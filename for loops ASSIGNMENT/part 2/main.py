# Welcome to my humble project
while True:
    typeofexam = str(input("Review or Term end exam? ")).upper()  # Turns the input to uppercase

    if typeofexam == "REVIEW":
        max_marks = 30
    elif typeofexam == "TERM END EXAM":
        max_marks = 50
    else:
        print("Invalid input, please enter 'Review' or 'Term end exam'")
        continue
    
    num_subjects = int(5)
    total_marks = 0

    # Collect marks for the specified number of subjects
    for i in range(num_subjects):
        while True:
            mark = float(input(f"Enter mark for subject {i + 1} (max {max_marks}): "))
            if mark <= max_marks:
                total_marks += mark
                break
            print(f"Can't go higher than {max_marks}. Try again!")

    # Average calculator 
    average = total_marks / num_subjects

    # Show off the final score (exaggeration) 
    print(f"The average mark is: {average:.2f}")

    # Ask if the user wants to calculate another type of exam
    calculate_another = input("Do you want to calculate another type of exam marks? (y/n): ").strip().lower()
    if calculate_another != 'y':
        play_again = input("Want to calculate more marks? (y/n): ").lower()
        if play_again != 'y':
            break
