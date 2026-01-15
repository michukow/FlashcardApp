import json
import random

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

def update():
    try:
        with open("flashcard.json","r",encoding="utf-8") as file:
            data=json.load(file)

        if not data:
            print("No flashcard yet.")
            return

        for i,f in enumerate(data,start=1):
            flashcard=Flashcard(f["side1"],f["side2"])
            print(f"{i}. {f["side1"]} - {f["side2"]}")
            

        while True:
            try:
                i=int(input("Enter number of flashcard to edit: "))-1
                if i<0 or i>=len(data):
                    print("Invalid number. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")

        old=data[i]

        new_side1=input("Update first side of flashcard: ")
        if new_side1!="":
            try:
                old["side1"]=new_side1
            except ValueError:
                print("An error occured.")
                return

        new_side2=input("Update second side of flashcard: ")
        if new_side2!="":
            try:
                old["side2"]=new_side2
            except ValueError:
                print("An error occured.")
                return

        with open("flashcard.json","w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)

        print("Flashcard updated.")

    except FileNotFoundError:
        print("File not found.")   

def learn():
    print("Learning...")
    good=0
    motivation_good=["Well done!","Just do it!", "You've got this!","Congratulation!","Good job!"]
    motivation_bad=["Bad!","Remember this!","Error!","Repeat that!"]
    flashcards_to_learn={}
    try:
        with open("flashcard.json","r",encoding="utf-8") as file:
            data=json.load(file)

            if not data:
                print("No flashcard yet")
                return

            for f in data:
                flashcard=Flashcard(f["side1"],f["side2"])
                flashcards_to_learn[f["side1"]]=f["side2"]

    except FileNotFoundError:
        print("File not found.")

    while flashcards_to_learn:
        side1,side2=random.choice(list(flashcards_to_learn.items()))
        answer=input(f"{side1}: ")

        if answer.lower()==side2.lower():
            good+=1
            print(random.choice(motivation_good))
            print(f"{side1} - {side2}\n")
            flashcards_to_learn.pop(side1)

        else:
            print(random.choice(motivation_bad))
            print(f"{side1} - {side2}\n")

    print("Wow! You've done it!")   

def main():
    while True:
        print()
        print("=== FLASHCARD ===")
        print("1. Add flashcard")
        print("2. Show all flashcards")
        print("3. Delete specific flashcard")
        print("4. Update specific flashcard")
        print("5. Repeat everything")
        print("6. Exit")
        print()

        choice=str(input("Choose option: "))

        if choice=="1":
            add_flashcard()
        elif choice=="2":
            show_all()
        elif choice=="3":
            delete()
        elif choice=="4":
            update()
        elif choice=="5":
            learn()
        elif choice=="6":
            break
        else:
            print("Invalid option. Try again! \n")

if __name__ == "__main__":
    main()