from Dice import Dice

def main():
  trialsNumber = 1000000
  dice1 = Dice(6)
  dice2 = Dice(6)
  dice3 = Dice(6)
  sucessNumber = 0
  for _ in range(trialsNumber):
    dicesSum = dice1.throw() + dice2.throw() + dice3.throw()
    if ((dicesSum <= 15) and (dicesSum >= 10)):
      sucessNumber+= 1
      
  print ("Sum of three dices probability to be between 10 and 15 including: " + str(sucessNumber/trialsNumber))

if __name__ == "__main__":
  main()
