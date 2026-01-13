import json

class Flashcard:
    def __init__(self,side1,side2):
        self.side1=side1
        self.side2=side2

    def to_dict(self):
        return self.__dict__

    def info(self):
        return self.side1, self.side2

def add_flashcard():
    while True:
        try:
            side1=input("Insert first side of the flashcard: ")
            if side1=="":
                print("The flashcard can not be empty.")
                continue
            break
        except ValueError:
            print("An error occured. Try again!")

    while True:
        try:
            side2=input("Insert second side of the flashcard: ")
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
            if not isinstance(data,list):
                data=[]
    except FileNotFoundError:
        data=[]

    data.append(flashcard.to_dict())

    with open("flashcard.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)

    print(f"Flashcard {flashcard.info()} added successfully!")

def main():
    while True:
        print()
        print("=== FLASHCARD ===")
        print("1. Add flashcard")
        print("2. Exit")
        print()

        choice=str(input("Choose option: "))

        if choice=="1":
            add_flashcard()
        elif chocie=="2":
            break
        else:
            print("Invalid option. Try again! \n")

if __name__ == "__main__":
    main()