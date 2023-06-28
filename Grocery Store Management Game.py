import random

class GroceryStore:
    def __init__(self):
        self.inventory = {'apple': 10, 'banana': 15, 'orange': 20}
        self.leaderboard = {}

    def buy(self, item, quantity):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            return True
        return False

    def sell(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def update_leaderboard(self, player, score):
        if player in self.leaderboard:
            self.leaderboard[player] += score
        else:
            self.leaderboard[player] = score

    def print_leaderboard(self):
        sorted_leaderboard = sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)
        print("Leaderboard:")
        for player, score in sorted_leaderboard:
            print(f"{player}: {score}")

def main():
    game = GroceryStore()
    players = ['Player 1', 'Player 2', 'Player 3']

    while True:
        print("\n--- Grocery Store Management Game ---")
        print("1. Buy groceries")
        print("2. Sell groceries")
        print("3. Print inventory")
        print("4. Print leaderboard")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item you want to buy: ")
            quantity = int(input("Enter the quantity: "))
            success = game.buy(item, quantity)
            if success:
                print(f"You bought {quantity} {item}(s)!")
            else:
                print("Sorry, the item is not available or the quantity is not sufficient.")

        elif choice == '2':
            item = input("Enter the item you want to sell: ")
            quantity = int(input("Enter the quantity: "))
            game.sell(item, quantity)
            print(f"You sold {quantity} {item}(s)!")
        
        elif choice == '3':
            print("Current Inventory:")
            for item, quantity in game.inventory.items():
                print(f"{item}: {quantity}")

        elif choice == '4':
            game.print_leaderboard()

        elif choice == '5':
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Please try again.")

        # Simulate competition and update leaderboard
        for player in players:
            score = random.randint(1, 10)
            game.update_leaderboard(player, score)

if __name__ == '__main__':
    main()
