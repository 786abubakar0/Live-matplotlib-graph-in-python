import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import sys

df = pd.read_csv("data.csv") # Reading the file
matplotlib.use("TkAgg")  # Making matplotlib use tkinter.
plt.ion()  # Interactive mode on

ax1 = plt.axes(xlim=(0,100), ylim=(-50,+50))
lines_colors = ["orange","red"]
lines = []

for index in range(2):
    line_obj = ax1.plot([],[],lw=2,color=lines_colors[index])[0]
    lines.append(line_obj)

plt.xlabel("Last 100 Readings") # Naming the x axis
plt.ylabel("Data")  # Naming the y axis
data_x = df['x']
data_y = df['y']
x = []
y1 =[]
y2=[]
reading_count = 0

try:
    for i in range(df.shape[0]):
        if(len(x)>100):
            y1.pop(0)
            y2.pop(0)
        else:
            x.append(reading_count)

        reading_count += 1
        y1_value = data_x.iloc[i]
        y2_value = data_y.iloc[i]

        y1.append(y1_value)
        y2.append(y2_value)
        lines[0].set_data(x,y1)
        lines[1].set_data(x,y2)
        plt.legend(["X_data", "Y_data"], loc="upper left")

        plt.draw()
        plt.pause(0.1)

    x_difference = df['x'].max() - df['x'].min()
    y_difference = df['y'].max() - df['y'].min()
    difference = abs(x_difference - y_difference)

    if (difference < 20):
        level = "Expert"
    elif (difference < 40):
        level = "Intermediate"
    else:
        level = "Novice"
    graph_text = plt.text(50, 40, level, bbox=dict(facecolor='blue', alpha=0.5))
    # graph_text.remove()

    plt.ioff()
    plt.show()
except Exception as e:
    sys.exit()