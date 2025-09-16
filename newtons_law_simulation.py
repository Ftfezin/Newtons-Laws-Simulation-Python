import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

m = 2.0 # mass of the block
F_applied = 20.0 # applied force
mu = 0.2
g = 9.8 
dt = 0.1 # time steps 
t_max = 5 # total simulation

#variable initialize
x = 0.0 # initial position 
v = 0.0 # initial velocity
t = 0.0 # start time

positions = [] # to record postion at each step
velocities = [] # record velocity
times = [] #record time 

#simulation loop

while t <= t_max:
    
    #friction force
    F_friction = mu * m * g
    
    # net force , applied force for this simple case
   
    if t < 1.0:   # push for first 1 second
        F_net = F_applied - F_friction
    else:
        F_net = -F_friction
    if F_net < 0 :
        F_net = 0
    
    #newtons second law a = f/m (acceleration)
    a = F_net/m
    
    #update velocity and postion 
    v = v + a * dt
    x = x + v * dt
    
    positions.append(x)
    velocities.append(v)
    times.append(t)
    
    t += dt
    

# Animation , force diagram
fig , ax = plt.subplots(figsize=(10,3))
ax.set_xlim(0,max(positions)+5)
ax.set_ylim(-2,2)

#ground line
ax.plot([0, max(positions)+5], [0,0], color='black')

#block 
block = patches.Rectangle((0,0), 1, 0.5, color='skyblue')
ax.add_patch(block)

#force arrows
applied_arrow = ax.arrow(0, 0.6, 0.5, 0, head_width=0.2, head_length=0.3, fc='green', ec='green')
friction_arrow = ax.arrow(0, 0.4, -0.5, 0, head_width=0.2, head_length=0.3, fc='red', ec='red')
gravity_arrow = ax.arrow(0, 0, 0, -0.7, head_width=0.2, head_length=0.3, fc='blue', ec='blue')
normal_arrow = ax.arrow(0, -0.7, 0, 0.7, head_width=0.2, head_length=0.3, fc='purple', ec='purple')

def animate(i):
    #move block
    block.set_xy((positions[i], 0))
    
    #remove old arrows
    for a in ax.patches[1:]:
        a.remove()
    
    # arrow at new block postion
    applied_arrow = ax.arrow(positions[i]+0.5, 0.6, 0.5, 0, head_width=0.2, head_length=0.3, fc='green', ec='green', label='Applied')
    friction_arrow = ax.arrow(positions[i]+0.5, 0.4, -0.5, 0, head_width=0.2, head_length=0.3, fc='red', ec='red', label='Friction')
    gravity_arrow = ax.arrow(positions[i]+0.5, 0, 0, -0.7, head_width=0.2, head_length=0.3, fc='blue', ec='blue', label='Gravity')
    normal_arrow = ax.arrow(positions[i]+0.5, -0.7, 0, 0.7, head_width=0.2, head_length=0.3, fc='purple', ec='purple', label='Normal')
    
    return block, applied_arrow, friction_arrow, gravity_arrow, normal_arrow
    
ani = FuncAnimation(fig, animate, frames=len(positions), interval=100, blit=False)

plt.show()