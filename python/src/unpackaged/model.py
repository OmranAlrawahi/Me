# When running in Spyder set graphics prefrences to inline.


#import operator which will be used in the model 
# 
import random
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation
import matplotlib
import tkinter
matplotlib.use('TkAgg')
import matplotlib.backends.backend_tkagg
import requests
import bs4

#a = agentframework.Agent()


r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs)

#print(a.y, a.x)
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5        
#print(a.y, a.x)
    
# module parameters located on the top of the module to simplify changing any of them 
num_of_agents = 100
num_of_iterations = 10
neighbourhood = 20
agents = []
environment = []

#read the csv file and create a 2D Lis
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)


for row in reader:	# A list of rows
    rowlist = []
    environment.append(rowlist)
    for value in row:	# A list of value
        #print(value) # Floats
        rowlist.append(value)
        



# Make the agents.
for i in range(num_of_agents):
    y = int(td_ys[i].text)# defining x
    x = int(td_xs[i].text)# defining x
    agents.append(agentframework.Agent(environment, agents, x, y))
    """
    defining the agent based on predefined x and y list from the link a bove 
    """
    
carry_on = True	    
# update the frame and make the agents animate. 
def update(frame_number):
    fig.clear()
    """
    Clear the figure
    """
    global carry_on
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    
# to stop the agents based on condition 
    if random.random() < 0.01:
        carry_on = False
        print("stopping condition")
#for agent in agents:
    #print(agent.x,agent.y)

#distance = agents[0].distance(agents[1])
#print("distance", distance)
 # Move the agents and make them interact with the environment and with each other
#    for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
#matplotlib.pyplot.show()
#for agent in agents: 
    #print(agent.x,agent.y)
# function make the agent keep moving till it reach 100 move or met the stoping condition
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 100) & (carry_on == True) :
        yield a			# Returns control and waits next call.
        a = a + 1


# to calculate the distance between agents.
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
 
def run():        
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_function)
    canvas.show()
       
root = tkinter.Tk() 
root.wm_title("Model!!")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
tkinter.mainloop()