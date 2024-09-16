import math

import matplotlib.pyplot as plt
from math import tan,pi



class VECTORS_MATH():
    def __init__(self):
        self.dino_vectors = [(6,4),(3,1),(1,2),(-1,5),(-2,5),(-3,4),(-4,4),(-5,3),(-5,2),
                             (-2,2),(-5,1),(-4,0),(-2,1),(-1,0),(0,-3),(-1,-4),(1,-4),
                             (2,-3),(1,-2),(3,-1),(5,1),(6,4)]
    def cartesian_to_polor(self,vector1):
        return (math.sqrt(vector1[0]**2+vector1[1]**2),math.atan2(vector1[1],vector1[0]))
    def polor_to_cartesian(self,vector1):
        return (vector1[0]*math.cos(vector1[1]),vector1[0]*math.sin((vector1[1])))

    def vectors_change_angle(self,vector1,angle):
        tmp_polor_vector = self.cartesian_to_polor(vector1)
        return self.polor_to_cartesian((tmp_polor_vector[0],angle + tmp_polor_vector[1]))

    def revolve_image(self):
        tmp_buff = []
        for i in self.dino_vectors:
            tmp_buff.append(self.vectors_change_angle(i,pi/15))
        self.op_draw_line(tmp_buff)

    def vectors_add(self,vector1,vector2):
        return (vector1[0]+vector2[0],vector1[1]+vector2[1])

    def vectors_red(self,vector1,vector2):
        return (int(vector1[0]-vector2[0]),int(vector1[1]-vector2[1]))

    def vectors_mulp(self,vector1,mulp):
        return (vector1[0]*mulp,vector1[1]*mulp)

    def vectors_distance(self,vector1):
        return math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)

    def generate_vectors_add(self):
        tmp_vector_add_0 = []
        tmp_vector_add_1 = []
        tmp_vector_add_2 = []
        # 偏移（2，5）
        for i in self.dino_vectors:
            tmp_vector_add_0.append(self.vectors_add(i,(2,5)))

        # 偏移（6，11）
        for i in self.dino_vectors:
            tmp_vector_add_1.append(self.vectors_add(i,(60,11)))

        # 偏移（-2，-3）
        for i in self.dino_vectors:
            tmp_vector_add_2.append(self.vectors_add(i,(-20,-3)))

        self.op_draw_line(tmp_vector_add_0,tmp_vector_add_1,tmp_vector_add_2,self.dino_vectors)

    def generate_vectors_multp(self):
        tmp_vector_mulp_0 = []
        for i in self.dino_vectors:
            tmp_vector_mulp_0.append(self.vectors_mulp(i,4))
        self.op_draw_line(tmp_vector_mulp_0,self.dino_vectors)

    def generate_vectors_red(self):
        tmp_vector_red_0 = []
        for i in self.dino_vectors:
            tmp_vector_red_0.append(self.vectors_red(i,(12,23)))

        self.op_draw_line(tmp_vector_red_0)

    def generate_image_x100(self):
        tmp_data = []
        # (10,10) 偏移向量
        tmp_offset_vector = []
        for i in range(10):
            for j in range(10):
                tmp_offset_vector.append((i*10,j*10))

        for n,i in enumerate(tmp_offset_vector):
            tmp_data.append([])
            for j in self.dino_vectors:
                tmp_data[n].append(self.vectors_add(j,i))

        self.op_draw_line(*tmp_data)

    def generate_x2(self):
        self.tmp_x2 = []
        for i in range(-20,21):
            self.tmp_x2.append((i,i ** 2))
        print(self.tmp_x2)

    def generate_distance(self):
        distance = 0.0
        tmp_vector = []
        tmp_target_vector = []
        for index,item in enumerate(self.dino_vectors):
            if index == 0:
                tmp_list = item
            else:
                tmp_vector.append(item)
        tmp_vector.append(tmp_list)

        for index,item in enumerate(tmp_vector):
            tmp_target_vector.append(self.vectors_red(item,self.dino_vectors[index]))

        for i in tmp_target_vector:
            distance = distance + self.vectors_distance(i)

        print("周长为："+ str(distance))

    def op_draw_dot(self,vectors):
        X = []
        Y = []
        for i in vectors:
            X.append(i[0])
            Y.append(i[1])
        plt.scatter(X,Y)
        plt.show()

    def op_draw_line(self,*args):
        print(args)
        X = []
        Y = []
        all = []
        for vectors in args:
            for i in vectors:
                X.append(i[0])
                Y.append(i[1])
            plt.plot(X,Y)
            X.clear()
            Y.clear()

        plt.show()

    def show(self):
        #self.op_draw_line(self.dino_vectors)
        self.revolve_image()


        #print(self.vectors_change_polor((1,90)))

        #self.generate_distance()

        #self.generate_image_x100()

        # self.generate_vectors_red()

        # self.generate_vectors_multp()

        # self.op_draw_dot(self.dino_vectors)


        # self.op_draw_line(self.dino_vectors)


        # self.generate_x2()
        # self.op_draw_line(self.tmp_x2)

        # self.generate_vectors_add()


if __name__ == '__main__':
    vector_math = VECTORS_MATH()
    vector_math.show()