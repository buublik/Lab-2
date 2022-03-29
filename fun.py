import threading
import hashlib
from datetime import datetime

hashToFind = ""
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
    dividor = 11881376 // _num_treads
    remainder = 11881376 - (dividor * _num_treads)
    for i in range(_num_treads):
                treadsWorks.append([i*dividor, dividor*(i+1)])

    treadsWorks[len(treadsWorks) - 1][1]+= remainder
    return treadsWorks

treadsNum = int(input("Ведите колличество потоков >> "))
hashToFind = input("Ведите хеш для применения к нему грубой силы >> ")

def process(args, id):
    print("Задание для потока #" + str(id) +" " + str(args))
    start_time = datetime.now()
    for i in range(args[0], args[1]):
        encoded=int_to_sting(i).encode()
        result = hashlib.sha256(encoded)
        if(result.hexdigest() == hashToFind):
            print( "tread " + str(id) + " found hash: " + int_to_sting(i) )
            print("Время поиска: " + str(datetime.now() - start_time))
works = calc_works(treadsNum)
threads = [threading.Thread(target=process, args = (works[i], i, )) for i in range(treadsNum)]
for t in threads:
    t.start()
for t in threads:
    t.join()
