
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
if __name__ == "__main__":
    fizzbuzz()
