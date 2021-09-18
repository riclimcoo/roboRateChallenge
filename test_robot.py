import unittest
import robot

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        testCases = [
            {
                "start":    "2038-01-01T20:15:00",
                "end":      "2038-01-02T08:15:00",
                "expected": 19650
            },
            {
                "start":    "2038-01-11T07:00:00",
                "end":      "2038-01-17T19:00:00",
                "expected": 202200
            },
            {
                "start":    "2038-01-01T20:15:00",
                "end":      "2038-01-02T04:16:00",
                "expected": 13725
            },
            {
                "start":    "2038-01-01T20:15:00",
                "end":      "2038-01-02T05:16:00",
                "expected": 13760
            },
        ]

        for test in testCases:
            print(f"Given input: \n{test}")
            wage = robot.wages_iso(test["start"],test["end"])
            print(f"Output: {wage}")
            assert wage == test["expected"]
            print("Success!\n")

if __name__ == '__main__':
    unittest.main()