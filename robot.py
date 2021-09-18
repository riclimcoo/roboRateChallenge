import datetime

userIn = {
  "shift": {
    "start": "2038-01-01T20:15:00",
    "end": "2038-01-02T04:15:00"
  },
  "roboRate": {
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
}

rate = {
    "standard": {
        "dayRate":   userIn["roboRate"]["standardDay"]["value"],
        "nightRate": userIn["roboRate"]["standardNight"]["value"],
        "dayStart":  datetime.time.fromisoformat(userIn["roboRate"]["standardDay"]["start"]),
        "dayEnd":    datetime.time.fromisoformat(userIn["roboRate"]["standardDay"]["end"])
    },
    "weekend":{
        "dayRate":   userIn["roboRate"]["extraDay"]["value"],
        "nightRate": userIn["roboRate"]["extraNight"]["value"],
        "dayStart":  datetime.time.fromisoformat(userIn["roboRate"]["extraDay"]["start"]),
        "dayEnd":    datetime.time.fromisoformat(userIn["roboRate"]["extraDay"]["end"])
    }
}

oneminute = datetime.timedelta(minutes=1)
onehour =   datetime.timedelta(hours=1)
eightHours = datetime.timedelta(hours=8)
def calcWages(start, end):
    now = start
    lastBreak = now
    wage = 0
    while(now < end):
        # Take a break every eight hours
        if(now-lastBreak>=eightHours):
            now += onehour
            lastBreak = now
            continue

        # Determine the rate table for today
        rateToday = rate["standard"]
        if(now.weekday()==5 or now.weekday()==6):
            rateToday = rate["weekend"]
        isDay = (rateToday["dayStart"] <= now.time() < rateToday["dayEnd"])
        if (isDay):
            wage+= rateToday["dayRate"]
        else:
            wage+= rateToday["nightRate"]
        now += oneminute
    return wage

def calcWagesISO(start,end):
  return calcWages(datetime.datetime.fromisoformat(start),
      datetime.datetime.fromisoformat(end))

wage = calcWagesISO(userIn["shift"]["start"],userIn["shift"]["end"])
print(f"Given input: \n${userIn}")
print(f"Calculated wage is ${wage}\n")

def test():
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
      wage = calcWagesISO(test["start"],test["end"])
      print(f"Output: {wage}")
      assert wage == test["expected"]
      print("Success!\n")

test()
