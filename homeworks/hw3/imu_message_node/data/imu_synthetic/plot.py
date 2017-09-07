import matplotlib.pyplot as plt
import csv

filename = 'output-10.txt'
with open(filename, 'r') as f:
  euler_list = [list(map(float,rec)) for rec in csv.reader(f, delimiter=',')]

euler_list1 = [x[0] for x in euler_list]
euler_list2 = [x[1] for x in euler_list]
euler_list3 = [x[2] for x in euler_list]
roll, = plt.plot(euler_list1, 'ro', label="roll")
pitch, = plt.plot(euler_list2, 'b+', label='pitch')
yaw, = plt.plot(euler_list3, 'g*', label='yaw')

plt.legend(handles=[roll, pitch, yaw])

plt.show()