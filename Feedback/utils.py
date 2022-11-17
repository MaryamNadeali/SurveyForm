import datetime
import random

def trackingCode():
    current_time = datetime.datetime.now()
    uid = random.randint(1000,9999)
    trackin_code = 'WFF' + str((current_time.year)-2000) + str(current_time.month) + str(current_time.day) + str(uid)
    return trackin_code
