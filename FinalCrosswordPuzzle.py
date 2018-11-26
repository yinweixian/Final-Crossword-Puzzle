#Hayden Whitney
#11/18
#A trivia word search game
import random

#global score
#score = 0

#defining functions to allow for random later
def tq1():
  q = "The order of operations that python follows is this acronym. "
  ans = "PEMDAS"
  ansLen = len(ans)
  return q, ans

def tq2():
  q = "A number that is either a positive or negative whole number is an: "
  ans = "INTEGER"
  ansLen = len(ans)
  return q, ans

def tq3():
  q = "A floating decimal point number is a: "
  ans = "FLOAT"
  ansLen = len(ans)
  return q, ans

def tq4():
  q = "A _ stores a series of values that can be accessed through indexing or loops. "
  ans = "LIST"
  ansLen = len(ans)
  return q, ans

def tq5():
  q = "Code with human readable descriptions that can help document design decisions and has no affect on the execution of the code are called: "
  ans = "COMMENT"
  ansLen = len(ans)
  return q, ans

def tq6():
  q = "A named sequence of statements that will perform some useful operation is: "
  ans = "FUNCTION"
  ansLen = len(ans)
  return q, ans

def tq7():
  q = "Symbols that perform mathematical operations (+, -, *, /) are known as: "
  ans = "OPERATORS"
  ansLen = len(ans)
  return q, ans

def tq8():
  q = "A _ statement tests a specified condition."
  ans = "IF"
  ansLen = len(ans)
  return q, ans

def tq9():
  q = "A _ allows you to access a particular part in a list. "
  ans = "SLICE"
  ansLen = len(ans)
  return q, ans

def tq10():
  q = "Names that store data are called: "
  ans = "VARIABLES"
  ansLen = len(ans)
  return q, ans
 
q_list = [tq1(), tq2(), tq3(), tq4(), tq5(), tq6(), tq7(), tq8(), tq9(), tq10()]

puzzle = "NNOITCNUFSHXZINTEGEROTNEMMOCHOOQTVPTSILTZVAZECILSAEDOQMWCVBRBKLVDWXNUEAVFLAVGHMPXJFISLCCIOSELBAIRAVS"
polished_puzzle = """    0 1 2 3 4 5 6 7 8 9
  
0   N N O I T C N U F S
1   H X Z I N T E G E R
2   O T N E M M O C H O
3   O Q T V P T S I L T
4   Z V A Z E C I L S A
5   E D O Q M W C V B R
6   B K L V D W X N U E
7   A V F L A V G H M P
8   X J F I S L C C I O
9   S E L B A I R A V S
"""

def wordPuzzle():
  i = 0
  foundword=""
  while i < ansLen:
    index=ans[i]
    index=int(index)
    foundword=foundword+puzzle[index+1]


def credits():
  print("\nThis game was made possible by Matthew Walker, Hayden Whitney, and users like you. Thank you.")
  return_to_menu = input("\nPress the enter key to return to menu.\n")
  menu()

def game():
  z = 0
  score = 0
  while z <= 10:
    q, ans = random.choice(q_list)
    user_ans = input(q)
  
    if user_ans.upper() != ans:
      print("you got it wrong")
      score = score - 10

    if user_ans.upper() == ans:
      print("you got it right!")
      score = score + 10

    #wordPuzzle()
    z = z+1
  


def score():
  score = 0
  






def tutorial():
    print("""
Welcome to the word search game. finding the words is difficult
so listen up. when the word search puzzle comes up you will enter
the cordinates of each letter like your playing battleship. 
""")
    return_to_menu = input("\nPress the enter key to return to menu.\n")
    menu()










    
def menu():
  print("[0] Tutorial")
  print("[1] Play")
  print("[2] Score")
  print("[3] Credits")
  choice = input("\nEnter the [#] of your choice: ")
  if choice == "0":
    tutorial()
  elif choice == "1":
    game()
  elif choice == "2":
    score()
  elif choice == "3":
    credits()
  else:
    print("Please enter a valid choice.")
    menu()
    
menu()
