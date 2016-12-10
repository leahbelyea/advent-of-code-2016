import re

with open('input/10.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# input = [
#     'value 5 goes to bot 2',
#     'bot 2 gives low to bot 1 and high to bot 0',
#     'value 3 goes to bot 1',
#     'bot 1 gives low to output 1 and high to bot 0',
#     'bot 0 gives low to output 2 and high to output 0',
#     'value 2 goes to bot 2'
# ]


# Output is considered to be a bot with no ability to give chips away
class Bot:
    bots = []

    def __init__(self, id, low, high):
        self.id = id
        self.low = low
        self.high = high
        self.chips = []
        self.comparisons = []

    def __str__(self):
        return '{} gives low to {} and high to {} and has chips {}'.format(self.id, self.low, self.high, self.chips)

    def addChip(self, chip):
        self.chips.append(int(chip))

    def canMove(self):
        hasChips = len(self.chips) >= 2
        hasLow = self.low
        hasHigh = self.high
        return hasChips and hasLow and hasHigh

    def getLowChip(self):
        if len(self.chips) < 1 : return None
        self.chips.sort()
        return self.chips[0]

    def getHighChip(self):
        if len(self.chips) < 1 : return None
        self.chips.sort()
        return self.chips[-1]

    def move(self):
        lowChip = self.getLowChip()
        highChip = self.getHighChip()
        self.chips.remove(lowChip)
        self.chips.remove(highChip)
        lowBot = Bot.getBot(self.low)
        highBot = Bot.getBot(self.high)
        lowBot.addChip(lowChip)
        highBot.addChip(highChip)

    def willCompare(self):
        chips = self.chips
        chips.sort()
        if len(chips) < 1: return []
        return [chips[0], chips[-1]]

    @staticmethod
    def getBot(id):
        for bot in Bot.bots:
            if bot.id == id:
                return bot
        return None

    @staticmethod
    def printBots():
        for bot in Bot.bots:
            print bot

    @staticmethod
    def printBotHoldings():
        bots = Bot.bots
        bots.sort(key=lambda x: x.id)
        for bot in bots:
            print '{}: {}'.format(bot.id, bot.chips)

    @staticmethod
    def botsCanMove():
      for bot in Bot.bots:
          if bot.canMove():
              return True
      return False

output = {}
comparison = [17, 61]

for instruction in filter(lambda x: x.find('value') < 0, input):
    [bot, low, high] = re.findall('((?:bot|output) [0-9]+)', instruction)
    Bot.bots.append(Bot(bot, low, high))

    if low.find('output') >= 0:
        Bot.bots.append(Bot(low, None, None))
    if high.find('output') >= 0:
        Bot.bots.append(Bot(high, None, None))

for instruction in filter(lambda x: x.find('value') >= 0, input):
    [chip, bot] = re.findall('[0-9]+', instruction)
    botId = 'bot {}'.format(bot)
    bot = Bot.getBot(botId)
    bot.addChip(chip)

# Part 1

def getBotCompared(comparison):
    while True:
        for bot in Bot.bots:
            if bot.willCompare() == comparison:
                return bot
            if bot.canMove():
                bot.move()

bot = getBotCompared(comparison)
print bot.id.replace('bot ', '')


# Part 2

def doWork():
    while Bot.botsCanMove():
        for bot in Bot.bots:
            if bot.canMove():
                bot.move()

doWork()
output0Value = Bot.getBot('output 0').getLowChip()
output1Value = Bot.getBot('output 1').getLowChip()
output2Value = Bot.getBot('output 2').getLowChip()
print output0Value * output1Value * output2Value
