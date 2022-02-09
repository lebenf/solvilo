import re
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fd = open ("diz.txt")
    ll = fd.readlines()
    res = [x for x in ll if re.match(".ogne",x)]
    print (res)