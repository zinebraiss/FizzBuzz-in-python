import argparse
def fizzbuzz(count=100):
    for i in range(1, count + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

#exeuter ce block seulement si ce fichier est lancer directement :
#if __name__ == "__main__":
  #  fizzbuzz()


#Create an empty rule book for my program's command-line interface
parser = argparse.ArgumentParser(description='FizzBuzz')
#add the arguments
parser.add_argument("--count", type=int, default=100)

#check the rules and defining the variables
args = parser.parse_args()

for i in range(1, args.count + 1):
   output = ""
   if i % 3 == 0 and i % 5 == 0:
       output += "FizzBuzz "
   elif  i % 3 == 0:
       output += "Fizz "
   elif i % 5 == 0:
       output += "Buzz "
   print(output if output else i)



print(args.count)


