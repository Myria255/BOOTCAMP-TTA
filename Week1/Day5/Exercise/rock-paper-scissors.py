
from game import Game

def get_user_menu_choice(): 
    print("\nMenu:") 
    print("(p) Play a new game") 
    print("(s) Show scores") 
    print("(q) Quit") 
    return input("Enter your choice: ").lower()

def print_results(results):
    for key, value in results.items():
        
        print("this is the result of the game: ")
        print(f"{key.capitalize()}: {value}")
        
def main():
    results = {"wins": 0, "losses": 0, "ties": 0}
    while True:
        user_choice= get_user_menu_choice().lower()
        if user_choice == "q":
            print_results(results)
            break
        elif user_choice == 'p': # Use lowercase for consistency
            new_game = Game()
            game_result =new_game.play() # Capture the returned result
            if game_result == 'win':
                results['wins'] += 1
            elif game_result == 'loss':
                results['losses'] += 1
            elif game_result == 'draw':
                results['ties'] += 1
        
        elif user_choice == 's':
            print_results(results)

main()
