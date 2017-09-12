print "hello world"
inp = raw_input("Europe floor?")
usf = int(inp) + 1
print "US floor",usf
try:
    x = raw_input("enter a number:")
    y = int(x)

except Exception as e:
    raise e

def bigOne(x,y):
    if x < y:
        print "x less y"
    else :
        print "x more than y"
bigOne(3,4)