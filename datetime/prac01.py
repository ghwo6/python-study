import datetime
y = 2026
m = 90
d = 17
# date = datetime.datetime.strptime("2026 9 17","%Y %m %d")
date = datetime.datetime.strptime(f"{y} {m} {d}","%Y %m %d")

'''
date = datetime.datetime.strptime(f"2026 90 17","%Y %m %d")
잘못된 값을 입력시 ValueError가 일어남

ghwo61351@c6r3s6 python-study % /usr/bin/python3 /Users/ghwo61351/tasks_ghwo6/python-study/datetime/prac01.py
Traceback (most recent call last):
  File "/Users/ghwo61351/tasks_ghwo6/python-study/datetime/prac01.py", line 6, in <module>
    date = datetime.datetime.strptime(f"{y} {m} {d}","%Y %m %d")
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/_strptime.py", line 568, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
  File "/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/lib/python3.9/_strptime.py", line 349, in _strptime
    raise ValueError("time data %r does not match format %r" %
ValueError: time data '2026 90 17' does not match format '%Y %m %d'
ghwo61351@c6r3s6 python-study % 
'''

# print(datetime.datetime.strptime)

print(type(date))

print(date)