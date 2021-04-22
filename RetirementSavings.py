import math


class RetirementSavings:

    def __init__(self, givenAge, givenSalary, givenPercent, givenGoal):
        self.age = givenAge
        self.salary = givenSalary
        self.percent = givenPercent
        self.goal = givenGoal
    
    def check_numbers_r(self):
        if self.age < 0 or self.salary < 0 or self.percent < 0 or self.goal < 0 or self.percent > 100:
            raise Exception
        else:
            return

    def get_savings_per_year(self):
        return (float(self.salary) * (float(self.percent)/100)) * 1.35

    def get_years_til_goal(self):
        if self.salary == 0:
            return 100
        else:
            return math.ceil(float(self.goal) / self.get_savings_per_year())

    def calculate_goal_age(self):
        return self.get_years_til_goal() + int(self.age)

    def give_result_r(self):
        retireAge = self.calculate_goal_age()
        if retireAge < 100:
            return "You will retire at age " + str(retireAge) + "."
        else:
            return "You will not retire until you are 100 or older."
