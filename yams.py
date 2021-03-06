##
## EPITECH PROJECT, 2020
## yams
## File description:
## yams
##

#!/usr/bin/python3 python3

import sys

class classYams():
    def __init__(self, currentDies, combinationWanted):
        self.clearedList = []
        self.foundElemWanted = []
        self.die = self.listStrToListInt(currentDies)
        self.combination = combinationWanted
        if (self.die == [] or self.gestError() == 84):
            exit(84)

    def permutation(self, nbPermutation):
        totalPermutation = 1
        i = 1
        while (i <= nbPermutation):
            totalPermutation *= i
            i += 1
        return totalPermutation

    def calcCombination(self, nbCombination, nbElem):
        return (self.permutation(nbElem) / 
        (self.permutation(nbCombination) *
        self.permutation(nbElem - nbCombination)))

    def preCheck(self, key):
        found = 0
        if (key == "pair"):
            for elem in self.die:
                if (elem == self.combination[key][0]):
                    found += 1
                else:
                    self.clearedList.append(elem)
            if (found >= 2):
                print("Chances to get a {} pair: 100.00%".format(self.combination[key][0]))
                exit(0)
        elif (key == "three"):
            for elem in self.die:
                if (elem == self.combination[key][0]):
                    found += 1
                else:
                    self.clearedList.append(elem)
            if (found >= 3):
                print("Chances to get a {} three-of-a-kind: 100.00%".format(self.combination[key][0]))
                exit(0)
        elif (key == "four"):
            for elem in self.die:
                if (elem == self.combination[key][0]):
                    found += 1
                else:
                    self.clearedList.append(elem)
            if (found >= 4):
                print("Chances to get a {} four-of-a-kind: 100.00%".format(self.combination[key][0]))
                exit(0)
        elif (key == "full"):
            for elem in self.die:
                if ((elem == self.combination[key][0] or elem == self.combination[key][1]) and self.foundElemWanted.count(elem) < 3):
                    self.foundElemWanted.append(elem)
                    found += 1
                else:
                    self.clearedList.append(elem)
            if (found == 5):
                print("Chances to get a {} full of {}: 100.00%".format(self.combination[key][0], self.combination[key][1]))
                exit(0)
        elif (key == "straight"):
            for elem in self.die:
                if (elem not in self.foundElemWanted and ((elem == 1 and 6 not in self.foundElemWanted) or
                (elem == 6 and 1 not in self.foundElemWanted) or (elem != 1 and elem != 6))):
                    self.foundElemWanted.append(elem)
                else:
                    self.clearedList.append(elem)
            if (len(self.foundElemWanted) == 5 and
            ((self.combination[key][0] == 1 and 1 in self.foundElemWanted and 6 not in self.foundElemWanted) or
            (self.combination[key][0] == 6 and 6 in self.foundElemWanted and 1 not in self.foundElemWanted) or
            (self.combination[key][0] != 1 and self.combination[key][0] != 6 and
            ((1 in self.foundElemWanted and 6 not in self.foundElemWanted) or (1 not in self.foundElemWanted and 6 in self.foundElemWanted))))):
                print("Chances to get a {} straight: 100.00%".format(self.combination[key][0]))
                exit(0)
        elif (key == "yams"):
            for elem in self.die:
                if (elem == self.combination[key][0]):
                    found += 1
                else:
                    self.clearedList.append(elem)
            if (found == 5):
                print("Chances to get a {} yams: 100.00%".format(self.combination[key][0]))
                exit(0)
        else:
            exit(84)
        return False


    def calcBinomial(self, p, nbCombination, nbElem):
        return (self.calcCombination(nbCombination, nbElem) *
        pow(p, nbCombination) * pow((1 - p), nbElem - nbCombination))

    def calcFull(self, nbFace, nbCombination, nbElem):
        return (self.calcCombination(nbCombination, nbElem) / pow(nbFace, nbElem))

    def gameBoard(self):
        key = list(self.combination.keys())[0]
        self.preCheck(key)
        if (key == "pair"):
            print("Chances to get a {} pair: {}%".format(self.combination[key][0], 
            round((self.calcBinomial(1 / 6, 2 - (len(self.die) - len(self.clearedList)), len(self.clearedList)) +
            self.calcBinomial(1 / 6, 3 - (len(self.die) - len(self.clearedList)), len(self.clearedList)) +
            self.calcBinomial(1 / 6, 4 - (len(self.die) - len(self.clearedList)), len(self.clearedList))+
            self.calcBinomial(1 / 6, 5 - (len(self.die) - len(self.clearedList)), len(self.clearedList))) * 100, 2)))
        if (key == "three"):
            print("Chances to get a {} three-of-a-kind: {}%".format(self.combination[key][0],
            round((self.calcBinomial(1 / 6, 3 - (len(self.die) - len(self.clearedList)), len(self.clearedList)) +
            self.calcBinomial(1 / 6, 4 - (len(self.die) - len(self.clearedList)), len(self.clearedList)) + 
            self.calcBinomial(1 / 6, 5 - (len(self.die) - len(self.clearedList)), len(self.clearedList))) * 100, 2)))
        if (key == "four"):
            print("Chances to get a {} four-of-a-kind: {}%".format(self.combination[key][0], round((self.calcBinomial(1 / 6, 4 - (len(self.die) - len(self.clearedList)), len(self.clearedList)) +
            (self.calcBinomial(1 / 6, 5 - (len(self.die) - len(self.clearedList)), len(self.clearedList)))) * 100, 2)))
        if (key == "full"):
            print("Chances to get a {} full of {}: {}%".format(self.combination[key][0], self.combination[key][1],
            round((self.calcFull(6, 3 - (len(self.die) - len(self.clearedList)), len(self.clearedList)) * 100), 2)))
        if (key == "straight"):
            print(self.clearedList, self.die)
            print(5 - (len(self.die) - len(self.clearedList)), len(self.clearedList))
            print("Chances to get a {} straight: {}%".format(self.combination[key][0],
            round((self.calcFull(6, 5 - (len(self.die) - len(self.clearedList)), len(self.clearedList)) * 100), 2)))
        if (key == "yams"):
            print("Chances to get a {} yams: {}%".format(self.combination[key][0],
            round(self.calcBinomial(1 / 6, 5 - (len(self.die) - len(self.clearedList)), len(self.clearedList)) * 100, 2)))

    def gestError(self):
        listCombination = [ "pair", "three", "four", "full", "straight", "yams"]
        parseCombination = self.combination.split("_")
        try:
            listCasted = self.listStrToListInt(parseCombination[1:])
            if (listCasted == []):
                return 84
            self.combination = {parseCombination[0]: listCasted}
            for face in self.die:
                if (face < 0 or face > 6):
                    return 84
        except:
            return 84
        nbrArgs = len(self.combination[parseCombination[0]])
        if (parseCombination[0] not in listCombination or 
        (nbrArgs == 2 and parseCombination[0] != "full") or
        (nbrArgs != 2 and parseCombination[0] == "full")):
            return 84
        for face in self.combination[parseCombination[0]]:
            if (face < 1 or face > 6):
                return 84
        return 0

    def listStrToListInt(self, toConvert):
        converted = []
        try:
            for numStr in toConvert:
                if (len(numStr) != len(str(numStr))):
                    return []
                converted.append(int(numStr))
        except:
            return []
        return converted

def help():
    file = open("README.md", "r")
    print(file.read())

def main(argv):
    lengthArgs = len(argv)
    if (lengthArgs != 2 and lengthArgs != 7 or
    (lengthArgs == 2 and argv[1] != "-h")):
        return 84
    if (lengthArgs == 2):
        help()
    else:
        game = classYams(argv[1:6], argv[6])
        game.gameBoard()
    return 0

exit(main(sys.argv))
