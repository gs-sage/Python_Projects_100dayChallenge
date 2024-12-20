import random

#changed the player and dealer functions to only take predetermined lists
# and empty lists
# moved the logic part to the blackjack function

def dealer(card_list, empty_list):
    dealer_first_card = random.choice(card_list)
    empty_list.append(dealer_first_card)
    print(f"Dealer's first card : {empty_list}")
    return empty_list

    # if user_input == "y":
    #     for i in range(len(empty_list)):
    #         i = random.choice(card_list)
    #         empty_list.append(i)
    #         print(f"Dealer's second card : {empty_list}")
    #
    # return sum(empty_list)

def player(card_list, empty_list):
    player_first_card = random.choice(card_list)
    player_second_card = random.choice(card_list)
    empty_list.append(player_first_card)
    empty_list.append(player_second_card)
    print(f"Player's first two cards : {empty_list}")
    return empty_list

    # if user_input == "y":
    #     for i in range(len(empty_list) - 1):
    #         i = random.choice(card_list)
    #         empty_list.append(i)
    #         print(f"Player's third card : {empty_list}")
    # return empty_list

def blackjack(card_list, game, dealer_empty_list, player_empty_list):
    high_score = 21
    total_score_dealer = 0
    total_score_player = 0
    want_to_play = True

    if game == "y":
        total_score_dealer = sum(dealer(card_list, dealer_empty_list))
        total_score_player = sum(player(card_list, player_empty_list))
        print("\n")

    else:
        print("Please enter valid input of 'y' or 'n'.")

    while want_to_play:
        ask_user = input("Type 'y' to get another card, type 'n' to pass : ").lower()

        if ask_user == "y":
            dealercards = random.choice(card_list)
            dealer_empty_list.append(dealercards)
            total_dealer_score = sum(dealer_empty_list)
            print(f"Dealer's current cards : {dealer_empty_list}")
            print(f"Dealer's current score : {total_dealer_score}")
            total_score_dealer = total_dealer_score
            # print(f"Total score of dealer {total_score_dealer}")
            print("\n")

            playercards = random.choice(card_list)
            player_empty_list.append(playercards)
            total_player_score = sum(player_empty_list)
            print(f"Player's current cards : {player_empty_list}")
            print(f"Player's current score : {total_player_score}")
            total_score_player = total_player_score
            # print(f"Total score player {total_score_player}")
            print("\n")

            if total_score_dealer or total_score_player > high_score:
                want_to_play = False
                if total_score_dealer > high_score:
                    print(f"Player wins with score {total_score_player}, dealer score went over 21.")

                elif total_score_player > high_score:
                    print(f"Dealer wins with score {total_score_dealer}, player score went over 21.")

            # removed for loop here and only went with the while loop since
            # i was using the len and range which caused issues if i selected y
            # more than once.

            # for dealercards in range(len(dealer_empty_list)):
            #     dealercards = random.choice(card_list)
            #     dealer_empty_list.append(dealercards)
            #     total_dealer_score = sum(dealer_empty_list)
            #     print(f"Dealer's current cards : {dealer_empty_list}")
            #     print(f"Dealer's current score : {total_dealer_score}")
            #     total_score_dealer = total_dealer_score
            #     print(f"Total score of dealer {total_score_dealer}")
            #
            # for playercards in range(len(player_empty_list) - 1):
            #     playercards = random.choice(card_list)
            #     player_empty_list.append(playercards)
            #     total_player_score = sum(player_empty_list)
            #     print(f"Player's current cards : {player_empty_list}")
            #     print(f"Player's current score : {total_player_score}")
            #     total_score_player = total_player_score
            #     print(f"Total score player {total_score_player}")

                # if total_score_player > high_score:
                #     print(total_score_player)
                #     print(f"Player score {total_score_player}, player loses")
                #     want_to_play = False
        else:
            if total_score_dealer <= high_score and total_score_player <= high_score:
                if total_score_dealer > total_score_player and total_score_dealer < high_score:
                    print(f"Dealer's score : {total_score_dealer}, Dealer wins!!!")

                elif total_score_player > total_score_dealer and total_score_player < high_score:
                    print(f"Player's score : {total_score_player}, Player wins!!!")
            else:
                print("Game over. Thank you for playing")
            want_to_play = False


# blackjack()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealerlist = []
playerlist = []
game_start = input("Would you like to play a game of blackjack? Type 'y' or 'n': ").lower()

blackjack(cards, game_start, dealerlist, playerlist)









