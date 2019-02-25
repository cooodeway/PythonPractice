#import os
import re

class YOU:
    def say():
        words = input("You:")
        return words

class PY:
    states={"exit":0,"error":1,"sleep":2,"ready":3,"tellingjoke":4,"calculating":5,"byebye":6,"fighting":7,"calculated":8}
    regexes=[".*","^(hi|hello|py)$","^[aA]$","^[bB]$","^[cC]$","^[yY]$", "^[nN]$","^[\+\-]?[0-9]+\.?[0-9]*([\+\-\*/][\+\-]?[0-9]+\.?[0-9]*)?$","[^b].*|b[^y].*|by[^e].*"]
    
    actions={1:{1:2,0:1},2:{1:3,0:2}, 3:{2:4, 3:5, 4:6, 0:3}, 4:{5:2, 6:7, 0:1}, 5:{7:8, 0:5}, 6:{8:2, 0:0}, 7:{0:2}, 8:{0:2}}
    messages={"sleep":"It's like someone just talk...\r\nzzzzzzzzzzzzzz",
            "ready":"Hi, young programmer. What can I do for you?\r\nChoose (A/B/C): A. 讲个笑话  B. 算个算术题 C. 没事，就是调戏你一下，拜拜 ",
            "tellingjoke":"There are only 10 types of people: those who understand binary and those who don't. \r\nIs that funny?(Y/N)",
            "fighting":"I will tell a really funny joke someday if I keep studying hard! Perhaps I could be even smarter than you.\r\nFighting, Py!",
            "calculating":"Tell me your expression.",
            "calculated":"The result is:",
            "confused":"What's that? I haven't learn how to do it. Choose one I can.",
            "byebye":"Bye! Wish you'll be a better man next time！\r\n Input 'bye' to exit:",
            "error":"I'm confused... There must be something wrong."}
    
    

    def __init__(self):
        self.symbols=[re.compile(p) for p in self.regexes]
        self.status="sleep"

    def say(self,msg=""):
        print("Py: "+self.messages[self.status]+msg)

    def listen(self,words):
        mode=self.status[self.status]
        acts=self.actions[mode]
        for symb,stat in acts:
            if self.symbols[symb].match(words):
                self.status=self.states[stat]
                if self.status=="calculated":
                    try:
                        result = eval(words)
                        self.say(result)
                    except:
                        break
                else:    
                    self.say()
                    return
        
        self.status=self.states[1]
        self.say()



py=PY()
you=YOU()
while True:
    py.listen(you.say())
    


