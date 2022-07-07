import time


class ido:
    def __init__(self, name=0):
        self.name = name  # aktualis objektum vs. parameter neve

    def setname(self):
        while True:
            self.name=self.name+1
            time.sleep(0.5)
            print(self.name)

    def getname(self):
        return self.name





try:
    ido1 = ido()
    print(ido1.getname())
    ido1.setname()
except KeyboardInterrupt:
    exit(1)