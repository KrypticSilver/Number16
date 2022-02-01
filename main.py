def listToInt(array):
  integer = 0
  for e, i in enumerate(reversed(array)):
    integer += (int(i) * (10 ** e))

  return integer

# gets the number from the user
userInput = int(input("Input a number: "))

# squares the number
squareNumber = userInput**2

print(f"The number squared is: {squareNumber}")

# splits the number into individual integers
listNumber = [i for i in str(squareNumber)]

numberLength = len(listNumber)

splitNums = []

if numberLength == 2:
    splitNums.append(listNumber[0])
    splitNums.append(listNumber[1])

else:
    splitNums.append(listNumber[0:(numberLength // 2)])
    splitNums.append(listNumber[(numberLength // 2):])

result = 0
for i in splitNums:
  result += listToInt(i)


print(f"{listToInt(splitNums[0])} added to {listToInt(splitNums[1])} is [{result}]")
if userInput == result:
  print("This is a kaprekar number")

else:
  print("This is not a kaprekar number")
  