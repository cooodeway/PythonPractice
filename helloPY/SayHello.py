#import os

def youSay():
    words = input("You:")
    return words

def pySay(msg):
    print("Py: "+ msg)

def processedWork():
    work = youSay()
    if work in "aA":
        pySay("There are only 10 types of people: those who understand binary and those who don't.")
        pySay("Is that funny?(Y/N)")
        answer = youSay()
        if answer not in "yY":
            pySay("I will tell a really funny joke someday if I keep studying hard! Perhaps I could be even smarter than you.")
            pySay("Fighting, Py!")
    elif work in "bB":
        pySay("Tell me your expression.")
        express = youSay()
        result = eval(express)
        pySay("The result is: "+str(result))
    elif work in "cC":
        pySay("Bye! Wish you'll be a better man next time！")
        ex = input("    Press any key to exit:")
        #os.system("pause")
        exit(0)
    else:
        pySay("What's that? I haven't learn how to do it. Choose one I can.")
        return False
    return True

while True:
    pySay("zzzzzzzzzzzzzz")
    hello = youSay()
    if "hi" in hello or "hello" in hello or "py" in hello:
        pySay("Hi, young programmer. What can I do for you?")
        
        while True:
            print("Choose (A/B/C): A. 讲个笑话  B. 算个算术题 C. 没事，就是调戏你一下，拜拜 ")
            if processedWork():
                break;
    else:
        pySay("Are you speaking to me?")


