from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print('yum says {}'.format(self.name))

class Dog(Animal):
#   def __init__(self, name, age):
#        Animal.__init__(self, name, age)
#        self.robotic = Robot()
    def bark(self, name):
        print('{} says "Woof!"'.format(self.name))
    def move(self):
        return self.robotic.move()

class Robot():
    def move(self):
        print('...move move move...')

class CleanRobot(Robot):
    def clean(self):
        print('I vacuum dust')

class SuperRobot():
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        #self.name = name
        #self.age = age
        self.o1 = Robot()
        self.o2 = Dog(name, age)
        self.o3 = CleanRobot()
    def playGame(self):
        print('alphago game')
    def eat(self):
        return self.o2.eat()
    def move(self):
        return self.o1.move()
    def bark(self):
        return self.o2.bark(self.name)
    def clean(self):
        return self.o3.clean()



@app.route("/")
def index():
	# return name
	quotes = ["If people do not believe that mathematics is simple, it Neumann",
			"Computer science is no more about computers than astronomy",
			"To understand recursion you must first understand recursion", 
			"You look at things that are and ask, why? I dream of things",
			"Mathematics is the key and door to the sciences. -- Galileo",
			"Not everyone will understand your journey. Thats fine."]
	randomNumber = randint(0,len(quotes)-1)
	quote = quotes[randomNumber]    
	
	beast = Animal('hello', 7)
	print('beast: {}'.format(beast.name))
	    
	machineDog = SuperRobot('The super dog', 5)
	eating = machineDog.eat()
	barking = machineDog.bark()
	cleaning = machineDog.clean()
	
	snoopy = Dog('Snoopy the sad looking dog', 3)
	print('snoopy: {}'.format(snoopy.name))
	
	
	return render_template("index.html", title="home", **locals())

@app.route("/about")
def about():
   	return render_template("about.html", title="about")
#    
#	form_data = request.form
#	email = form_data["email"]
#	print (form_data["email"])
#    #if submit:
#    #    return redirect('/index')
#	return render_template("about.html", title="about", **locals())
        

@app.route("/confirmation", methods=["POST"])
def confirmation():
	form_data = request.form
	result="All OK"
	email = form_data["email"]
	print (form_data["email"])
	#return "All OK"
	return render_template("confirmation.html", title="Form confirmation", **locals())

if __name__ == "__main__":
    app.run(debug=True)