from datetime import datetime
def currentTime():
	now = datetime.now()
	print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
currentTime()
