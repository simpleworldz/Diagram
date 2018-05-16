import numpy as np 
import matplotlib.pyplot as plt 
from scipy import interpolate 

def smooth_line(x,y,ax,linestyle = '-',color = 'r'):
    """
    使曲线更光滑
    x,y: x,y轴数组
    """
    f = interpolate.interp1d(x, y, kind='cubic')
    nx = np.linspace(x.min(),x.max(),1000)
    ny = f(nx)
    ax.plot(nx, ny,linestyle,color = color) 

def get_data(data,index):
    """data：数据 ， index：索引"""
    mydata = data[:,[0,index*2 + 1,index*2 + 2]]
    return mydata
   

def darw_pp(mydata,index):
    """画PP（电子陶瓷介电频谱）图 并保存在figure文件夹中"""
    x = mydata[:,0]
    y1 = mydata[:,1]
    y2 = mydata[:,2]
    #将 KHZ 转化为 HZ
    x = np.array([x1*1000 for x1 in x])
    #处理后 y1 为 ε
    y1 = [10**11*144*y*1.22/12.82**2 for y in y1]
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    #有中文出现的情况，需要u'内容'
    
    #设置图像尺寸
    fig = plt.figure(figsize = (8,5))
    #设置一张图像只画一个坐标图 ax1为第一条曲线 ε
    ax1 = fig.add_subplot(111)
    #标题
    ax1.set_title('电子陶瓷介电频谱',fontsize = 20, color = 'b')
    #设置第一条曲线参数
    ax1.set_ylabel('ε',fontsize = 20, color = 'r')
    ax1.set_xlabel('f (HZ)',fontsize = 15, color = 'r')
    #ax2 为第二条曲线  损耗角正切值 D ，ax1 与 ax2 在统一坐标图上
    ax2 = ax1.twinx()
    ax2.set_ylabel('损耗角正切值 D',color = 'r')
    #是两条曲线更平滑
    smooth_line(x,y1,ax1,'-','b')
    smooth_line(x,y2,ax2,'--','r')
    #x轴 间隔设置 log
    plt.xscale('log')
    #**再 来个 散点**
    ax1.scatter(x,y1,marker = '^',color = 'b')
    ax2.scatter(x,y2,marker = '*',color = 'r')
    #中间的图示（区分两条直线）
    import matplotlib.lines as mlines
    line_1 = mlines.Line2D([],[],'1','-','b','^',label = 'ε')
    line_2 = mlines.Line2D([],[],'1','-','r','*',label = 'D')
    fig.legend(handles = [line_1,line_2],loc = 'center')
    #保存图片 python windows也可以用/ ?
    plt.savefig('figure/PP_'+str(index + 1))
    print('完成 图'+str(index +1))

#读取PP.DAT文件
#当前目录并非.py文件所在目录，而是powershell所在目录  
if __name__ == '__main__':
    #import os
    #print(os.getcwd())
    data = np.genfromtxt('PP.DAT',delimiter = '\t')
    #作图 四幅
    for i in range(4):
        mydata = get_data(data,i)
        darw_pp(mydata,i)
