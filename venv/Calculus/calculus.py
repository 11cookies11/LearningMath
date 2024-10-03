import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
# from scipy.interpolate import interp1d

class Calculus():
    def __init__(self):
        self.discrete_rate = 20

    def draw_xy_coordinate(self):
        # 定义控制点（这里假设控制点在二维平面上，y轴为高度）
        P0 = np.array([0, 0])  # 起点
        P1 = np.array([1, 100])  # 第一个控制点（控制曲线起始段的缓急）
        P2 = np.array([2, 90])  # 第二个控制点（控制曲线中间段的缓急）
        P3 = np.array([4, 8])  # 终点
        t_values = np.linspace(0, 1, 100)

        t_scater = np.linspace(0,1,self.discrete_rate)

        tmp_points = np.array([self.bezier_curve(t_scater, P0[0], P1[0], P2[0], P3[0]),
                               self.bezier_curve(t_scater, P0[1], P1[1], P2[1], P3[1])])
        # 计算贝塞尔曲线上的点
        curve_points = np.array([self.bezier_curve(t_values, P0[0], P1[0], P2[0], P3[0]),  # x轴数据（这里实际上没用到，因为x是等间距的）
                                 self.bezier_curve(t_values, P0[1], P1[1], P2[1], P3[1])])  # y轴数据

        speed_points = self.average_speed(self.bezier_curve(t_scater, P0[1], P1[1], P2[1], P3[1]))

        # 由于x轴是等间距的，我们可以直接生成它
        x_values = np.linspace(0, 4, len(curve_points[1]))

        x_values_tmp = np.linspace(0,4,len(tmp_points[1]))

        x_speed = np.linspace(0,4,len(speed_points))

        '''测试开始:'''
        print(self.average_flow_rate(self.volume,0.7,0.9))
        '''测试结束:'''

        plt.style.use('_mpl-gallery')
        fig,ax = plt.subplots()
        # 绘制曲线
        plt.plot(x_values, curve_points[1], label='Bezier Curve')

        print(x_values_tmp)
        # 绘制离散性
        plt.plot(x_values_tmp,tmp_points[1])
        plt.scatter(x_speed,speed_points)
        plt.xlabel('Time(h)')
        plt.ylabel('Volune(kv)')
        plt.grid(True)
        plt.show()

    def average_flow_rate(self,func,t1,t2):
        return (func(t2)-func(t1))/(t2 - t1)

    def volume(self,t):
        P0 = np.array([0, 0])  # 起点
        P1 = np.array([1, 0])  # 第一个控制点（控制曲线起始段的缓急）
        P2 = np.array([3, 30])  # 第二个控制点（控制曲线中间段的缓急）
        P3 = np.array([4, 8])  # 终点
        return self.bezier_curve(t, P0[1], P1[1], P2[1], P3[1])


    # 贝塞尔曲线计算函数（三次）
    def bezier_curve(self,t, P0, P1, P2, P3):
        return (1 - t) ** 3 * P0 + 3 * (1 - t) ** 2 * t * P1 + 3 * (1 - t) * t ** 2 * P2 + t ** 3 * P3

    def average_speed(self,speed_list):
        average_speed_list = []
        if len(speed_list) == 0:
            return Null

        for n in range(len(speed_list)):
            if n == len(speed_list)-1:
                pass
            else:
                average_speed_list.append((speed_list[n]+speed_list[n+1])/2)

        return average_speed_list




if __name__ == '__main__':
    calc  = Calculus()
    calc.draw_xy_coordinate()