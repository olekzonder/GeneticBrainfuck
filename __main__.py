import sys
import constants
import genetic
import interpreter
import generation
import threading
import time
import logging
def checkInput(goal):
    for i in goal:
        if ord(i) > 255:
            print("Юникод не поддерживается")
            exit()

def outputResult(generations,bestProgram):
        generations = int(generations)
        bestProgram = str(bestProgram)
        if generations == 0: 
            print("Начало работы")
        else:
            output = interpreter.interpret(bestProgram)
            output = output if output != False else "Код выводит ошибку..."
            print("Лучшая программа: %s" %output)
            print("Код: %s" %bestProgram)

def bestProgramExists(program,programs):
    if program in programs:
        return True
    else:
        return False

def replacePrograms(parent, child, programs):
    for i in range(constants.populationSize):
        if parent == programs[i]:
            programs[i] = child
            break
    return programs
print("Genetic BrainFuck (3 ОКТ 2022)")
if len(sys.argv) >1:
    if len(sys.argv) == 2:
        goal = sys.argv[1]
        print("Введена строка: %s" %goal)
    else:
        print("Введено слишком много аргументов! Используйте кавычки для объединения нескольких слов!")
        exit()
else:
    goal = str(input("Введите строку: "))
checkInput(goal)
programs = generation.createPopulation()
scores = []
bestProgram = ''
generations = 0
matchFound = False
while True:
    scores = genetic.getScores(programs, goal)
    bestProgram = genetic.getBest(programs,scores)
    parent1 = genetic.getParent(programs,scores,'')
    parent2 = genetic.getParent(programs,scores,parent1)
    children = genetic.breed(parent1,parent2)
    programs = replacePrograms(parent1, children[0], programs)
    programs = replacePrograms(parent2, children[1], programs)
    if not bestProgramExists(bestProgram,programs):
        programs[genetic.getWorstIndex(scores)] = bestProgram
    if generations % constants.displayTime == 0:
        outputResult(generations, bestProgram)
        if interpreter.interpret(bestProgram) == goal and matchFound == False:
            matchFound == True
            print("---ПОКОЛЕНИЕ %d -----------------------------------------------" % generations)
            print("БЫЛ ПОЛУЧЕН ПРАВИЛЬНЫЙ ОТВЕТ: %s" %interpreter.interpret(bestProgram))
            print("Код:", bestProgram)
            print("---------------------------------------------------------------")
            f = open("geneticbrainfuck.txt","w")
            f.write(bestProgram)
            f.close()
            print("Полученная программа записана в файл geneticbrainfuck.txt")
            answer = str(input("Желаете продолжить? (y/n): "))
            if answer.lower() != 'y':
                exit()
            else:
                matchFound = True
    generations += 1