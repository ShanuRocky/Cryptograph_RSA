import threading
import os

primes = []
position = 0
stop = False

helpmenu = "\n\
--------help menu--------\n\
clear\t\t|clear screen\n\
exit\t\t|ends program\n\
help\t\t|show this menu\n\
lastPrime\t|show biggest prime found\n\
primes\t\t|show list of primes\n\
-------------------------\n"

#load primes from file
def getprimes(file):
    global primes
    global position
    readfile = file.readlines()
    print("@primegen : loading primes...")
    for line in readfile:
        #convert str to int
        num, char = 0, 0
        for char in line:
            if char == '\n':
                break
            num = num*10 + int(char)

        primes.append(num)

    print("@primegen : done")

    position = len(primes)
    return 0

def console():
    global stop
    global helpmenu
    global primes

    while True:
        inp = input("@primegen > ")

        if inp == "exit":
            stop = True
            return 0

        elif inp == "help":
            print(helpmenu)

        elif inp == "lastPrime":
            print(primes[len(primes)-1])

        else:
            print("unkown command")


def saveprimes(file,num):
    file.write(str(num)+"\n")
    return 0

def genratenextprime():
    global primes
    global position
    global stop

    primefile = open("primes.txt", "a")
    num = primes[position - 1] + 2
    while not stop:
          flag = True
          for i in primes:
              if i*i > num:
                 break
              if num%i == 0:
                 flag = False
                 break

          if flag:
             primes.append(num)
             saveprimes(primefile,num)
             position += 1

          num += 2

    primefile.close()

    return 0

def main():
    global stop
    global primes
    global position
    os.system("clear")

    a = threading.Thread(target = console)
    primefile = open("primes.txt", "r")
    getprimes(primefile)
    primefile.close()
    a.start()

    b = threading.Thread(target = genratenextprime)
    b.start()

    return 0

main()





