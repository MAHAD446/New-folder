# parent class
class Bird:

    def __init__(self):
        print("bird id ready")

    def whoisthis(self):
        print("bird")

    def swim(self):
        print("swim faster")

# child class
class peguin(Bird):

    def __init__(self):
 # call super () function
      super().__init__()
      print("peguin is ready")

    def whoisthis(self):
         print("peguin")

    def run(self):
        print("run faster")


# object creation
peggy = peguin()
peggy .whoisthis
peggy.swim()
peggy.run()
