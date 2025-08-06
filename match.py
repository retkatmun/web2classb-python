'''
color = "black"

match Color:

case "blue":
    print(color)
case "black":
    print(color)
case "green":
    print(color)
case _ "neutral":
    print(f"the is no match with: {color}")
'''

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")

