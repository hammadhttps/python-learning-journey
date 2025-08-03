import random

class SlotMachine:
    def __init__(self):
        self.symbols = ["🍎", "🍊", "🍐", "🍇", "🍓", "🍒", "💎", "7️⃣"]
        self.balance = 0
        self.bet = 0
        self.game_running = True
    
    def get_user_balance(self):
        """Get initial balance from user"""
        while True:
            try:
                balance = int(input("Enter your starting balance $: "))
                if balance > 0:
                    return balance
                else:
                    print("❌ Invalid balance. Must be greater than 0.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
    
    def get_user_bet(self):
        """Get bet amount from user"""
        while True:
            try:
                bet = int(input(f"Enter your bet (1-{min(100, self.balance)}) $: "))
                if 1 <= bet <= min(100, self.balance):
                    return bet
                else:
                    print(f"❌ Invalid bet. Must be between 1 and {min(100, self.balance)}.")
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
    
    def get_user_choice(self):
        """Get user's game choice"""
        while True:
            choice = input("\n🎰 What would you like to do? (spin/quit): ").lower().strip()
            if choice in ["spin", "quit"]:
                return choice
            else:
                print("❌ Invalid choice. Please enter 'spin' or 'quit'.")
    
    def spin_slot_machine(self):
        """Generate random symbols for the slot machine"""
        return [random.choice(self.symbols) for _ in range(3)]
    
    def display_reels(self, reels):
        """Display the slot machine reels"""
        print("\n" + "="*20)
        print("🎰 SLOT MACHINE 🎰")
        print("="*20)
        print(f"  {reels[0]} | {reels[1]} | {reels[2]}")
        print("="*20)
    
    def check_win(self, reels):
        """Check if the spin is a winning combination"""
        return reels[0] == reels[1] == reels[2]
    
    def calculate_winnings(self, reels):
        """Calculate winnings based on the combination"""
        if self.check_win(reels):
            # Different symbols have different payouts
            symbol = reels[0]
            if symbol == "💎":
                return self.bet * 10  # Diamond pays 10x
            elif symbol == "7️⃣":
                return self.bet * 7   # Seven pays 7x
            elif symbol == "🍒":
                return self.bet * 5   # Cherry pays 5x
            else:
                return self.bet * 3   # Other symbols pay 3x
        return 0
    
    def display_balance(self):
        """Display current balance"""
        print(f"\n💰 Current Balance: ${self.balance}")
    
    def handle_win(self, reels, winnings):
        """Handle winning scenario"""
        self.balance += winnings
        print(f"🎉 JACKPOT! You won ${winnings}!")
        print(f"💰 Your balance is now ${self.balance}")
    
    def handle_loss(self):
        """Handle losing scenario"""
        self.balance -= self.bet
        print(f"😔 Sorry! You lost ${self.bet}")
        print(f"💰 Your balance is now ${self.balance}")
    
    def check_game_over(self):
        """Check if the game should end"""
        if self.balance == 0:
            print("\n💸 You're out of money!")
            return self.ask_to_continue()
        return True
    
    def ask_to_continue(self):
        """Ask user if they want to continue playing"""
        while True:
            choice = input("\n🔄 Would you like to add more money? (y/n): ").lower().strip()
            if choice == 'y':
                self.balance = self.get_user_balance()
                return True
            elif choice == 'n':
                return False
            else:
                print("❌ Please enter 'y' or 'n'.")
    
    def play_round(self):
        """Play one round of the slot machine"""
        # Get bet
        self.bet = self.get_user_bet()
        
        # Spin the machine
        reels = self.spin_slot_machine()
        self.display_reels(reels)
        
        # Check for win
        winnings = self.calculate_winnings(reels)
        if winnings > 0:
            self.handle_win(reels, winnings)
        else:
            self.handle_loss()
    
    def run(self):
        """Main game loop"""
        print("🎰 Welcome to the Slot Machine! 🎰")
        print("="*40)
        
        # Get initial balance
        self.balance = self.get_user_balance()
        
        # Main game loop
        while self.game_running:
            self.display_balance()
            
            # Check if player can continue
            if not self.check_game_over():
                break
            
            # Get player choice
            choice = self.get_user_choice()
            
            if choice == "spin":
                self.play_round()
            elif choice == "quit":
                break
        
        # Game over
        print(f"\n🎰 Thanks for playing! Final balance: ${self.balance}")
        if self.balance > 0:
            print("💰 You're leaving with a profit!")
        else:
            print("💸 Better luck next time!")

def main():
    """Main function to start the game"""
    game = SlotMachine()
    game.run()

if __name__ == "__main__":
    main()
