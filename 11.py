import itertools
import copy
import cProfile

class Facility:
    facilityStates = []

    def __init__(self, floors, elevatorAt):
        self.floors = floors
        self.elevatorAt = elevatorAt
        self.processed = False
        self.next = []

    def __str__(self):
        return '{} 4 {}\n{} 3 {}\n{} 2 {}\n{} 1 {}'.format(
            '*' if self.elevatorAt == 3 else ' ',
            self.floors[3],
            '*' if self.elevatorAt == 2 else ' ',
            self.floors[2],
            '*' if self.elevatorAt == 1 else ' ',
            self.floors[1],
            '*' if self.elevatorAt == 0 else ' ',
            self.floors[0]
        )

    __repr__ = __str__

    def __cmp__(self, other):
        if self.elevatorAt != other.elevatorAt: return 1

        selfPairs = {}
        for x in range(len(self.floors)):
            for item in self.floors[x]:
                if item.element not in selfPairs:
                    selfPairs[item.element] = [x]
                else:
                    selfPairs[item.element].append(x)
        selfPairs = [sorted(x) for x in selfPairs.values()]


        otherPairs = {}
        for x in range(len(other.floors)):
            for item in other.floors[x]:
                if item.element not in otherPairs:
                    otherPairs[item.element] = [x]
                else:
                    otherPairs[item.element].append(x)
        otherPairs = [sorted(x) for x in otherPairs.values()]

        if sorted(selfPairs) != sorted(otherPairs): return 1




        # generalizedSelf = [[], [], [], []]
        # selfMap = {}
        # count = 1
        # for x in range(len(self.floors)):
        #     for item in self.floors[x]:
        #         letter = item.element[0]
        #         if letter not in selfMap:
        #             selfMap[letter] = count
        #             count += 1
        #         generalizedSelf[x].append(str(selfMap[letter]) + item.type[0])
        #     generalizedSelf[x].sort()
        #
        # generalizedOther = [[], [], [], []]
        # otherMap = {}
        # count = 1
        # for x in range(len(other.floors)):
        #     for item in other.floors[x]:
        #         letter = item.element[0]
        #         if letter not in otherMap:
        #             otherMap[letter] = count
        #             count += 1
        #         generalizedOther[x].append(str(otherMap[letter]) + item.type[0])
        #     generalizedOther[x].sort()
        #
        # if generalizedSelf != generalizedOther: return 1

        # print self
        # for floor in generalizedSelf:
        #     print floor
        # print '\n\n'


        # for x in range(len(self.floors)):
        #     if len(self.floors[x]) != len(other.floors[x]): return 1
        #     for item in self.floors[x]:
        #         if item not in other.floors[x]: return 1

        return 0


    def isSafe(self):
        for floor in self.floors:
            if not Item.isSafe(floor): return False

        return True

    def isDuplicate(self):
        for facility in Facility.facilityStates:
            if self == facility: return True

        return False

    def getElevators(self):
        twoCombos = [list(x) for x in list(itertools.combinations(self.floors[self.elevatorAt], 2))]
        oneCombos = [[x] for x in self.floors[self.elevatorAt]]
        twoElevators = []
        oneElevators = []

        goDown = False
        for x in range(self.elevatorAt):
            if len(self.floors[x]) > 0:
                goDown = True

        for combo in twoCombos:
            if not Item.isSafe(combo): continue

            if self.elevatorAt < 3:
                twoElevators.append(Elevator(combo, 'up'))
            if goDown:
                if self.elevatorAt > 0:
                    twoElevators.append(Elevator(combo, 'down'))

        for combo in oneCombos:
            if not Item.isSafe(combo): continue

            if self.elevatorAt < 3:
                oneElevators.append(Elevator(combo, 'up'))
            if goDown:
                if self.elevatorAt > 0:
                    oneElevators.append(Elevator(combo, 'down'))

        return {'one': oneElevators, 'two': twoElevators}

    def getNewState(self, elevator):
        newFloor = self.elevatorAt + 1 if elevator.direction == 'up' else self.elevatorAt - 1
        newState = Facility(copy.deepcopy(self.floors), newFloor)

        for item in elevator.contents:
            newState.floors[self.elevatorAt].remove(item)
            newState.floors[newFloor].append(item)
        return newState

    def process(self, endFacility):
        validElevators = self.getElevators()

        twoUp = False

        for elevator in validElevators['two']:
            newState = self.getNewState(elevator)
            if newState.isSafe() and not newState.isDuplicate():
                self.next.append(newState)
                Facility.facilityStates.append(newState)
                if elevator.direction =='up':
                    twoUp = True

        for elevator in validElevators['one']:
            newState = self.getNewState(elevator)
            if newState.isSafe() and not newState.isDuplicate():
                if elevator.direction == 'up' and twoUp:
                    continue
                self.next.append(newState)
                Facility.facilityStates.append(newState)

        self.processed = True

    @staticmethod
    def hasUnprocessedStates():
        unprocessedStates = filter(lambda x: not x.processed, Facility.facilityStates)
        return len(unprocessedStates) > 0

    @staticmethod
    def getUnprocessedFacility():
        for facility in Facility.facilityStates:
            if not facility.processed:
                return facility

        return None

