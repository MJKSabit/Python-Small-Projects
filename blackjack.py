from random import choice

class GameVarriable:
    
    money_in_hand = 500
    money_in_bet = 0

    player_name = ""

    card_by_value = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'K':10, 'Q':10}

class Player:

    def __init__(self, name):
        self.name = name
        card = self.random_card()

        self.in_hand_card = [card]

    how_many_ace = 0

    def random_card(self):
        card = choice(GameVarriable.card_by_text)
        GameVarriable.card_by_text.pop(GameVarriable.card_by_text.index(card))

        if card == 'A':
            self.how_many_ace += 1

        return card


    def in_hand_card_sum(self):
        
        in_hand_card_value = [GameVarriable.card_by_value[index] for index in self.in_hand_card]
        card_sum = sum(in_hand_card_value)

        if 21 > card_sum:
            card_sum += 10*min((21-card_sum)//10, self.how_many_ace)

        return card_sum


    def print_info(self):
        print("\n"+"-"*100)
        print(f"Points in hand for {self.name}: {self.in_hand_card_sum()}")

        for card in self.in_hand_card:
            print(f"[{card}]", end=' ')
        # print(*card, sep='] [')

        print("\n"+"-"*100)

    def hit(self):
        self.in_hand_card += [self.random_card()]

        card_sum = self.in_hand_card_sum()
        self.print_info()

        return card_sum

def reset():
    GameVarriable.card_by_text = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'K', 'Q']*4
    GameVarriable.player = Player(GameVarriable.player_name)
    GameVarriable.dealer = Player("Dealer")

    return (GameVarriable.player, GameVarriable.dealer)

def set_user_name(name):
    GameVarriable.player_name = name


def initiate_new_game():
    
    if GameVarriable.money_in_hand <= 0:
        exit()

    while True:

        try:
            GameVarriable.money_in_bet = int(input(f"Current Balance: ${GameVarriable.money_in_hand}\nHow much you want to bet?\n$"))

            if GameVarriable.money_in_bet > GameVarriable.money_in_hand or GameVarriable.money_in_bet<=0:
                print("Not much money in hand or no money!, TRY AGAIN")
                continue
            
            GameVarriable.money_in_hand -= GameVarriable.money_in_bet
            break
        except:
            continue


def ask_hit():
    ans = None
    while True:
        ans = input("[Hit] or [Stand]: ")

        if ans[0].upper()=='H' or ans[0].upper()=='S':
            return ans[0].upper()=='H'

        print("Invalid Input, TRY AGAIN")

def end_game(pl):

    if pl:
        print(pl.name.capitalize()+" has - W O N - the game!!!")
    
    if input("Press [Enter] to continue your game! (or No)\n") == '':
        initiate_new_game()
        
        player, dealer = reset()

        player.hit()
        dealer.print_info()

        start_game(player, dealer)
    else:
        exit()

def whole_new_game():

    set_user_name(input("Your name: "))

    player, dealer = reset()

    point = player.hit()
    dealer.print_info()

    return player, dealer

def start_game(player, dealer):

    if player.in_hand_card[0] == player.in_hand_card[1] and input("Split? [Yes]/[No]")[0].upper() == 'Y':
        # Split
        print("Split...")
        pass
    else:
        if dealer.in_hand_card[0] == 'A' and input("Insure? [Yes]/[No]")[0].upper() == 'Y':
            # Insure
            GameVarriable.money_in_hand += GameVarriable.money_in_bet/2
            GameVarriable.money_in_bet /= 2

            stand(player, dealer)
        else:
            while ask_hit():
                point = player.hit()

                if point>21:
                    end_game(dealer)
            else: # Stand
                stand(player, dealer)

def stand(player, dealer):
    dealer_point = dealer.hit()
    player_point = player.in_hand_card_sum()

    while dealer_point<=21 and player_point>dealer_point:
        dealer_point = dealer.hit()

    if dealer_point==player_point:
        GameVarriable.money_in_hand += GameVarriable.money_in_bet
        print("----- P U S H --------")
        end_game(None)
        # Push
    elif dealer_point>21:
        GameVarriable.money_in_hand += 2*GameVarriable.money_in_bet
        end_game(player)
    else:
        # dealer_point>player_point:
        end_game(dealer)


# Main Game Starts
initiate_new_game()

p, d = whole_new_game()
start_game(p, d)