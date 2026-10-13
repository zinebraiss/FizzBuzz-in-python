import argparse


def fizzbuzz2(count: int, fizz: str, buzz: str, fizzbuzz: str) -> list[str]:
    outputs = []
    for i in range(1, count + 1):
        if i % 3 == 0 and i % 5 == 0:
            outputs.append(fizzbuzz)
        elif i % 3 == 0:
            outputs.append(fizz)
        elif i % 5 == 0:
            outputs.append(buzz)
        else:
            outputs.append(str(i))
    return outputs


def main() -> int:
    # Create an empty rule book for my program's command-line interface
    parser = argparse.ArgumentParser(description='FizzBuzz')

    #adding the arguments
    parser.add_argument("--count", type=int, default=100)
    parser.add_argument("--fizz", type=str, default="Fizz")
    parser.add_argument("--buzz", type=str, default="Buzz")
    parser.add_argument("--fizzbuzz", type=str, default="FizzBuzz")

    # Récupération des arguments
    args = parser.parse_args()

    results = fizzbuzz2(count=args.count,fizz=args.fizz,buzz=args.buzz, fizzbuzz=args.fizzbuzz)


    for item in results:
        print(item)

    return 0


if __name__ == "__main__":
    main()