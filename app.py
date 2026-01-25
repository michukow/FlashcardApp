import json
import random
from datetime import datetime

class Flashcard:
    def __init__(self,side1,side2,date):
        self.side1=side1
        self.side2=side2
        self.date=date

    def to_dict(self):
        return self.__dict__

def add_flashcard():
    while True:
        try:
            side1=input("Insert first side of the flashcard [native]: ")
            if side1=="":
                print("The flashcard can not be empty.")
                continue
            break
        except ValueError:
            print("An error occured. Try again!")

    while True:
        try:
            side2=input("Insert second side of the flashcard [new word]: ")
            if side2=="":
                print("The flashcard can not be empty.")
                continue
            break
        except ValueError:
            print("An error occured. Try again!")

    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    flashcard=Flashcard(side1,side2,date)

    try:
        with open("flashcard.json","r",encoding="utf-8") as file:
            data=json.load(file)

    except FileNotFoundError:
        print("File not found.")
        data=[]

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
                print(f"{i}. {f['side1']} - {f['side2']}")

    except FileNotFoundError:
        print("File not found.")
        data=[]

def delete():
    try:
        with open("flashcard.json","r",encoding="utf-8") as file:
            data=json.load(file)

        if not data:
            print("No flashcards yet.")
            return

        for i,f in enumerate(data,start=1):
            print(f"{i}. {f['side1']} - {f['side2']}")

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
        data=[]

def update():
    try:
        with open("flashcard.json","r",encoding="utf-8") as file:
            data=json.load(file)

        if not data:
            print("No flashcard yet.")
            return

        for i,f in enumerate(data,start=1):
            print(f"{i}. {f['side1']} - {f['side2']}")
            

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

        date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        old["date"]=date

        with open("flashcard.json","w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)

        print("Flashcard updated.")

    except FileNotFoundError:
        print("File not found.")   
        data=[]

def exam_mode():
    good=0
    max_flashcards=0
    motivation_good=["Well done!","Just do it!", "You've got this!","Congratulation!","Good job!"]
    motivation_bad=["Bad!","Remember this!","Error!","Nice try!","Repeat that!"]
    flashcards_exam={}
    
    try:
        with open("flashcard.json","r",encoding="utf-8") as file:
            data=json.load(file)

            if not data:
                print("No flashcard yet")
                return

            for f in data:
                flashcards_exam[f["side1"]]=f["side2"]
                max_flashcards=len(flashcards_exam)

    except FileNotFoundError:
        print("File not found.")
        data=[]

    while flashcards_exam:
        side1,side2=random.choice(list(flashcards_exam.items()))
        answer=input(f"{side1}: ")

        if answer.lower()==side2.lower():
            good+=1
            print(random.choice(motivation_good))
            print(f"{side1} - {side2}\n")
            flashcards_exam.pop(side1)

        else:
            print(random.choice(motivation_bad))
            print(f"Correct answer: {side1} - {side2}\n")

    print("Wow! You've done it!")
    print(f"Total: {max_flashcards}") 
    print(f"Correct: {good}")
    print(f"Wrong: {max_flashcards-good}")

def learn_mode():
    learning_pile=[]
    try:
        with open("flashcard.json","r",encoding="utf-8") as file:
            data=json.load(file)

            if not data:
                print("No flashcard yet")
                return

            for f in data:
                flashcard=Flashcard(f["side1"],f["side2"],f["date"])
                learning_pile.append(flashcard)

    except FileNotFoundError:
        print("File not found.")
        data=[]

    while learning_pile:

        card=learning_pile.pop(0)
        side1=card.side1
        side2=card.side2

        print(f"{side1}")
        input("Press ENTER to show answer...")

        print(f"{side2}")

        answer=input(f"Do you know the answer? [y/n]: ").lower()

        while answer not in ("y","n"):
            answer=input("Type 'y' or 'n': ").lower()

            if answer=="n":
                learning_pile.append(card)
        print()

    try:
        with open("streak.json","r",encoding="utf-8") as file:
            streak_data=json.load(file)

        if not streak_data:
            print("No flashcard yet.")
            return

        streak=streak_data["streak"]
        streak_date=streak_data["streak_date"]

    except FileNotFoundError:
        print("File not found.")
        data=[]
        streak=0
        streak_date=None

    today=datetime.today().date()

    if streak_date:
        diff=(today-datetime.strptime(streak_date,"%Y-%m-%d").date()).days

        if diff==1:
            streak+=1   
        elif diff==0:
            pass               
        else:
            streak=1
    else:
        streak=1

    with open("streak.json","w",encoding="utf-8") as file:
        json.dump(
            {
                "streak":streak,
                "streak_date":today.strftime("%Y-%m-%d")
            },
            file,indent=4,ensure_ascii=False
        )

    print("\nWow! You've repeated every flashcard.")
    print(f"Current streak: {streak}")

def main():
    while True:
        print()
        print("=== FLASHCARD ===")
        print("1. Add flashcard")
        print("2. Show all flashcards")
        print("3. Delete specific flashcard")
        print("4. Update specific flashcard")
        print("5. Learn mode")
        print("6. Exam")
        print("7. Exit")
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
            learn_mode()
        elif choice=="6":
            exam_mode()
        elif choice=="7":
            break
        else:
            print("Invalid option. Try again! \n")

if __name__ == "__main__":
    main()