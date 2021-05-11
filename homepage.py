import random
import string
from tkinter import *
import webbrowser
from wmi import *
import pygame
import keyboard
#gui
initial_root = Tk()
initial_root.title("Home")
#main 
homepagelabel = Label(initial_root, text="home")
homepagelabel.pack()
#CALCULATOR
def calculator():
 calculator_root = Tk()
 calculator_root.title("Simple Calculator")

 e = Entry(calculator_root, width=35, borderwidth=5)
 e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

 #e.insert(0, "")

 def button_click(number):
	 #e.delete(0, END)
	 current = e.get()
	 e.delete(0, END)
	 e.insert(0, str(current) + str(number))

 def button_clear():
 	 e.delete(0, END)

 def button_add():
	 first_number = e.get()
	 global f_num
	 global math
	 math = "addition"
	 f_num = int(first_number)
	 e.delete(0, END)

 def button_equal():
	 second_number = e.get()
	 e.delete(0, END)
	
	 if math == "addition":
		 e.insert(0, f_num + int(second_number))

	 if math == "subtraction":
		 e.insert(0, f_num - int(second_number))

	 if math == "multiplication":
		 e.insert(0, f_num * int(second_number))

	 if math == "division":
		 e.insert(0, f_num / int(second_number))

	

 def button_subtract():
	 first_number = e.get()
	 global f_num
	 global math
	 math = "subtraction"
	 f_num = int(first_number)
	 e.delete(0, END)

 def button_multiply():
	 first_number = e.get()
	 global f_num
	 global math
	 math = "multiplication"
	 f_num = int(first_number)
	 e.delete(0, END)

 def button_divide():
	 first_number = e.get()
	 global f_num
	 global math
	 math = "division"
	 f_num = int(first_number)
	 e.delete(0, END)


 # Define Buttons

 button_1 = Button(calculator_root, text="1", padx=40, pady=20, command=lambda: button_click(1))
 button_2 = Button(calculator_root, text="2", padx=40, pady=20, command=lambda: button_click(2))
 button_3 = Button(calculator_root, text="3", padx=40, pady=20, command=lambda: button_click(3))
 button_4 = Button(calculator_root, text="4", padx=40, pady=20, command=lambda: button_click(4))
 button_5 = Button(calculator_root, text="5", padx=40, pady=20, command=lambda: button_click(5))
 button_6 = Button(calculator_root, text="6", padx=40, pady=20, command=lambda: button_click(6))
 button_7 = Button(calculator_root, text="7", padx=40, pady=20, command=lambda: button_click(7))
 button_8 = Button(calculator_root, text="8", padx=40, pady=20, command=lambda: button_click(8))
 button_9 = Button(calculator_root, text="9", padx=40, pady=20, command=lambda: button_click(9))
 button_0 = Button(calculator_root, text="0", padx=40, pady=20, command=lambda: button_click(0))
 button_add = Button(calculator_root, text="+", padx=39, pady=20, command=button_add)
 button_equal = Button(calculator_root, text="=", padx=91, pady=20, command=button_equal)
 button_clear = Button(calculator_root, text="Clear", padx=79, pady=20, command=button_clear)

 button_subtract = Button(calculator_root, text="-", padx=41, pady=20, command=button_subtract)
 button_multiply = Button(calculator_root, text="*", padx=40, pady=20, command=button_multiply)
 button_divide = Button(calculator_root, text="/", padx=41, pady=20, command=button_divide)

 # Put the buttons on the screen

 button_1.grid(row=3, column=0)
 button_2.grid(row=3, column=1)
 button_3.grid(row=3, column=2)

 button_4.grid(row=2, column=0)
 button_5.grid(row=2, column=1)
 button_6.grid(row=2, column=2)

 button_7.grid(row=1, column=0)
 button_8.grid(row=1, column=1)
 button_9.grid(row=1, column=2)

 button_0.grid(row=4, column=0)
 button_clear.grid(row=4, column=1, columnspan=2)
 button_add.grid(row=5, column=0)
 button_equal.grid(row=5, column=1, columnspan=2)

 button_subtract.grid(row=6, column=0)
 button_multiply.grid(row=6, column=1)
 button_divide.grid(row=6, column=2)


 calculator_root.mainloop()
