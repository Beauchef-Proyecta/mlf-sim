import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import Slider, Button

from mk2robot import MK2Robot


""" 1. Useful functions """

def update(val):
    # This function is called ny time a slider value changes
    robot.update_pose(q0_slider.val, q1_slider.val, q2_slider.val)
    [X_pos, Y_pos, Z_pos] = robot.get_joint_positions()
    plot_robot(X_pos, Y_pos, Z_pos)
    fig.canvas.draw_idle()

def plot_robot(X_pos, Y_pos, Z_pos):
    
    # Clear figure
    ax.clear()

    # Plot the data
    ax.scatter(0, 0, 0, zdir='z', s=30)                                     # Origin
    ax.plot([0,X_pos[0]],[0,Y_pos[0]],[0,Z_pos[0]])                         # L0
    ax.plot([X_pos[0],X_pos[1]],[Y_pos[0],Y_pos[1]],[Z_pos[0],Z_pos[1]])    # L1
    ax.plot([X_pos[1],X_pos[2]],[Y_pos[1],Y_pos[2]],[Z_pos[1],Z_pos[2]])    # L2
    ax.plot([X_pos[2],X_pos[3]],[Y_pos[2],Y_pos[3]],[Z_pos[2],Z_pos[3]])    # L3
    ax.scatter(X_pos, Y_pos, Z_pos, zdir='z', s=20)                         # Joints

    # Make it prettier
    ax.set_ylabel('Y [mm]')
    ax.set_xlabel('X [mm]')
    ax.set_zlabel('Z [mm]')

    # Set axis limits
    ax.set_xlim(-300, 300)
    ax.set_ylim(-300, 300)
    ax.set_zlim(0, 300)



""" 2. The actual script """

# Spawn a robot!
robot = MK2Robot(link_lengths=[55, 39, 135, 147, 66.3])
robot.update_pose(0, 0, 90)
[X_pos, Y_pos, Z_pos] = robot.get_joint_positions()

# Create the figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the robot for the first time
plot_robot(X_pos, Y_pos, Z_pos)

axcolor = 'lightgoldenrodyellow'
ax.margins(x=0)

# Adjust the main plot to make room for the sliders
plt.subplots_adjust(bottom=0.4)

# Make horizontal sliders
axq0 = plt.axes([0.2, 0.1, (1-0.2)-0.1, 0.03], facecolor=axcolor)
q0_slider = Slider(
    ax=axq0,
    label='q0 [º]',
    valmin=-90,
    valmax=90,
    valinit=0,
)

axq1 = plt.axes([0.2, 0.2, (1-0.2)-0.1, 0.03], facecolor=axcolor)
q1_slider = Slider(
    ax=axq1,
    label='q1 [º]',
    valmin=-90,
    valmax=90,
    valinit=0,
)

axq2 = plt.axes([0.2, 0.3, (1-0.2)-0.1, 0.03], facecolor=axcolor)
q2_slider = Slider(
    ax=axq2,
    label='q2 [º]',
    valmin=0,
    valmax=180,
    valinit=90,
)

# Add event handler for every slider
q0_slider.on_changed(update)
q1_slider.on_changed(update)
q2_slider.on_changed(update)


# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
q0_rightax = plt.axes([0.01, 0.1, 0.04, 0.03])
q0_right_button = Button(q0_rightax, '<-', color='1')

q0_leftax = plt.axes([0.06, 0.1, 0.04, 0.03])
q0_left_button = Button(q0_leftax, '->', color='1')

q1_rightax = plt.axes([0.01, 0.2, 0.04, 0.03])
q1_right_button = Button(q1_rightax, '<-', color='1')

q1_leftax = plt.axes([0.06, 0.2, 0.04, 0.03])
q1_left_button = Button(q1_leftax, '->', color='1')

q2_rightax = plt.axes([0.01, 0.3, 0.04, 0.03])
q2_right_button = Button(q2_rightax, '<-', color='1')

q2_leftax = plt.axes([0.06, 0.3, 0.04, 0.03])
q2_left_button = Button(q2_leftax, '->', color='1')


def right_q0(event):
    q0_slider.set_val(max(q0_slider.val - 1, q0_slider.valmin))

def left_q0(event):
    q0_slider.set_val(min(q0_slider.val + 1, q0_slider.valmax))

def right_q1(event):
    q1_slider.set_val(max(q1_slider.val - 1, q1_slider.valmin))

def left_q1(event):
    q1_slider.set_val(min(q1_slider.val + 1, q1_slider.valmax))

def right_q2(event):
    q2_slider.set_val(max(q2_slider.val - 1, q2_slider.valmin))

def left_q2(event):
    q2_slider.set_val(min(q2_slider.val + 1, q2_slider.valmax))

q0_right_button.on_clicked(right_q0)
q0_left_button.on_clicked(left_q0)
q1_right_button.on_clicked(right_q1)
q1_left_button.on_clicked(left_q1)
q2_right_button.on_clicked(right_q2)
q2_left_button.on_clicked(left_q2)

# Now we are ready to go
plt.show()



