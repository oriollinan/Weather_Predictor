import sys
import math

class Groundhog:
    def __init__(self, period):
        self.values = []
        self.tendency = None
        self.tendency_switches = 0
        self.aberrations = [5]
        self.input = 0
        self.period_list = []
        self.period = period
        self.highest_value = None

    def get_highest_value(self):
        for temp in self.period_list:
            if (self.highest_value == None or self.highest_value < temp):
                self.highest_value = temp

    def check_highest_vale(self):
        i = 0
        while (i < self.period - 1):
            if (self.period_list[i] >= self.highest_value):
                return 1
            i = i + 1
        return 0

    def store_input(self, user_input, length):
        if user_input == "STOP":
            exit(0)
        self.input = float(user_input)
        if (length < self.period):
            self.period_list.insert(0, self.input)
            self.get_highest_value()
            # print(self.period_list)
        else:
            self.period_list.pop()
            self.period_list.insert(0, self.input)
            self.get_highest_value()
            # print(self.period_list)

    def get_variance(self, mean):
        i = 0
        variance = 0
        while (i < self.period - 1):
            variance += (self.period_list[i] - mean) ** 2
            i = i + 1
        variance /= (self.period - 1)
        return math.sqrt(variance)

    def get_mean(self, length):
        i = 0
        summatory = 0
        while (i < self.period - 1):
            summatory += self.period_list[i]
            i = i + 1
        mean = summatory / (self.period - 1)
        i = 0
        return mean

    def average_increase(self):
        if (self.check_highest_vale() == 1):
            increase = abs((self.period_list[self.period - 1] - self.highest_value) / (self.period - 1))
        else:
            increase = 0
        return increase

    def get_temp_evolution(self):
        evolution = (round((100 / self.period_list[self.period - 1]) * self.period_list[0]) - 100)
        return evolution

    def gather_data(self, length):
        if (length >= self.period - 1):
            variance = self.average_increase()
            evolution = self.get_temp_evolution()
            print("g={:.2f}        r={:.2f}       ".format(variance, evolution), end ='')
        else:

            print("g=nan        r=nan%       ", end ='')
        if (length >= self.period - 2):
            s = self.get_variance(self.get_mean(length))
            print('s={:.2f}'.format(s))
        else:
            print('s=nan')

    def loop(self):
        while True:
            user_input = input()
            length = len(self.period_list)
            self.store_input(user_input, length)
            self.gather_data(length)

def groundhog_init():
    groundhog = Groundhog(int(sys.argv[1]) + 1)
    groundhog.loop()

if __name__ == '__main__':
    groundhog_init()
