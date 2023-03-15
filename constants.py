#Эти константы желательно не трогать
instructions = ["[", "]", "<", ">", "+", "-", "."] #Инструкции BrainFuck без ","
children = 2

#А эти можно трогать с радостью
populationSize = 10
minProgramSize = 10
maxProgramSize = 1000
mutationRate = 0.01
errorScore = 1 #какой фитнесс у программы, которая выдаёт ошибку
lengthPenalty = 0.001 #ругаемся на то, что программа слишком большая
maxBufSize = 255 #максимальный размер ленты
maxCycle = 1000
charSize = 255
