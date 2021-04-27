from django.db import models

# Create your models here.
import random

original_names = ["Fehu", "Urus", "Thurisaz", "Ansuz", "Raido", "Kaunaz", "Gebo", "Wunjo", "Hagalaz", "Naudiz", "Isaz",
         "Jera", "Eihwaz", "Pertho", "Algiz", "Sowulo", "Teiwaz", "Berkana", "Ehwaz", "Mannaz", "Laguz", "Inguz",
         "Dagaz", "Othila"]
original_means = ["Wealth", "Power", "Troll", "Mouth", "Road", "Torch", "Talent", "Joy", "Havoc", "Night", "Freeze",
         "Harvest", "Strength", "Hidden", "Defence", "Sun", "Warrior", "Birth", "Wheel", "Human",
         "Lagoon", "Living", "Dawn", "Estate"]
original_letters = ["F", "U/V", "Th", "A", "R", "K/C", "G", "W", "H", "N", "I", "J", "Y", "P", "Z/X", "S", "T", "B", "E", "M",
        "L", "Ing", "D", "O"]


class Rune(models.Model):

    def __init__(self, number):
        self.name = original_names[number]
        self.meaning = original_means[number]
        self.letter = original_letters[number]

    def __str__(self):
        return f"{self.name}\n{self.letter}\n{self.meaning}"

    def __getitem__(self):
        return {"Name": self.name, "Letter": self.letter, "Meaning": self.meaning}

    def getimage(self):
        return str(self.name + ".png")

    def checklet(self, let=""):
        l = str(let).upper()
        if l in self.letter:
            return True
        else:
            return False

    def checkname(self, na=""):
        n = str(na).upper()
        if n == self.name:
            return True
        else:
            return False

    def checkmean(self, me=""):
        m = str(me).upper()
        if m in self.meaning:
            return True
        else:
            return False


class Runes:

    def __init__(self):
        self.runes = []
        for i in range(24):
            self.runes.append(Rune(i, i, i))

    def randomRunes(self):
        random.shuffle(self.runes)
        return self.runes

    def __getitem__(self, rune):
        return self.runes[rune]

    def __str__(self):
        return self.runes