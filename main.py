import re
import random
# Press the green button in the gutter to run the script.
def check (good, guess):
    if good == guess:
        return [True, good, '', '']
    else:
        right = ""
        ok = ""
        ko = ""
        for i in range(len(good)):
            if guess[i] == good[i]:
                right += guess[i]
                ok += "."
            else:
                right += '.'
                if guess[i] in good:
                    ok += guess[i]
                else:
                    ko += guess[i]
                    ok+='.'
        return [False, right, ok, ko]

def purge (wordlist, right, oks, ko):
    res = [x for x in wordlist if re.match(right, x)]
    okk = ""
    for ok in oks:
        res = [x for x in wordlist if not re.match(ok, x)]
        okk += ok.replace(".","")
    for kk in ko:
        res = [x for x in res if kk not in x]
    for oo in okk:
        res = [x for x in res if oo in x]
    return res

def choose_random (stats, wl, right, ok, ko):
    return random.choice(wl)

def dummy (wl):
    return

def mergeright(old, new):
    rval = ''
    for i in range(len(old)):
        if old[i] == new[i]:
            rval += new[i]
        elif old[i] == '.':
            rval += new[i]
        else:
            rval += old[i]
    return rval

def split_oks(ok):
    retval = []
    if ok == '.....':
        return retval
    for i in range(len(ok)):
        if ok [i] != '.':
            retval.append( ('.'*i)+ok[i]+('.'*(4-i)) )
    return retval


def testfunc (good, cfunc, sfunc, wl):
    maxiter = 6
    i=1
    res = wl
    history = []
    right = '.....'
    oks = []
    ko = ''
    while i <= 6:
        stats = sfunc(res)
        chosen = cfunc(stats, res, right, oks, ko)
        result = check(good, chosen)
        history.append([chosen, result])
        if result[0]:
            return [i, history]
        if result[2] and result[2] != '.....':
            oks += split_oks(result[2])
        right = mergeright(right, result[1])
        ko += result[3]
        res = purge(res, right, oks, ko)
        i+=1
    return [0, history]
if __name__ == '__main__':
    fd = open ("diz.txt")
    ll = fd.readlines()
    res = [x.strip() for x in ll]
    tries = []
    for i in range (1000):
        rr = testfunc('fioca', choose_random, dummy, res)
        tries.append(rr[0])
    print (tries)
    print ("1 ", tries.count (1))
    print ("2 ", tries.count (2))
    print ("3 ", tries.count (3))
    print ("4 ", tries.count (4))
    print ("5 ", tries.count (5))
    print ("6 ", tries.count (6))
    print ("0 ", tries.count (0))





