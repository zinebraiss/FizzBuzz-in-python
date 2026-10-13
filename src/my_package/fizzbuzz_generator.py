import argparse
from typing import Generator

#generator function, calling it doesn't run its code immediately, instead it returns a generator that we can iterate over
#en bref un générator envoie element par element uniquement à la demande, niveau mémoire : il stock rien car il calcule les  juste à la volé
#this return is like Generator[yieldtype, SendType, ReturnType]
#Le sendtype definie le type de donné envoyé au generator
#le return type représente le type de valeur renvoyé par l'instruction return, dans mon cas c'est none car j'ai pas de return
#there is also Iterator[YieldType] , asyncGenerator[] what does it do?

def fizzbuzz(count: int, fizz: str, buzz: str, fizzbuzz: str) -> Generator[list[str], None, None]:

    for i in range(1, count + 1):
        if i % 3 == 0 and i % 5 == 0:
            yield fizzbuzz
        elif i % 3 == 0:
            yield fizz
        elif i % 5 == 0:
          yield buzz
        else:
            yield str(i)



def main() -> int:
    # Create an empty rule book for my program's command-line interface
    parser = argparse.ArgumentParser(description="FizzBuzz")

    # adding the arguments
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--fizz", type=str, default="Fizz")
    parser.add_argument("--buzz", type=str, default="Buzz")
    parser.add_argument("--fizzbuzz", type=str, default="FizzBuzz")

    # Récupération des arguments
    args = parser.parse_args()

    results = fizzbuzz(
        count=args.count, fizz=args.fizz, buzz=args.buzz, fizzbuzz=args.fizzbuzz
    )

    for output in results:
        print(output)
    return 0


if __name__ == "__main__":
    main()
