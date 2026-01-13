class Flashcard:
    def __init__(self,side1,side2):
        self.side1=side1

    def to_dict(self):
        return self.__dict__

def main():
    while True:
        print()
        print("=== FLASHCARD ===")
        print("1. Add flashcard")
        print("2. Exit")
        print()

        choice=str(input("Choose option: "))

        if choice=="1":
            add()
        elif chocie=="2":
            break
        else:
            print("Invalid option. Try again! \n")

if __name__ == "__main__":
    main()