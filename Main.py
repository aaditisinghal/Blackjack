cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
want_to_play=input("Do you want to play blackjack?y/n?").lower()
user_hand=[]
if want_to_play=="y":

      print('''
                .------.            _     _            _    _            _    
                |A_  _ |.          | |   | |          | |  (_)          | |   
                |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
                | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
                |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
                '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\/
                      |  \/ K|                           _/ |                
                      '------'                          |__/           
            ''')
      import random
      random_cards1= random.choice(cards)
      random_cards2= random.choice(cards)
      user_cards=user_hand.append(random_cards1,random_cards1)
      current_score= 
      print(f" your cards: {user_hand}")
      print(f"Currentscore: {current_score}")

      computer_firstcard= random.choice(cards)
      computer_secondcard= random.choice(cards)
      computer_sum= computer_firstcard+computer_secondcard
      print(f"Computer first card: {computer_firstcard}")

      another_card=input("Type 'y' to get another card, type 'n' to pass:")

      while another_card=="y":
            random_cards3=random.choice(cards)
            print(f"next card{random_cards3}")
            sum3=current_score+random_cards3
            print(f"final sum:{sum3}")
            another_card=input("Type 'y' to get another card, type 'n' to pass:")

      while another_card=="n":
            if (sum3> computer_sum or current_score>computer_sum) and sum3<=21:
                  print("you won!")
            elif (sum3<computer_sum or current_score<computer_sum) and computer_sum<=21:
                  print("you lose!")
            elif sum3==computer_sum or current_score==computer_sum:
                  print("draw")
