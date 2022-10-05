#Эти константы желательно не трогать
instructions = ["[", "]", "<", ">", "+", "-", "."] #Инструкции BrainFuck без ","
children = 2

#А эти можно трогать с радостью
populationSize = 10
minProgramSize = 10
maxProgramSize = 500
mutationRate = 0.01
errorScore = 1.0 #какой фитнесс у программы, которая выдаёт ошибку
lengthPenalty = 0.001 #ругаемся на то, что программа слишком большая
displayTime = 10000 #как часто показывать прогресс
maxBufSize = 255 #максимальный размер ленты
maxCycle = 255
charSize = 255