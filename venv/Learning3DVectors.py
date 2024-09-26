from math import *
import matplotlib.pyplot as plt
import numpy as np


class Vector3D:
    def __init__(self):
        self.base_x = np.array((1,0,0)).reshape(3,1)
        self.base_y = np.array((0,1,0)).reshape(3,1)
        self.base_z = np.array((0,0,1)).reshape(3,1)

        self.u = (1,0,0)
        self.v = (0,1,0)
        self.w = (0,0,1)
        self.x_projection = (1, 0, 0)
        self.y_projection = (0, 1, 0)
        self.z_projection = (0, 0, 1)
        self.xy_projection = (1, 1, 0)
        self.yz_projection = (0, 1, 1)
        self.xz_projection = (1, 0, 1)
        self.projection = np.array([[1,0,0],
                                   [0,1,0],
                                   [0,0,1],
                                   [1,1,0],
                                   [0,1,1],
                                   [1,0,1],]).T
        self.origin = (0,0,0)
        self.length = 20
        self.xyz_axies = np.ones((6,6))
        for cnt,item in enumerate(self.xyz_axies):
            for count,i in enumerate(item):
                if count < 3:
                    item[count] = self.origin[count]
                else:
                    if(cnt == 0):
                        item[count] = self.u[count-3]*self.length
                    elif(cnt == 1):
                        item[count] = self.v[count-3]*self.length
                    elif(cnt == 2):
                        item[count] = self.w[count-3]*self.length
                    elif(cnt == 3):
                        item[count] = -self.u[count-3]*self.length
                    elif(cnt == 4):
                        item[count] = -self.v[count-3]*self.length
                    elif(cnt == 5):
                        item[count] = -self.w[count-3]*self.length
                    else:
                        pass

    def vector_translate(self,vector,translate):
        x, y, z = zip(vector)
        tx,ty,tz = zip(translate)
        T = [[1,0,0,tx[0]],
             [0,1,0,ty[0]],
             [0,0,1,tz[0]],
             [0,0,0,1]]
        P = [x[0],y[0],z[0],1]
        T = np.array(T)
        P = np.array(P).reshape(4,1)
        return np.dot(T,P)[:3]

    def guides_line(self,vector):
        T = np.array(vector).reshape(3,1)
        xy = np.array([[1,0,0],
                      [0,1,0],
                      [0,0,0]])

        xz = np.array([[1,0,0],
                      [0,0,0],
                      [0,0,1]])

        yz = np.array([[0, 0, 0],
                      [0, 1, 0],
                      [0, 0, 1]])

        xy_vector = np.dot(xy,T)
        xz_vector = np.dot(xz, T)
        yz_vector = np.dot(yz, T)
        target_xy_vector = (T - xy_vector)
        target_xz_vector = (T - xz_vector)
        target_yz_vector = (T - yz_vector)
        xy_projection = np.concatenate((xy_vector,target_xy_vector))
        xz_projection = np.concatenate((xz_vector, target_xz_vector))
        yz_projection = np.concatenate((yz_vector, target_yz_vector))

        all_projection = np.vstack((xy_projection.T,xz_projection.T,yz_projection.T)).T
        self.op_draw_line(all_projection)



    def test_np(self):
        # self.vector_translate((1,1,1),(1,0,0))
        self.guides_line((2,3,4))
        # print(self.base_x)
        # print(self.base_x*2+self.base_y*2+self.base_z)
        # print(np.arange(16).reshape(2,-1))
        #print(np.zeros([3,6]))
        # tmp1 = self.projection
        # tmp2 = np.arange(1,4).reshape(3,1)
        # tmp3 = (tmp1*tmp2)
        # print(tmp3)
        # self.op_draw_line(tmp3)



    def op_draw_line(self,*args):
        X,Y,Z,U,V,W = zip(args)
        print(X)
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        ax.quiver(X,Y,Z,U,V,W)
        ax.set_xlim(-max(U), max(U))
        ax.set_ylim(-max(V), max(V))
        ax.set_zlim(-max(W), max(W))
        plt.show()





if __name__ == '__main__':
    vector3d = Vector3D()
    vector3d.test_np()
    # vector3d.op_draw_line(*vector3d.xyz_axies,)
    # vector3d.op_draw_line((0,0,0,20,0,0),(0,0,0,0,20,0),(0,0,0,0,0,20),(0,0,0,-20,0,0),(0,0,0,0,-20,0),(0,0,0,0,0,-20))

