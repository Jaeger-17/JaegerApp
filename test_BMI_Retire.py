import unittest
from BodyMassIndex import BodyMassIndex
from RetirementSavings import RetirementSavings


class TestApp(unittest.TestCase):

    def test_create_BMI(self):
        userBMI = BodyMassIndex(5, 10, 150)
        self.assertEqual(userBMI.feet, 5)
        self.assertEqual(userBMI.inches, 10)
        self.assertEqual(userBMI.weight, 150)

    def test_check_numbers(self):
        userBMI1 = BodyMassIndex(5, 10, 150)
        userBMI2 = BodyMassIndex(-5, 10, 150)
        userBMI3 = BodyMassIndex(5, -10, 150)
        userBMI4 = BodyMassIndex(5, 10, -150)
        userBMI5 = BodyMassIndex(0, 0, 150)

        try:
            userBMI1.check_numbers()
        except ValueError:
            self.fail("unexpected exception")

        with self.assertRaises(ValueError):
            userBMI2.check_numbers()
        with self.assertRaises(ValueError):
            userBMI3.check_numbers()
        with self.assertRaises(ValueError):
            userBMI4.check_numbers()
        with self.assertRaises(ValueError):
            userBMI5.check_numbers()

    def test_conv_to_kg(self):
        userBMI1 = BodyMassIndex(0, 0, 150)
        userBMI2 = BodyMassIndex(0, 0, 0)

        self.assertEqual(userBMI1.conv_to_kg(), 67.5)
        self.assertEqual(userBMI2.conv_to_kg(), 0)

    def test_conv_to_inches(self):
        userBMI1 = BodyMassIndex(5, 10, 0)
        userBMI2 = BodyMassIndex(5, 0, 0)
        userBMI3 = BodyMassIndex(0, 10, 0)
        userBMI4 = BodyMassIndex(0, 0, 0)

        self.assertEqual(userBMI1.conv_to_inches(), 70)
        self.assertEqual(userBMI2.conv_to_inches(), 60)
        self.assertEqual(userBMI3.conv_to_inches(), 10)
        self.assertEqual(userBMI4.conv_to_inches(), 0)

    def test_conv_to_meters(self):
        userBMI1 = BodyMassIndex(5, 10, 0)
        userBMI2 = BodyMassIndex(0, 0, 0)

        self.assertEqual(userBMI1.conv_to_meters(), 1.75)
        self.assertEqual(userBMI2.conv_to_meters(), 0)

    def test_calculate_BMI(self):
        userBMI1 = BodyMassIndex(5, 10, 150)
        userBMI2 = BodyMassIndex(6, 3, 120)

        self.assertEqual(userBMI1.calculate_bmi(), 22.0)
        self.assertEqual(userBMI2.calculate_bmi(), 15.4)

    def test_give_result(self):
        userBMI_1 = BodyMassIndex(5, 10, 100)
        userBMI_2 = BodyMassIndex(5, 10, 126)
        userBMI_3 = BodyMassIndex(5, 10, 150)
        userBMI_4 = BodyMassIndex(5, 10, 170)
        userBMI_5 = BodyMassIndex(5, 2, 150)
        userBMI_6 = BodyMassIndex(5, 10, 204)
        userBMI_7 = BodyMassIndex(5, 2, 175)

        self.assertEqual(userBMI_1.give_result(), "You are underweight.")
        self.assertEqual(userBMI_2.give_result(), "Your weight is normal.")
        self.assertEqual(userBMI_3.give_result(), "Your weight is normal.")
        self.assertEqual(userBMI_4.give_result(), "You are overweight.")
        self.assertEqual(userBMI_5.give_result(), "You are overweight.")
        self.assertEqual(userBMI_6.give_result(), "You are obese.")
        self.assertEqual(userBMI_7.give_result(), "You are obese.")

    def test_create_retire(self):
        userRetire = RetirementSavings(25, 65000, 10, 500000)
        self.assertEqual(userRetire.age, 25)
        self.assertEqual(userRetire.salary, 65000)
        self.assertEqual(userRetire.percent, 10)
        self.assertEqual(userRetire.goal, 500000)

    def test_check_numbers_r(self):
        userRetire1 = RetirementSavings(25, 65000, 10, 500000)
        userRetire2 = RetirementSavings(-25, 65000, 10, 500000)
        userRetire3 = RetirementSavings(25, -65000, 10, 500000)
        userRetire4 = RetirementSavings(25, 65000, -10, 500000)
        userRetire5 = RetirementSavings(25, 65000, 10, -500000)

        try:
            userRetire1.check_numbers_r()
        except ValueError:
            self.fail("unexpected exception")

        with self.assertRaises(ValueError):
            userRetire2.check_numbers_r()
        with self.assertRaises(ValueError):
            userRetire3.check_numbers_r()
        with self.assertRaises(ValueError):
            userRetire4.check_numbers_r()
        with self.assertRaises(ValueError):
            userRetire5.check_numbers_r()

    def test_get_savings_per_year(self):
        userRetire1 = RetirementSavings(25, 65000, 10, 500000)
        userRetire2 = RetirementSavings(30, 100000, 5, 500000)
        userRetire3 = RetirementSavings(25, 0, 10, 500000)

        self.assertEqual(userRetire1.get_savings_per_year(), 8775)
        self.assertEqual(userRetire2.get_savings_per_year(), 6750)
        self.assertEqual(userRetire3.get_savings_per_year(), 0)

    def test_get_years_til_goal(self):
        userRetire1 = RetirementSavings(25, 65000, 10, 500000)
        userRetire2 = RetirementSavings(30, 100000, 5, 500000)
        userRetire3 = RetirementSavings(25, 0, 10, 500000)

        self.assertEqual(userRetire1.get_years_til_goal(), 57)
        self.assertEqual(userRetire2.get_years_til_goal(), 75)
        self.assertEqual(userRetire3.get_years_til_goal(), 100)

    def test_calculate_goal_age(self):
        userRetire1 = RetirementSavings(25, 65000, 10, 500000)
        userRetire2 = RetirementSavings(30, 100000, 5, 500000)
        userRetire3 = RetirementSavings(25, 0, 10, 500000)

        self.assertEqual(userRetire1.calculate_goal_age(), 82)
        self.assertEqual(userRetire2.calculate_goal_age(), 105)
        self.assertEqual(userRetire3.calculate_goal_age(), 125)

    def test_give_result_r(self):
        userRetire1 = RetirementSavings(25, 65000, 10, 500000)
        userRetire2 = RetirementSavings(30, 100000, 5, 500000)
        userRetire3 = RetirementSavings(25, 0, 10, 500000)

        self.assertEqual(userRetire1.give_result_r(), "You will retire at age 82.")
        self.assertEqual(userRetire2.give_result_r(), "You will not retire until you are 100 or older.")
        self.assertEqual(userRetire3.give_result_r(), "You will not retire until you are 100 or older.")


if __name__ == '__main__':
    unittest.main()
