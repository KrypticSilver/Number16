

# gets the number from the user
userInput = int(input("Input a number: "))

# squares the number
squareNumber = userInput**2

print(f"The number squared is: {squareNumber}")

# splits the number into individual integers
listNumber = [i for i in str(squareNumber)]
print(f"The number squared as a list is {listNumber}")

numberLength = len(listNumber)
print("The number of digits is: " + str(numberLength))

splitNums = []

if numberLength == 2:
    splitNums.append(listNumber[0])
    splitNums.append(listNumber[1])

else:
    splitNums.append(listNumber[0:(numberLength // 2)])
    splitNums.append(listNumber[(numberLength // 2):])

print(splitNums)

list1 = splitNums[]