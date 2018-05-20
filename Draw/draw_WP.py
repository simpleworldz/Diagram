import numpy as np
import matplotlib.pyplot as plt
from draw_PP import get_data
import sys

def draw_WP(mydata,index = 0,d =1 ,D =1):
    """
    画WP（相对介电温谱）图 并保存在figure文件夹中
    d： 厚度，D： 直径
    """
    x = mydata[:,0]
    y1 = mydata[:,1]
    y2 = mydata[:,2] 
    #处理后 y1 为 相对介电常数 ε
    y1 = [10**12*144*y*d/D**2 for y in y1]
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    #有中文出现的情况，需要u'内容'

    #设置图像尺寸
    fig = plt.figure(figsize = (8,5))
    #设置一张图像只画一个坐标图 ax1为第一条曲线 相对介电常数 ε
    ax1 = fig.add_subplot(111)
    #标题
    ax1.set_title('电容介电温谱',fontsize = 20,color = 'b')
    #ax1 的坐标参数
    ax1.set_ylabel('相对介电常数 ε', color = 'r')
    ax1.set_xlabel('温度 T （℃）',color = 'r')
    #作图
    line1, = ax1.plot(x,y1,'-ob')
    #ax2 为第二条曲线  损耗角正切值 D ，ax1 与 ax2 在统一坐标图上
    ax2 = ax1.twinx()
    #设置ax2坐标参数 并plot
    ax2.set_ylabel('损耗角正切值 D',color = 'r')
    line2, = ax2.plot(x,y2,'-or')
    #中间的图示（区分两条直线）
    fig.legend((line1,line2),('ε','D'),'center')
    plt.savefig(sys.path[0]+'/figure/WP_'+str(index + 1))
    print('完成 图: '+'/figure/PP_'+str(index + 1))
    

#读取 WP.DAT 数据
#当前目录并非.py文件所在目录，而是powershell所在目录  
if __name__ == '__main__':
    data = np.genfromtxt(sys.path[0]+'/WP.DAT',delimiter = '\t')
    #作图 四幅
    for i in range(4):
        mydata = get_data(data,i)
        draw_WP(mydata,i,d = 1.22 ,D = 12.82)