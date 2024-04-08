#Класс для объекта из артефакта
class ArtifactObject():
    def __init__(self, depth, edge, stimulation, studied, id):
        self.depth: int = depth
        self.edge: int = edge
        self.stimulation: str = stimulation
        self.studied: bool = studied
        self.id: int = id
    def info(self):
        print("ArtifactObject: "+ str(self.id))
        print("depth: " + str(self.depth))
        print("edge: " + str(self.edge))
        print("stimulation: " + self.stimulation)
        print("studied: " + str(self.studied))
        print("\n")

#Класс артефакта
class Artifact():
    def __init__(self, id):
        self.id = id
        self.depend = [[]] #Зависимости, т.е. объекты этого артефакта
    def addObject(self, obj: ArtifactObject):
        if len(self.depend) <= obj.depth: #Если объект не помещается, то увеличиваем массив артефакта
            self.depend.append([])
        self.depend[obj.depth].append(obj)
        obj.studied = True
    def info(self):
        for d in self.depend:
            for e in d:
                #Вывод кол-ва неисследованных объектов
                if e.depth == 0:
                    if len(self.depend[0]) < e.edge:
                        print(str(e.edge - len(self.depend[0]))+" new research \n")
                else:
                    if len(self.depend[e.depth]) < (e.edge - 1):
                        print(str()+" new research \n")
