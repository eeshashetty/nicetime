import datetime

try:
    import __builtin__

except ImportError:
    import builtins as __builtin__

class NiceTime:
    def __init__(self,h,m,s):
        self.hour = h
        self.minute = m
        self.second = s

    def print(self):
        h = str(self.hour)
        m = str(self.minute)
        s = str(self.second)
        if len(h) == 1:
            h = "0" + h
        if len(m) == 1:
               m = "0" + m
        if len(s) == 1:
               s = "0" + s

        print("%s:%s:%s" %(h,m,s))


def now():
    dt = datetime.datetime.now()
    t = time(dt.hour, dt.minute, dt.second)
    return t

def time(h,m,s):
    if s <= 9:
        s += 60
        m-=1

    if m <= 9:
        m += 60
        h -= 1
    t = NiceTime(h,m,s)

    return t

