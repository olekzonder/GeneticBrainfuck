import random
import constants
#Составление программ и всё, что с этим связано
def getRandomInstruction():
    return constants.instructions[random.randint(0, len(constants.instructions)-1)]

def addInstruction(program):
    program = str(program)
    if len(program) + 1 < constants.maxProgramSize:
        program += getRandomInstruction()
    return program
    
def removeInstruction(program, index):
    index = int(index)
    program = list(program)
    if len(program) - 2 > constants.minProgramSize:
        program.pop(index)
    return ''.join(program)

def mutateInstruction(program, index):
    program = str(program)
    index = int(index)
    program = list(program)
    instruction = getRandomInstruction()
    if program[index] == instruction:
        mutateInstruction(program, index)
    else:
        program[index] = getRandomInstruction()
    return ''.join(program)

def optimize(program):
    sum = 0
    optimized = ''
    for i in range(len(program)):
        if program[i] == "[":
            sum += 1
        elif program[i] == "]":
            sum -= 1
        else:
            if sum < 0:
                for i in range(sum,0):
                    optimized  += '['
            elif sum >0:
                for i in range(0,sum):
                    optimized += ']'
        sum = 0
        optimized += program[i]
    return optimized

def createProgram():
    program = ''
    programSize = random.randint(constants.minProgramSize, constants.maxProgramSize)
    for i in range(programSize):
        program += getRandomInstruction()
    program = optimize(program)
    return program

def createPopulation():
    programs = []
    for i in range(constants.populationSize):
        programs.append(createProgram())
    return programs