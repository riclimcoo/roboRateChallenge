import unittest
import wages

class TestRoboWages(unittest.TestCase):

    def test_wages(self):
        defaultRate = {
            "standardDay": {
                "start": "07:00:00",
                "end": "23:00:00",
                "value": 20
            },
            "standardNight": {
                "start": "23:00:00",
                "end": "07:00:00",
                "value": 25
            },
            "extraDay": {
                "start": "07:00:00",
                "end": "23:00:00",
                "value": 30
            },
            "extraNight": {
                "start": "23:00:00",
                "end": "07:00:00",
                "value": 35
            }
        }
        testCases = [
            {
                "shift":{
                    "start":    "2038-01-01T20:15:00",
                    "end":      "2038-01-02T08:15:00",
                },
                "expected": 19650
            },
            {
                "shift":{
                    "start":    "2038-01-11T07:00:00",
                    "end":      "2038-01-17T19:00:00",
                },
                "expected": 202200
            },
            {
                "shift":{
                    "start":    "2038-01-01T20:15:00",
                    "end":      "2038-01-02T04:16:00",
                },
                "expected": 13725
            },
            {
                "shift":{
                    "start":    "2038-01-01T20:15:00",
                    "end":      "2038-01-02T05:16:00",
                },
                "expected": 13760
            },
        ]

        for test in testCases:
            print(f"Given input: \n{test}")
            wage = wages.wages(test["shift"], defaultRate)
            print(f"Output: {wage}")
            assert wage == test["expected"]
            print("Success!\n")

if __name__ == '__main__':
    unittest.main()