import matplotlib.pyplot as plt
#折线图
# x = [100, 59, 80, 50]
# y = [1, 3, 5, 6]
# plt.plot(x, y, marker = 'o' , label ='chart', color ='red', linestyle = '-', markerfacecolor = 'b')
# plt.xlabel('x_data')
# plt.ylabel('y_data')
# plt.title('test plor')
# plt.legend()
# plt.show()
#直方图
import numpy as np
plt.style.use('ggplot')
mu1,mu2,sigma=100,130,15
x1=mu1+sigma*np.random.randn(10000)
x2=mu2+sigma*np.random.randn(10000)
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
n,bins,patches=ax1.hist(x1,bins=50,density=False,color='darkgreen')
n,bins,patches=ax1.hist(x2,bins=50,density=False,color='orange',alpha=0.5)
ax1.xaixs.set_ticks_postion('bottom')
ax1.yaixs.set_ticks_postion('left')
plt.xlabel('bins')
plt.ylabel('Number of Values in Bin')
fig.suptitle('histograms',fontsize=14,fontweight='bold')
ax1.set_titel('Two Frequency Distributions')
plt.show()
