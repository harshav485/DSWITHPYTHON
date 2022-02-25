class Cookie:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color


cookie_one = Cookie("green")
print("cookir1", cookie_one.getColor())
cookie_one.setColor("Blue")

print("cookir1", cookie_one.getColor())