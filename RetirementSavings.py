import math


class RetirementSavings:

    def __init__(self, givenAge=20, givenSalary=40000, givenPercent=1, givenGoal=1000000):
        self.age = givenAge
        self.salary = givenSalary
        self.percent = givenPercent
        self.goal = givenGoal

    def calculate_retirement(self):
        spy = (float(self.salary) * (float(self.percent) / 100)) * 1.35
        years = math.ceil(float(self.goal) / spy)
        return (float(self.age) + years)

    def give_retirement_age(self):
        retirementAge = self.calculate_retirement()
        if retirementAge < 100:
            return ("You will retire at age " + str(retirementAge) + "\n")
        else:
            return "You will probably not be able to reach your goal.\n"
            