#calculator buttons
calcb = Button(initial_root, text='Calculator', command=calculator)
calcb.pack()
#PASSWORD MAKER
def passwordmaker():
 #gui
 pwgeneratorroot = Tk()
 #username/email
 entrywidget1 = Entry(pwgeneratorroot, width=50)
 entrywidget1.insert(0, "Username/email: ")
 entrywidget1.grid(row=0, rowspan=2)
 #website
 entrywidget2 = Entry(pwgeneratorroot, width=50)
 entrywidget2.insert(0, "Website: ")
 entrywidget2.grid(row=2, rowspan=2)
 #def generator
 def click():
     y = ''
     for i in range (0, 20):
         x = random.randint(0,2)
         if x == 0:
             y = y + random.choice(string.ascii_letters)
         if x == 1:
             y = y + random.choice(string.punctuation)
         if x == 0:
             y = y + random.choice(string.digits)
     #open and work on file
     my_file = open("password.txt", "a")
     my_file.write("\n" + "\n" + entrywidget1.get() + "\n" + entrywidget2.get() + "\n" + "Password: " + y)
     #label the result
     label = Label(pwgeneratorroot, text="\n" + "\n" + entrywidget1.get() + "\n" + entrywidget2.get() + "\n" "Password: " + y)
     label.grid(row=5, rowspan=3)
 #button
 myButton = Button(pwgeneratorroot, text="Create Password", command=click)
 myButton.grid(row=4)
 #make everything work
 pwgeneratorroot.mainloop()
#password maker button
passwordb = Button(initial_root, text='Password creator', command=passwordmaker)
passwordb.pack()
#WEB BROWSER
def searchonweb():
 #calculator_root
 Calculatorroot = Tk()
 #def
 def searchoninternet(url):
     webbrowser.open_new_tab(url)
 #def open web tab
 search = Entry(Calculatorroot, text='Input url or search')
 search.pack()
 def searchoninternet():
     x = "https://www.google.com/search?q=" + search.get()
     webbrowser.open_new_tab(x)
 searchb = Button(Calculatorroot, text='Search', command=searchoninternet)
 searchb.pack()
 Calculatorroot.mainloop()
#web page packing
websearchb = Button(initial_root, text='Search on the web', command=searchonweb)
websearchb.pack()
#STRESS TEST NOT WORKING
def stresstest():
	stressroot = Tk()
	for i in range(0, 99999):
	    stresslab = Label(stressroot, text=i)
	    stresslab.pack()
stresstestb = Button(initial_root, text='Stress test (not working, crashes)', command=stresstest)
stresstestb.pack()
#game
def gamestart():
    pygame.init()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    class pl():
        def __init__(self, x, y, speed):
            self.x = x
            self.y = y
            self.speed = speed
    class obj():
        def __init__(self, x, y, z):
            self.x = x
            self.y=y
            self.z=big
    ent = []
    def spawn():
        ent.append('a')
    for item in ent:
        item = obj(random.randint(0,1080), random.randint(0,720), random.randint(15, 45))
    player = pl(0, 0, 1)
    size = (1920, 1080)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lil' game")
    done = False
    fps = 75
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT: 
                done = True  
        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, [player.x, player.y], 1)
        pygame.draw.polygon(screen, WHITE, [(250, 250), (250, 300), (300, 300), (300,250)])
        pygame.draw.line(screen, WHITE, (600, 600), (605, 605))
        pygame.draw.line(screen, WHITE, (605, 600), (600, 605))
        try:
            pygame.draw.circle(screen, WHITE, [a.x, a.y], a.z)
        except:
            pass
        def up():
            player.y -= player.speed
        def down():
            player.y += player.speed
        def left():
            player.x -= player.speed
        def right():
            player.x += player.speed
        def speedup():
            player.speed = player.speed * 2
        def speeddown():
            player.speed = player.speed / 2
        if keyboard.is_pressed('w'): 
            up()
        elif keyboard.is_pressed('a'): 
            left()
        elif keyboard.is_pressed('s'): 
            down()
        elif keyboard.is_pressed('d'): 
            right()
        elif keyboard.is_pressed('space'):
            spawn()
        elif keyboard.is_pressed('q'):
            speedup()
        elif keyboard.is_pressed('e'):
            speeddown()
        elif keyboard.is_pressed('x'):
            player.x = 0
            player.y = 0
            player.speed = 1
        #not to go outside the map
        if player.x < 0:
            player.x = 1920
        if player.x > 1920:
            player.x = 0
        if player.y < 0:
            player.y = 1080
        if player.y > 1080:
            player.y = 0
        #Collision
        if player.x > 250 and player.x <= 275 and player.y > 250 and player.y <= 275:
            player.x -= player.speed
            player.y -= player.speed
        if player.x >= 275 and player.x < 300 and player.y >= 275 and player.y < 300:
            player.x += player.speed
            player.y += player.speed
        if player.x > 600 and player.x <= 605 and player.y > 600 and player.y <= 605:
            player.x -= player.speed
            player.y -= player.speed
            player.x = 0
            player.y = 0
        if player.speed < 0.25:
            player.speed = 1
        pygame.display.flip()
        clock.tick(fps)
#gameb
gameb = Button(initial_root, text="Game!", command=gamestart)
gameb.pack()
#initialroot mainloop
initial_root.mainloop()