#import os

def youSay():
    words = input("You:")
    return words

class PY:
    messages={"sleep":"zzzzzzzzzzzzzz",
            "continuesleep":"Are you speaking to me?",
            "wakeup":"Hi, young programmer. What can I do for you?",
            "readytowork":"Choose (A/B/C): A. 讲个笑话  B. 算个算术题 C. 没事，就是调戏你一下，拜拜 ",
            "telljoke":"There are only 10 types of people: those who understand binary and those who don't.",
            "upset":"I will tell a really funny joke someday if I keep studying hard! Perhaps I could be even smarter than you.",
            "cheerup":"Fighting, Py!",
            "readytocalc":"Tell me your expression.",
            "calculated":"The result is:",
            "readytoexit":"Bye! Wish you'll be a better man next time！"}
    
    actions={"sleep":{"hi|hello|py":"wakeup","^(hi|hello|py)":"continuesleep"},
            "readytowork":{""}}

    def __init__(self, status="sleep"):
        self.status = status
        self.cmd = ""
    
    def act(self,words):
        self.actions[self.status]()

    def say(self):
        print("Py: "+self.messages[self.status])

    def listen(self):
        words = input("You:")
        #self.act(words)


    def sleep(self):
        self.say()

    def wakeup(self,hello):
        if "hi" in hello or "hello" in hello or "py" in hello:
            self.status="wakeup"
            self.say()
            return True
        else:
            self.status="continuesleep"
            self.say()
            self.status="sleep"
            return False
    
    def readytowork(self):
        self.status="readytowork"
        self.say()

    def process(self, work):
        if work in "aA":
            self.say("There are only 10 types of people: those who understand binary and those who don't.")
            self.say("Is that funny?(Y/N)")
            answer = youSay()
            if answer not in "yY":
                self.say("I will tell a really funny joke someday if I keep studying hard! Perhaps I could be even smarter than you.")
                self.say("Fighting, Py!")
        elif work in "bB":
            self.say("Tell me your expression.")
            express = youSay()
            result = eval(express)
            self.say("The result is: "+str(result))
        elif work in "cC":
            self.say("Bye! Wish you'll be a better man next time！")
            ex = input("    Press any key to exit:")
            #os.system("pause")
            exit(0)
        else:
            self.say("What's that? I haven't learn how to do it. Choose one I can.")
            return False
        return True

py=PY()
while True:
    py.act()
    hello = youSay()
    if py.wakeup(hello):
        while True:
            py.readytowork()
            work = youSay()
            if py.process(work):
                break
        
    if "hi" in hello or "hello" in hello or "py" in hello:
        py.say("Hi, young programmer. What can I do for you?")
        
        while True:
            print("Choose (A/B/C): A. 讲个笑话  B. 算个算术题 C. 没事，就是调戏你一下，拜拜 ")
            work = youSay()
            if py.process(work):
                break;
    else:
        py.say("Are you speaking to me?")


