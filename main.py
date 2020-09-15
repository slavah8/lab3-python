#Author: Slava Hlushko vqh5091@psu.edu
#Collaborator Jennifer Lee jml7322@psu.edu
#Collaborator Ronit Ramnarayan rvr5507@psu.edu
#Collaborator Lukas Cowell lfc5378@psu.edu
#Section 11
#Breakout 9


def sum_n(n):
  if n == 0:
    return 0
  else:
    return n + sum_n(n-1)


def print_n(s,n):
  if n == 0:
    return
  else:
    print(f"{s}")
    return print_n(s,n-1)






def run():
  askInt = int(input("Enter an int: "))
  print(sum_n(askInt))
  askString = (input("Enter a string: "))
  print_n(askString, askInt)
  

if __name__ == "__main__": 
  run()







