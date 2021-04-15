# NiceTime
Your time, but nicer

## About this Project
This is a joke package, made to amuse my friends in Java Lab. If you want to use it or improve on it, please go ahead.

## Installation
```
pip install -i https://test.pypi.org/simple/ NiceTime==0.0.1
```

## Usage
```python
import nicetime

# converts minutes up to 69 in the previous hour. Continues with minute 10 in current hour. 

t = nicetime.time(3,9,12)
t.print() # should print 02:69:12

# works for seconds as well!

t = nicetime.time(4,10,9)
t.print() # should print 03:69:69

# can convert current time as well

t = nicetime.now()
t.print()

```