class Elevator:
    def __init__(self, contents, direction):
        self.contents = contents
        self.direction = direction

    def __str__(self):
        string = '{}:'.format(self.direction)
        for item in self.contents:
            string += ' {}'.format(item)
        return string

    __repr__ = __str__

    def isSafe(self):
        return Item.isSafe(self.contents)

class Item:
    def __init__(self, element, type):
        self.element = element
        self.type = type

    def __str__(self):
        return '{} {}'.format(self.element, self.type)

    __repr__ = __str__

    def __eq__(self, other):
        return self.element == other.element and self.type == other.type

    @staticmethod
    def isSafe(items):
        generators = filter(lambda x: x.type == 'generator', items)
        if len(generators) == 0: return True
        microchips = filter(lambda x: x.type == 'microchip', items)
        for microchip in microchips:
            matchingGenerator = filter(lambda x: x.type == 'generator' and x.element == microchip.element, items)
            if not matchingGenerator: return False

        return True

def doStuff():
    # Build Graph

    # startFacility = Facility([
    #     [Item('hydrogen', 'microchip'), Item('lithium', 'microchip')],
    #     [Item('hydrogen', 'generator')],
    #     [Item('lithium', 'generator')],
    #     []
    # ], 0)
    #
    # endFacility = Facility([
    #     [],
    #     [],
    #     [],
    #     [Item('hydrogen', 'microchip'), Item('lithium', 'microchip'), Item('hydrogen', 'generator'), Item('lithium', 'generator')]
    # ], 3)

    # startFacility = Facility([
    #     [Item('plutonium', 'generator'), Item('strontium', 'generator')],
    #     [Item('plutonium', 'microchip'), Item('strontium', 'microchip'), Item('t', 'microchip'), Item('t', 'generator')],
    #     [Item('promethium', 'generator'), Item('promethium', 'microchip')],
    #     []
    # ], 0)
    #
    # endFacility = Facility([
    #     [],
    #     [],
    #     [],
    #     [Item('plutonium', 'generator'), Item('strontium', 'generator'), Item('plutonium', 'microchip'), Item('strontium', 'microchip'), Item('promethium', 'generator'), Item('promethium', 'microchip'), Item('t', 'generator'), Item('t', 'microchip')]
    # ], 3)

    # startFacility = Facility([
    #     [Item('thulium', 'generator'), Item('thulium', 'microchip'), Item('plutonium', 'generator'), Item('strontium', 'generator')],
    #     [Item('plutonium', 'microchip'), Item('strontium', 'microchip')],
    #     [Item('promethium', 'generator'), Item('promethium', 'microchip'), Item('ruthenium', 'generator'), Item('ruthenium', 'microchip')],
    #     []
    # ], 0)
    #
    # endFacility = Facility([
    #     [],
    #     [],
    #     [],
    #     [Item('thulium', 'generator'), Item('thulium', 'microchip'), Item('plutonium', 'generator'), Item('strontium', 'generator'), Item('plutonium', 'microchip'), Item('strontium', 'microchip'), Item('promethium', 'generator'), Item('promethium', 'microchip'), Item('ruthenium', 'generator'), Item('ruthenium', 'microchip')]
    # ], 3)

    startFacility = Facility([
        [Item('elerium', 'generator'), Item('elerium', 'microchip'), Item('dilithium', 'generator'), Item('dilithium', 'microchip'), Item('thulium', 'generator'), Item('thulium', 'microchip'), Item('plutonium', 'generator'), Item('strontium', 'generator')],
        [Item('plutonium', 'microchip'), Item('strontium', 'microchip')],
        [Item('promethium', 'generator'), Item('promethium', 'microchip'), Item('ruthenium', 'generator'), Item('ruthenium', 'microchip')],
        []
    ], 0)

    endFacility = Facility([
        [],
        [],
        [],
        [Item('elerium', 'generator'), Item('elerium', 'microchip'), Item('dilithium', 'generator'), Item('dilithium', 'microchip'), Item('thulium', 'generator'), Item('thulium', 'microchip'), Item('plutonium', 'generator'), Item('strontium', 'generator'), Item('plutonium', 'microchip'), Item('strontium', 'microchip'), Item('promethium', 'generator'), Item('promethium', 'microchip'), Item('ruthenium', 'generator'), Item('ruthenium', 'microchip')]
    ], 3)

    Facility.facilityStates.append(startFacility)

    while Facility.hasUnprocessedStates():
        Facility.getUnprocessedFacility().process(endFacility)

    print len(Facility.facilityStates)
    print endFacility in Facility.facilityStates


    # Find fewest steps

    def findFewestSteps(facilityStates, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path

        shortestPath = None
        for state in start.next:
            if state not in path:
                newPath = findFewestSteps(facilityStates, state, end, path)
                if newPath:
                    if not shortestPath or len(newPath) < len(shortestPath):
                        shortestPath = newPath
        return shortestPath


    path = findFewestSteps(Facility.facilityStates, startFacility, endFacility)
    if path: print len(path) - 1

#
# cProfile.run('doStuff()')
import time
start = time.time()
doStuff()
print time.time() - start
