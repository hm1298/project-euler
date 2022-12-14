#hm1289, solution from 2017
import math

f = open("0099_base_exp.txt")
maxl, index = 0, None
trials = f.read().split("\n")
for i in range(len(trials)):
    base, exp = map(int, trials[i].split(","))
    attempt = exp * math.log(base)
    if attempt > maxl:
        maxl, index = attempt, i
        #print(str(base) + ", " + str(exp))

print(index + 1)