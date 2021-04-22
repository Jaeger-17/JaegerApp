class BodyMassIndex:

    def __init__(self, givenFeet, givenInches, givenWeight):
        self.inches = givenInches
        self.feet = givenFeet
        self.weight = givenWeight

    def check_numbers(self):
        if self.feet < 0 or self.inches < 0 or self.weight < 0:
            raise ValueError
        elif self.feet == 0 and self.inches == 0:
            raise ValueError
        return

    def conv_to_kg(self):
        return float(self.weight) * 0.45

    def conv_to_inches(self):
        return (self.feet * 12) + self.inches

    def conv_to_meters(self):
        return float(self.conv_to_inches()) * 0.025

    def calculate_bmi(self):
        kilos = float(self.conv_to_kg())
        meters = ((float(self.feet) * 12) + float(self.inches)) * 0.025
        result = (kilos / (meters * meters))
        return round(result, 1)

    def give_result(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "You are underweight."
        elif (bmi >= 18.5 and bmi < 25):
            return "Your weight is normal."
        elif (bmi >= 25 and bmi < 30):
            return "You are overweight."
        else:
            return "You are obese."
