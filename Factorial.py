def FirstFactorial(num):

  # code goes here
  # first create the variable for storge the result in it.
  total = 1

  #create the loop for factorial 
  for number in range(2 , num + 1):
    # in every step multiple the number in last value
    total *= number

    # we want count for change the value in every step.
    number =+ 1


  return total

# keep this function call here 
print(FirstFactorial(input()))
