import random

class Game():
    def __init__(self):
        self.user_item = None
    def get_user_item(self): 
        while True: 
            user_choice = input("Select (r)ock, (p)aper, or (s)cissors: ").lower() 
            if user_choice in ['r', 'p', 's']: 
                self.user_item = user_choice 
                return user_choice 
            else:
                print("Invalid input, please try again.")
    
    def get_computer_item(self):
        self.computer_item = random.choice(["R", "P", "S"])
        return self.computer_item.lower()
    
    def get_game_result(self, user_item, computer_item): 
        if user_item == computer_item: 
            return 'draw' 
        elif (user_item == 'r' and computer_item == 's') or (user_item == 'p' and computer_item == 'r') or (user_item == 's' and computer_item == 'p'): 
            return 'win' 
        else: return 'loss'
    
    def play(self): 
        
        user_item = self.get_user_item() 
        computer_item = self.get_computer_item() 
        result = self.get_game_result(user_item, computer_item) 
        print(f"You selected {user_item}. The computer selected {computer_item}. You {result}") 
        return result

    
    