import datetime

ONE_MINUTE = datetime.timedelta(minutes=1)
ONE_HOUR =   datetime.timedelta(hours=1)

def _wages(start, end, roboRate): 
  #first two input params are datetime objects
  now = start
  lastBreak = now
  wage = 0
  rate = parseRateInput(roboRate)

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
    else: # it's night
      wage+= rateToday["nightRate"]
    now += ONE_MINUTE
    # end of while loop
  return wage

def wages(shift, rateIn): 
  # convert parameters to datetime objects
  return _wages(datetime.datetime.fromisoformat(shift["start"]),
               datetime.datetime.fromisoformat(shift["end"]), rateIn)

def parseRateInput(rateIn):
  return {
      "standard": {
          "dayRate":   rateIn["standardDay"]["value"],
          "nightRate": rateIn["standardNight"]["value"],
          "dayStart":  datetime.time.fromisoformat(rateIn["standardDay"]["start"]),
          "dayEnd":    datetime.time.fromisoformat(rateIn["standardDay"]["end"])
      },
      "weekend":{
          "dayRate":   rateIn["extraDay"]["value"],
          "nightRate": rateIn["extraNight"]["value"],
          "dayStart":  datetime.time.fromisoformat(rateIn["extraDay"]["start"]),
          "dayEnd":    datetime.time.fromisoformat(rateIn["extraDay"]["end"])
      }
  }