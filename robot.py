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

ONE_MINUTE = datetime.timedelta(minutes=1)
ONE_HOUR =   datetime.timedelta(hours=1)

def wages(start, end): 
  #input params are datetime objects
  now = start
  lastBreak = now
  wage = 0
  # Increment wage minutely
  while(now < end):
    # Take a break every eight hours
    if(now-lastBreak>=8*ONE_HOUR):
        now += ONE_HOUR
        lastBreak = now
        continue

    # Determine the rate table for today
    if(now.weekday() == 5 or now.weekday() == 6):
      rateToday = rate["weekend"]
    else:
      rateToday = rate["standard"]
    isDay = (rateToday["dayStart"] <= now.time() < rateToday["dayEnd"])

    if (isDay):
      wage+= rateToday["dayRate"]
    else:
      wage+= rateToday["nightRate"]
    now += ONE_MINUTE
  return wage

def wages_iso(start_str,end_str): 
  #input params are ISO formatted strings
  return wages(datetime.datetime.fromisoformat(start_str),
               datetime.datetime.fromisoformat(end_str))

wage = wages_iso(userIn["shift"]["start"], userIn["shift"]["end"])
print(f"Given the suggested input,")
print(f"Calculated wage is ${wage}\n")
