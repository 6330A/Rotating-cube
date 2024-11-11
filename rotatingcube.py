import tkinter as tk
import math

import numpy as np

root = tk.Tk()
root.title("旋转立方体")
w, h = 200, 200

root.geometry(f"{w}x{h}+800+300")
canvas = tk.Canvas(root, width=w, height=h, bg="white")
canvas.pack()

length = w // 4
offset = w // 2
step = 1 / (8 * math.pi)
vx, vy, vz = 1 * step, 1 * step, 1 * step
rotation_interval = 30
points = np.array([[1, 1, 1], [-1, 1, 1], [1, 1, -1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1], [1, -1, 1], [-1, -1, 1]])
points = points * length
lines = [[0, 2], [2, 4], [4, 6], [6, 0], [1, 3], [3, 5], [5, 7], [7, 1], [0, 1], [2, 3], [4, 5], [6, 7]]

rotation_x = np.array([[1, 0, 0],
                       [0, math.cos(vx), math.sin(vx)],
                       [0, -math.sin(vx), math.cos(vx)]])
rotation_y = np.array([[math.cos(vy), 0, -math.sin(vy)],
                       [0, 1, 0],
                       [math.sin(vy), 0, math.cos(vy)]])
rotation_z = np.array([[math.cos(vz), math.sin(vz), 0],
                       [-math.sin(vz), math.cos(vz), 0],
                       [0, 0, 1]])


def repeat_task():
    global points

    points = (rotation_x @ rotation_y @ rotation_z @ points.T).T
    canvas.delete("all")

    p_2d = [[p[0] * -0.5 + p[1] + offset, p[0] * -0.5 + p[2] + offset] for p in points]
    # 先看看点
    for x, y in p_2d:
        canvas.create_oval(int(x), int(y), int(x + 1), int(y + 1), fill="black")

    for i, j in lines:
        x1, y1 = p_2d[i]
        x2, y2 = p_2d[j]  # 连接 0->2->4->6 -> 首尾相连
        canvas.create_line(x1, y1, x2, y2, fill="black")

    root.after(rotation_interval, repeat_task)


repeat_task()
root.mainloop()
