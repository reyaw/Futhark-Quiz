import copy
import random

original_names = ["Fehu", "Urus", "Thurisaz", "Ansuz", "Raido", "Kaun", "Gebo", "Wunjo", "Hagalaz", "Naudiz", "Isaz",
                  "Jera", "Eihwaz", "Pertho", "Algiz", "Sowulo", "Teiwaz", "Berkana", "Ehwaz", "Mannaz", "Laguz",
                  "Ingwaz", "Dagaz", "Othila"]
original_means = ["Wealth", "Power", "Troll", "Mouth", "Road", "Torch", "Talent", "Joy", "Havoc", "Night", "Freeze",
                  "Harvest", "Strength", "Hidden", "Defence", "Sun", "Warrior", "Birth", "Wheel", "Human",
                  "Lagoon", "Living", "Dawn", "Estate"]
original_letters = ["F", "U/V", "Th", "A", "R", "K/C", "G", "W", "H", "N", "I", "J", "Y", "P", "Z/X", "S", "T", "B",
                    "E", "M",
                    "L", "Ing", "D", "O"]

original_runes = ["16A0", "16A2", "16A6", "16A8", "16B1","16B4", "16B7", "16B9", "16BA", "16BE", "16C1", "16C3", "16C7",
                  "16C8", "16C9", "16CA", "16CF", "16D2", "16D6", "16D7", "16DA", "16DC", "16DE", "16DF"]

answer_key = {"A": 0, "B": 1, "C": 2, "D": 3, }


class Rune:

    def __init__(self, number):
        self.name = original_names[number]
        self.meaning = original_means[number]
        self.letter = original_letters[number]

    def __str__(self):
        return f"{self.name}\n{self.letter}\n{self.meaning}"

    def __getitem__(self):
        return {"Name": self.name, "Letter": self.letter, "Meaning": self.meaning}

    def get_image(self):
        return str(self.name + ".png")

    def get_name(self):
        return self.name

    def get_meaning(self):
        return self.meaning

    def get_letter(self):
        return self.letter


class Quiz:

    def __init__(self):
        self.questions = []
        for i in range(24):
            self.questions.append(Question(i))

    def __getitem__(self, question):
        return self.questions[question]

    def __str__(self):
        return self.questions

    def random_questions(self):
        random.shuffle(self.questions)

    def run(self):
        for question in self.questions:
            question.ask()


class Question:

    def __init__(self, question_number):

        self.user_answer = ""
        self.current_rune = Rune(question_number)
        self.options = []

        # Adds the letter of the rune in question to the multiple choice options
        # Ensures at least one of the answers will be correct
        self.options.append(self.current_rune.get_letter())

        # Populates the 3 remaining options with random letters from original_letters
        self.answer_letter_list = copy.deepcopy(original_letters)
        random.shuffle(self.answer_letter_list)
        self.i = 0
        while len(self.options) < 4:

            if self.answer_letter_list[self.i] not in self.options:
                self.options.append(self.answer_letter_list[self.i])
            self.i += 1

        # Shuffles the options
        random.shuffle(self.options)

    def __str__(self):
        return (
            f"The rune {self.current_rune.get_name()} corresponds to which English letter?\n"
            f"A: {self.options[0]}\n"
            f"B: {self.options[1]}\n"
            f"C: {self.options[2]}\n"
            f"D: {self.options[3]}\n"
        )

    def ask(self):

        print(self)

        self.user_answer = str.upper(input("Your answer: "))
        try:
            self.user_answer = answer_key[self.user_answer]
            if self.options[self.user_answer] == self.current_rune.get_letter():
                print("\nYou are correct!\n")

            else:
                print("I'm sorry, that's incorrect")

        except KeyError:
            print("Please choose A, B, C, or D")


test = Quiz()

# test.run()

print(u"\u16A0")
