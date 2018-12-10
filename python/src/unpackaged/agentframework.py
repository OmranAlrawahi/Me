
'''
Agent framework has the basic agent class. Agents move in 2d raster environment.
The Agents move and eat from the resources and share the resurses with orther agents
based on defined condetion witin the agent class.
'''

#import the random operator whhic will be used to initiat the agents
import random 

#initiate agent class
class Agent ():
   
        #Selecting x and either from random or predefind list 
    def __init__ (self,environment,agents,x,y):
       self.x = x #random.randint(0,99)
       self.y = y #random.randint(0,99)
       self.environment = environment
       self.agents = agents
       self.store = 0
'''
 Intiate the agent
 
Postional arguments:
 environment -- Environment in raster format shared by the agents and the agents do their activities. 
 agents -- All agents which live in the environment
 x -- The agent location coordinate in the x axis 
 y -- The agent location coordinate in the y axis 
'''

    def move(self):
            if random.random() < 0.5:
                self.y = ( self.y + 1) % 100
            else:
                self.y = ( self.y - 1) % 100 

            if random.random() < 0.5:
                self.x = ( self.x + 1) % 100 
            else:
                self.x = ( self.x - 1) % 100
          
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10


    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent) 
            if distance <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                #print("sharing " + str(distance) + " " + str(ave))

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
'''
    
        """
        print("sharing?")
        for agent in self.agents:
            distance = self.distance(agent)
            print("distance",distance)
            if (distance < 20):
                share = (self.store + agent.store) / 2
                print("Aha distance < 20 sharing resources")
                print("self.store", self.store);
                print("agent.store", agent.store);
                print("share", share);
                self.store = share
                agent.store = share
            else:
                print("Distance >= 20 not sharing resources")
                

        
    def distance(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5        
'''