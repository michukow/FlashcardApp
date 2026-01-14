import json

class Flashcard:
    def __init__(self,side1,side2):
        self.side1=side1
        self.side2=side2

    def to_dict(self):
        return self.__dict__

def add_flashcard():
    while True:
        try:
            side1=input("Insert first side of the flashcard [foreign or word to learn]: ")
            if side1=="":
                print("The flashcard can not be empty.")
                continue
            break
        except ValueError:
            print("An error occured. Try again!")

    while True:
        try:
            side2=input("Insert second side of the flashcard [native or explanation]: ")
            if side2=="":
                print("The flashcard can not be empty.")
                continue
            break
        except ValueError:
            print("An error occured. Try again!")

    flashcard=Flashcard(side1,side2)

    try:
        with open("flashcard.json","r",encoding="utf-8") as file:
            data=json.load(file)
            if not data:
                print("No flashcard yet.")
    except FileNotFoundError:
        print("File not found.")

    data.append(flashcard.to_dict())

    with open("flashcard.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)

    print(f"Flashcard added successfully!")

def show_all():
    try:
        with open("flashcard.json","r",encoding="utf-8") as file:
            data=json.load(file)
            if not data:
                print("No flashcard yet.")

            print("Showing all your flashcards...")
            for i,f in enumerate(data,start=1):
                flashcard=Flashcard(f["side1"],f["side2"])
                print(f"{i}. {f["side1"]} - {f["side2"]}")

    except FileNotFoundError:
        print("File not found.")

def delete():
    try:
        with open("flashcard.json","r",encoding="utf-8") as file:
            data=json.load(file)

        if not data:
            print("No flashcards yet.")
            return

        for i,f in enumerate(data,start=1):
            flashcard=Flashcard(f["side1"],f["side2"])
            print(f"{i}. {f["side1"]} - {f["side2"]}")

        while True:
            try:
                i=int(input("Enter number of flashcard to delete "))-1
                if i<0 or i>=len(data):
                    print("Invalid number. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")

        removed=data.pop(i)

        with open("flashcard.json","w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)

        print("Flashcard was removed.")

    except FileNotFoundError:
        print("File not found.")

def main():
    while True:
        print()
        print("=== FLASHCARD ===")
        print("1. Add flashcard")
        print("2. Show all flashcards")
        print("3. Delete specific flashcard")
        print("4. Exit")
        print()

        choice=str(input("Choose option: "))

        if choice=="1":
            add_flashcard()
        elif choice=="2":
            show_all()
        elif choice=="3":
            delete()
        elif choice=="4":
            break
        else:
            print("Invalid option. Try again! \n")

if __name__ == "__main__":
    main()