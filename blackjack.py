
from p1_random import P1Random

# this utilizes our random number import and sets up the random number generator
rng = P1Random()

# here I define the variables for the rest of the program.
# I set all of them to zero, so they can be incremented on through the program

num_of_games = 0
player_wins = 0
dealer_wins = 0
num_of_ties = 0
gaming = True

# Sets up first while loop that gives the player their initial card and hand for users first attempt
# or for when the program exits after a win/lose/tie but user wants to continue playing.

while gaming:
    num_of_games = num_of_games + 1 # this variable and the following equation keeps track of how many games are played.
    print('START GAME #', num_of_games)
    player_sum = 0  # sets the variable responsible for keeping track of player hand to 0.
    player_card = rng.next_int(13) + 1 # generates random number between 1 and 13 inclusively.
    if player_card == 1:
        print('Your card is a ACE!')
    elif player_card == 2:
        print('Your card is a 2!')
    elif player_card == 3:
        print('Your card is a 3!')
    elif player_card == 4:
        print('Your card is a 4!')
    elif player_card == 5:
        print('Your card is a 5!')
    elif player_card == 6:
        print('Your card is a 6!')
    elif player_card == 7:
        print('Your card is a 7!')
    elif player_card == 8:
        print('Your card is a 8!')
    elif player_card == 9:
        print('Your card is a 9!')
    elif player_card == 10:
        print('Your card is a 10!')
    elif player_card == 11:
        print('Your card is a JACK!')
        player_card = 10  # although the player card must be 11 to receive a Jack, this ensures that the card value is 10
    elif player_card == 12:
        print('Your card is a QUEEN!')
        player_card = 10
    elif player_card == 13:
        print('Your card is a KING!')
        player_card = 10
    player_sum = player_sum + player_card # this equation increments upon the player card to calculate the 'hand aspect'
    print('Your hand is:',player_sum)
# sets up second while loop that allows player to choose an option and executes the resulting sequence of events.
    menu = True
    while menu:
        print('1. Get another card')
        print('2. Hold hand')
        print('3. Print statistics')
        print('4. Exit')
        option = int(input('Choose an option:')) # takes user input for the option they choose
        if option == 1:
            player_card = rng.next_int(13)+1  # generates random number between 1 and 13 inclusively.
            if player_card == 1:
                print('Your card is a ACE!')
            elif player_card == 2:
                print('Your card is a 2!')
            elif player_card == 3:
                print('Your card is a 3!')
            elif player_card == 4:
                print('Your card is a 4!')
            elif player_card == 5:
                print('Your card is a 5!')
            elif player_card == 6:
                print('Your card is a 6!')
            elif player_card == 7:
                print('Your card is a 7!')
            elif player_card == 8:
                print('Your card is a 8!')
            elif player_card == 9:
                print('Your card is a 9!')
            elif player_card == 10:
                print('Your card is a 10!')
            elif player_card == 11:
                print('Your card is a JACK!')
                player_card = 10
            elif player_card == 12:
                print('Your card is a QUEEN!')
                player_card = 10
            elif player_card == 13:
                print('Your card is a KING!')
                player_card = 10
            player_sum = player_sum + player_card # keeps track of the 'hand' aspect of the game.
            print('Your hand is:', player_sum)
            # the following segment prints the result according to player sum and keeps track of statistics values.
            if player_sum ==21:
                print('BLACKJACK! You win!')
                player_wins = player_wins + 1 # keeps track of the times the player wins.
                menu = False
            elif player_sum > 21:
                print('You exceeded 21! You lose.')
                dealer_wins = dealer_wins + 1 # keeps track of the times the dealer wins.
                menu = False  # this allows the second while loop to end restart the first while loop.
        elif option == 2:
            dealer_card = rng.next_int(11)+16 # generates random number between 16 and 26 inclusively.
            print('Dealer\'s hand:', dealer_card)
            print('Your hand is:', player_sum)
            if dealer_card > 21:
                print('You win!')
                player_wins = player_wins + 1
                menu = False # ending the second while loop allows player hand & game values to be calculated accurately
            elif dealer_card == 21:
                print('Dealer wins!')
                dealer_wins = dealer_wins + 1
                menu = False
            elif dealer_card == player_sum:
                print('It\'s a tie! No one wins!')
                num_of_ties = num_of_ties + 1  # keeps track of the number of ties
                menu = False
            else:
                if dealer_card > player_sum:
                    print('Dealer wins!')
                    dealer_wins = dealer_wins+1
                    menu = False
                else:
                    print('You win!')
                    player_wins = player_wins + 1
                    menu = False
        elif option == 3: # if the user chooses 3 then the following statistics will print
            percentage = round((player_wins/(num_of_games-1)*100),2) # this rounds the result to 2 decimal points.
            print('Number of Player wins:', player_wins)
            print('Number of Dealer wins:', dealer_wins)
            print('Number of tie games:', num_of_ties)
            print('Total # of games played is:', num_of_games - 1)
            print('Percentage of Player wins:', percentage, '%')
        elif option == 4:
            exit() # exits the program without having to set boolean variables to false.
        else: # if the user inputs something other than a number 1-4, the following output prints.
            print('Invalid input!')
            print('Please enter an integer value between 1 and 4.')



