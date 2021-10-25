from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import matplotlib.pyplot as plt
from matplotlib.pyplot import Figure
from matplotlib.pyplot import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from mk2robot import MK2Robot
from RepeatButton import RepeatButton

# Create main window
root = Tk()
root.iconbitmap("MLF.ico")
root.title("My Little Factory")

# A Frame that's going to contain the other widgets.
mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


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
    ax.scatter(0, 0, 0, zdir='z', s=30)                                          # Origin
    ax.plot([0, X_pos[0]], [0, Y_pos[0]], [0, Z_pos[0]])                         # L0
    ax.plot([X_pos[0], X_pos[1]], [Y_pos[0], Y_pos[1]], [Z_pos[0], Z_pos[1]])    # L1
    ax.plot([X_pos[1], X_pos[2]], [Y_pos[1], Y_pos[2]], [Z_pos[1], Z_pos[2]])    # L2
    ax.plot([X_pos[2], X_pos[3]], [Y_pos[2], Y_pos[3]], [Z_pos[2], Z_pos[3]])    # L3
    ax.scatter(X_pos, Y_pos, Z_pos, zdir='z', s=20)                              # Joints

    # Make it prettier
    ax.set_title('MK2 Arm Simulator')

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

# Change the style of the plots.
plt.style.use('ggplot')

# Create the figure
fig = Figure()
ax = fig.add_subplot(111, projection='3d')
fig.set_facecolor(ax.get_facecolor())

# Plot the robot for the first time
plot_robot(X_pos, Y_pos, Z_pos)

axcolor = 'lightgoldenrodyellow'
ax.margins(x=0)

# Add to the mainframe
canvas = FigureCanvasTkAgg(fig, mainframe)
canvas.get_tk_widget().grid(row=0, column=0, columnspan=3)


""" 3. Sliders creation """

# Create a Figure for the sliders
fig_slider = Figure(figsize=(6, 1))
fig_slider.set_facecolor(ax.get_facecolor())

# Make horizontal sliders
axq0 = fig_slider.add_axes([0.1, 0.1, 0.8, 0.08])
q0_slider = Slider(
    ax=axq0,
    label='q0 [º]',
    valmin=-90,
    valmax=90,
    valinit=0,
)

axq1 = fig_slider.add_axes([0.1, 0.45, 0.8, 0.08])
q1_slider = Slider(
    ax=axq1,
    label='q1 [º]',
    valmin=-90,
    valmax=90,
    valinit=0,
)

axq2 = fig_slider.add_axes([0.1, 0.8, 0.8, 0.08])
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

# Add the sliders to the mainframe
canvas2 = FigureCanvasTkAgg(fig_slider, mainframe)
canvas2.get_tk_widget().grid(row=1, column=2, rowspan=3, sticky=W)


""" 4. Buttons creation """


def slider_setter(slider):
    def move_left_slider():
        return slider.set_val(max(slider.val - 1, slider.valmin))

    def move_right_slider():
        return slider.set_val(min(slider.val + 1, slider.valmax))
    return move_left_slider, move_right_slider


# Set the functions called from the Buttons.
left_q0, right_q0 = slider_setter(q0_slider)
left_q1, right_q1 = slider_setter(q1_slider)
left_q2, right_q2 = slider_setter(q2_slider)

# Icons made by Freepik from www.flaticon.com
left_img = Image.open("left.png")
left_img = left_img.resize((16, 16))
right_img = Image.open("right.png")
right_img = right_img.resize((16, 16))

left_img = ImageTk.PhotoImage(left_img)
right_img = ImageTk.PhotoImage(right_img)

# Make Buttons
left_q0_btn = RepeatButton(
    mainframe,
    image=left_img,
    command=left_q0,
    repeatinterval=100,
    repeatdelay=10
)

right_q0_btn = RepeatButton(
    mainframe,
    image=right_img,
    command=right_q0,
    repeatinterval=100,
    repeatdelay=10
)

left_q1_btn = RepeatButton(
    mainframe,
    image=left_img,
    command=left_q1,
    repeatinterval=100,
    repeatdelay=10
)

right_q1_btn = RepeatButton(
    mainframe,
    image=right_img,
    command=right_q1,
    repeatinterval=100,
    repeatdelay=10
)

left_q2_btn = RepeatButton(
    mainframe,
    image=left_img,
    command=left_q2,
    repeatinterval=100,
    repeatdelay=10)

right_q2_btn = RepeatButton(
    mainframe,
    image=right_img,
    command=right_q2,
    repeatinterval=100,
    repeatdelay=10
)

left_q0_btn.grid(row=3, column=0, sticky=E, padx=(20, 5), pady=5)
right_q0_btn.grid(row=3, column=1, sticky=W, padx=5, pady=5)
left_q1_btn.grid(row=2, column=0, sticky=E, padx=(20, 5), pady=5)
right_q1_btn.grid(row=2, column=1, sticky=W, padx=5, pady=5)
left_q2_btn.grid(row=1, column=0, sticky=E, padx=(20, 5), pady=5)
right_q2_btn.grid(row=1, column=1, sticky=W, padx=5, pady=5)


# Create an style to get the background of matplotlib plots.
background = fig.get_facecolor()
background = [int(background[i]*255) for i in range(3)]
background = [hex(background[i])[2:] for i in range(3)]
bg = f"#{background[0]}{background[1]}{background[2]}"

s = ttk.Style()
s.configure('.', background=bg)


# Start the loop to print on screen.
root.mainloop()
