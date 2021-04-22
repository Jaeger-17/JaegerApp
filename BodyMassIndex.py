class BodyMassIndex:

    def __init__(self, givenFeet, givenInches, givenWeight):
        #declares variables for the class
        self.feet = givenFeet
        self.inches = givenInches
        self.weight = givenWeight
        return

    def check_numbers(self):
        #ensures non-negative values and no divide by 0
        if self.feet < 0 or self.inches < 0 or self.weight < 0:
            raise Exception
        elif self.feet == 0 and self.inches == 0:
            raise Exception
        return

    def conv_to_kg(self):
        #converts pounds to kilograms
        return float(self.weight) * 0.45

    def conv_to_inches(self):
        #converts feet and inches to just inches
        return (self.feet * 12) + self.inches

    def conv_to_meters(self):
        #converts inches to meters
        return float(self.conv_to_inches()) * 0.025

    def calculate_BMI(self):
        #calculates BMI based on metric units
        return round(self.conv_to_kg() / (self.conv_to_meters() * self.conv_to_meters()), 1)

    def give_result(self):
        #gives result (underweight, normal, overweight, etc.) based on BMI
        userBmi = self.calculate_BMI()
        if userBmi < 18.5:
            return "You are underweight."
        elif userBmi >= 18.5 and userBmi < 25:
            return "Your weight is normal."
        elif userBmi >= 25 and userBmi < 30:
            return "You are overweight."
        else:
            return "You are obese."
