#import os

class YOU:
    def say(self):
        words = input("You:")
        return words

class PY:
    def __init__(self):
        self.sleep()

    def say(self,msg):
        print("Py: "+ msg)

    def listen(self,words):
        #words = input("You:")
        if "sleep"==self.status:
            self.wakeup(words)
        elif "ready"==self.status:
            self.process(words)
        elif "tellingjoke"==self.status:
            self.telljoke(words)
        elif "calculating"==self.status:
            self.calculate(words)
        elif "byebye"==self.status:
            self.bye(words)
        else:
            self.say("I'm confused...")

    def sleep(self):
        self.status="sleep"
        self.say("zzzzzzzzzzzzzz")

    def wakeup(self,hello):
        if "hi" in hello or "hello" in hello or "py" in hello:
            self.say("Hi, young programmer. What can I do for you?")
            self.status="ready"
            self.say("Choose (A/B/C): A. 讲个笑话  B. 算个算术题 C. 没事，就是调戏你一下，拜拜 ")
        else:
            self.say("It's like someone just talk...")
            self.sleep()

    def process(self, work):
        if work in "aA":
            self.say("There are only 10 types of people: those who understand binary and those who don't.")
            self.say("Is that funny?(Y/N)")
            self.status="tellingjoke"
        elif work in "bB":
            self.say("Tell me your expression.")
            self.status="calculating"
        elif work in "cC":
            self.say("Bye! Wish you'll be a better man next time！")
            self.status="byebye"
        else:
            self.say("What's that? I haven't learn how to do it. Choose one I can.")
            self.say("Choose (A/B/C): A. 讲个笑话  B. 算个算术题 C. 没事，就是调戏你一下，拜拜 ")

    def telljoke(self, isfunny):
        if isfunny in "yY":
            self.sleep()
        else:
            self.say("I will tell a really funny joke someday if I keep studying hard! Perhaps I could be even smarter than you.")
            self.say("Fighting, Py!")
            self.sleep()
    
    def calculate(self, expression):
        try:
            result=eval(expression)
            self.say("The result is: "+str(result))
            self.sleep()
        except:
            self.say("Is that really an expression? Let me try again.")  

    def bye(self,words):
        if "bye" in words:
            exit()
        else:
            self.sleep()

py=PY()
you=YOU()
while True:
    py.listen(you.say())


