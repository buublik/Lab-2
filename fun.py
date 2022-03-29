import threading
import os
import hashlib
hashToFind = "74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f"
alphabet = "abcdefghijklmnopqrstuvwxyz"
def int_to_sting(_int):
    b = ['a','a','a','a','a']
    n = _int
    i = 0
    while n > 0:
        b[4-i] = alphabet[n % 26]
        i+=1
        n = n // 26
    return "".join(b)
def calc_works(_num_treads):
    treadsWorks = []
    dividor = 11881376 // treadsNum
    remainder = 11881376 - (dividor * treadsNum)
    for i in range(treadsNum):
        if(remainder == 0):
                treadsWorks.append([i*dividor, dividor*(i+1)])
        if(remainder > 0):
                treadsWorks.append([i*dividor, dividor*(i+1)])
    if(remainder > 0):
        treadsWorks[len(treadsWorks) - 1][1]+= remainder
    return treadsWorks
treadsNum = int(input("Ведите колличество потоков>> "))
def process(args, id):
    for i in range(args[0], args[1]):
        encoded=int_to_sting(i).encode()
        result = hashlib.sha256(encoded)
        if(result.hexdigest() == hashToFind):
            print( "tread " + str(id) + " found hash: " + int_to_sting(i) )
works = calc_works(treadsNum)
threads = [threading.Thread(target=process, args = (works[i], i, )) for i in range(treadsNum)]
for t in threads:
    t.start()
for t in threads:
    t.join()