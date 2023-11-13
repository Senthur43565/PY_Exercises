import random

# Define the symbols for the slot machine
symbols = ["Cherry", "Lemon", "Orange", "Plum", "Bell", "Bar", "Seven"]

# Define the payouts for different symbol combinations
payouts = {
    ("Cherry", "Cherry", "Cherry"): 10,
    ("Lemon", "Lemon", "Lemon"): 20,
    ("Orange", "Orange", "Orange"): 30,
    # Define more payout combinations here
}

# Function to spin the slot machine
def spin():
    results = [random.choice(symbols) for _ in range(3)]
    return results

# Function to determine the payout based on the results
def calculate_payout(results):
    result_tuple = tuple(results)
    if result_tuple in payouts:
        return payouts[result_tuple]
    else:
        return 0

# Function to play the slot machine
def play_slot_machine():
    print("Welcome to the Slot Machine!")
    while True:
        input("Press Enter to spin...")
        results = spin()
        print("Results:", results)
        payout = calculate_payout(results)
        print("Payout:", payout)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    play_slot_machine()
