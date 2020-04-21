#5.2 Write a program that repeatedly prompts a user for intege
 #   r numbers until the user enters 'done'. Once 'done' is entered, print out the largest an
  #  d smallest of the numbers. If the user enters anything other than a valid number catch it w
   # ith a try/except and put out an appropriate message and ignore the
   # number. Enter 7, 2, bob, 10, and 4 and match the output below.
largest = None
smallest = None
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        num = int(number)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)

