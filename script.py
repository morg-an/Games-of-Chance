import random

money = 100
coin_count = 0
chohan_count = 0

#Coin Flip
def coin_flip(call, bet):
  result = random.randint(1, 2)
  #winning situations
  if call.lower() == "heads" and result == 1:
    print("Win with heads")
    return bet
  elif call.lower() == "tails" and result == 2:
    print("Win with tails")
    return bet
  #losing situations
  elif call.lower() == "heads" and result == 2:
    print("Lose with heads")
    return bet*-1
  elif call.lower() == "tails" and result == 1:
    print("Lose with tails")
    return bet*-1
  #catch-all
  else:
    print("Error.")

def roll_chohan(call, bet):
  print("Your guess: " + call)
  print("Your bid: " + str(bet))
  #roll 2 dice and find remainder
  roll1 = random.randint(1, 6)
  print("Roll 1: ", roll1)
  roll2 = random.randint(1, 6)
  print("Roll 2: ", roll2)
  total = roll1+roll2
  remainder = total%2
  isEven = True if remainder==0 else False
  print("Is even: " + str(isEven))
  if isEven == True and call.lower() == "even":
    return bet
  elif isEven == True and call.lower() == "odd":
    return bet * -1
  if isEven == False and call.lower() == "even":
    return bet * -1
  if isEven == False and call.lower() == "odd":
    return bet

#Call your game of chance functions here
print("Coin Flip Starting Balance: " + str(money))
while coin_count < 5:
  money += coin_flip("Tails", 10)
  print("Running balance: " + str(money))
  coin_count += 1

print("Chohan Starting Balance: " + str(money))
while chohan_count < 2:
  money += roll_chohan("Odd", 5)
  print("Running balance: " + str(money))
  chohan_count += 1
