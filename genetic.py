import interpreter
import constants
import random
import generation

def getFitness(program, result):
    try:
        output = interpreter.interpret(program)
    except SyntaxError:
        return constants.errorScore/interpreter.countBrackets(program)
    except RuntimeError:
        return constants.errorScore
    except OverflowError:
        return constants.errorScore
    if output == False:
        return constants.errorScore
    max_score = len(result) * constants.charSize
    score = 0
    for i in range(max([len(result),len(output)])):
        try:
            score += abs(ord(output[i])-ord(result[i]))
        except IndexError:
            score += constants.charSize
    score += (len(program)*constants.lengthPenalty)
    return max_score - score 

def getScores(programs, result):
    scores = []
    for i in programs:
        scores.append(getFitness(i, result))
    return scores

def getBest(programs,scores):
    return programs[scores.index(max(scores))]

def getWorstIndex(scores):
    return scores.index(min(scores))

def getParent(programs,scores,otherParent):
    chances = []
    totalScore = sum(scores)
    randValue = random.random()-0.001
    prevChance = 0
    for i in range(constants.populationSize):
        chances.append(scores[i]/totalScore + prevChance)
        if chances[i] >= randValue and programs[i] != otherParent:
            return programs[i]
        prevChance = chances[i]
    return programs[0]


def getMutation(newProgram): #издеваемся над ребёнком
    i = 0
    newProgram = str(newProgram)
    maxPos = len(newProgram)
    while i < maxPos:
        if constants.mutationRate >= random.random():
            mutationType = random.randint(1, 3)
            if mutationType == 1:
                newProgram =generation.mutateInstruction(newProgram,i)
            elif mutationType == 2:
                newProgram = generation.addInstruction(newProgram)
                maxPos = len(newProgram)
            elif mutationType == 3:
                newProgram = generation.removeInstruction(newProgram,i)
                maxPos  = len(newProgram)
        i+=1
    return newProgram

#Now Playing: Yello - Oh Yeah
def breed(program1, program2):
    program1 = str(program1)
    program2 = str(program2)
    r = random.random()
    crossover1 = int(len(program1)*r)
    crossover2 = int(len(program2)*r)
    return [generation.optimize(getMutation(program1[:crossover1]+program2[crossover2:])),generation.optimize(getMutation(program2[:crossover2]+program1[crossover1:]))]