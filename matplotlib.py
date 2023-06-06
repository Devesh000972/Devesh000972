from matplotlib import pylot as plt
plt. style, use ('ggplot") 
x = [5, 8, 10] 
y = [12,6,67 ]
x2 = [6,9,11] 
y2 = [6,15,7] 
plt. plot (x,y, 'g' label=' Line One', linewith= 5)
plt. plot (x2, y2, 'c',label = 'Line Two' linewidth=5) 
plt.title('Epic info')
plt.xlable('X Axis')
plt.ylable('Y Axis')
plt.legend()
plt.grid(True,color='k')

plt.show()



