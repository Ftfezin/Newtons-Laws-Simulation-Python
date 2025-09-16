# Newton's laws simulation
It simulates a block sliding on a horizontal surface with applied force , frition, and motion.
the block's motiion is animated along with force arrows (applied , firction , gravity, normal).

#concept

# Newton's first law 
A body remains at rest or in uniform motion unless acted on by an external force.
In the simulation, the block stays still until a net force is applied.

# Newton's Second Law
F = ma
Net force determines acceleration.
If applied force > friction, the block accelerates.
If only friction acts, the block slows down.

# Newton's third law
 For every action, there is an equal and opposite reaction.
 Shown by:
  gravity force (down) ↔ Normal force (up)
  applied push (forward) ↔ Friction (backward)

# parameters you can adjust

m -> mass of block (kg)
F_applied -> applied force (N)
mu -> coefficient of friction
dt - > time step (s)
t_max -> total simulation time
for push direction eidt code :
if t < 1.0: # push for 1s
    F_net = F_applied - F_friction
else:
    F_net = -F_friction


