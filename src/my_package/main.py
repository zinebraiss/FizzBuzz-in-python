import argparse

# version version of the code without using the flags or the argument of the rule book
def fizzbuzz(count: int = 100) -> None:
    for i in range(1, count + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


# exeuter ce block seulement si ce fichier est lancer directement :
# if __name__ == "__main__":
#  fizzbuzz()


# Create an empty rule book for my program's command-line interface
parser = argparse.ArgumentParser(description='FizzBuzz')

# add the arguments
parser.add_argument("--count", type=int, default=100)
parser.add_argument("--fizz", type=str, default="Fizz")
parser.add_argument("--buzz", type=str, default="Buzz")
parser.add_argument("--fizzbuzz", type=str, default="FizzBuzz")

# check the rules and defining the variables
args = parser.parse_args()


def fizzbuzz2() -> None:
    output = ""
    for i in range(1, args.count + 1):
        if i % 3 == 0 and i % 5 == 0:
            output += args.fizzbuzz
            output += "\n"
        elif i % 3 == 0:
            output += args.fizz
            output += "\n"
        elif i % 5 == 0:
            output += args.buzz
            output += "\n"
        else:
            output += str(i)
            output += "\n"

    print(output)



if __name__ == "__main__":
  fizzbuzz2()

print(args.count, "arguments")