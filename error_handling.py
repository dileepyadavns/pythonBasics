
try :
    for i in ['1','2','3']:
      print(i**2)
except:
    print("please provide integers") 
finally:
    print("squres of each element in list")   



x=1
y=0

try:
  print(x/y)
except:
  print("please provide  valid denominator")  




def ask():
  while True:
    try:
      n=int(input())
    except:
      print("please provide valid number")
      continue
    else:
      print("you are right")
      break    



ask()

