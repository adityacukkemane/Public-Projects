while True: #starts a infinite loop 
    card_number = int(input("Enter a card number (1-13): ")) #asks the user for a number
    if card_number >= 13 or card_number <= 0: #if the card is 13 or -1, the loop will stop
        print("Terminating execution")
        break
    print("Card number:" ,card_number)
