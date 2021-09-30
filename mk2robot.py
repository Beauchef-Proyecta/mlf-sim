import numpy as np
import matplotlib.pyplot as plt
from transformations import translation_along_zaxis, \
                            rotation_around_zaxis, \
                            rotation_around_yaxis


class MK2Robot:
    HOME_0 = 0
    HOME_1 = np.pi
    HOME_2 = np.pi

    def __init__(self, link_lengths):
        self.a = link_lengths
        self.q = []
        self.T = []
        self.pose = []
        self.update_pose(MK2Robot.HOME_0, MK2Robot.HOME_1, MK2Robot.HOME_2)

    def update_pose(self, q0, q1, q2):
        """
        Este metodo calcula la pose de cada link del robot, usando las matrices T y R. Luego guarda el
        resultado para cada link como un elemento del arreglo self.pose
        """
        # Calcula las matrices T y Q
        self._update_transformation_matrices(q0,q1,q2)
        
        # re-escribe self.pose como una lista de 4 matrices nulas
<<<<<<< HEAD
        self.pose = np.array([np.zeros((4,4))] * 4) 

        """ 
        Tu codigo debería verse más o menos así
        
        self.pose[0] = producto de matrices lindas
        self.pose[1] = producto de mas matrices lindas
        self.pose[2] = producto de otras matrices lindas
        self.pose[3] = producto de las ultimas matrices lindas
        """
        ## ------- ESCRIBE TU CODIGO ACA ----------
        self.pose[0] = np.matmul(self.R[0],self.T[0]) 
        self.pose[1] = np.matmul(self.R[1],self.T[1])
        self.pose[2] = np.matmul(self.R[2],self.T[2])
        self.pose[3] = np.matmul(self.R[3],self.T[3])
        ## ------- FIN DE TU CODIGO      ----------        
=======
        self.pose = [np.zeros((4,4))] * 4 
        
        self.pose[0] = np.linalg.multi_dot([self.T[0], self.R[0], self.T[1]])
        self.pose[1] = np.linalg.multi_dot([self.pose[0], self.R[1], self.T[2]])
        self.pose[2] = np.linalg.multi_dot([self.pose[1], self.R[2], self.T[3]])
        self.pose[3] = np.linalg.multi_dot([self.pose[2], self.R[3], self.T[4]])
   
>>>>>>> dev

    def _update_transformation_matrices(self, q0,q1,q2):
        """
        Este método calcula las matrices de rotación traslación del modelo de nuestro robot 
        y guarda sus valores como elementos de las listas self.R y self.T, en orden
        """
        q0 = q0 * np.pi / 180
        q1 = q1 * np.pi / 180
        q2 = q2 * np.pi / 180

        self.q = [q0, q1, q2]

        self.T = []
        self.R = []

        
<<<<<<< HEAD
        ## ------- REEMPLAZA LOS VALORES CORRECTOS PARA CADA CASO ----------
        angulo_rotacion_l0 = 90
        angulo_rotacion_l1 = q0
        angulo_rotacion_l2 = q1
        angulo_rotacion_l3 = q2
=======
        angulo_rotacion_l0 = q0
        angulo_rotacion_l1 = q1
        angulo_rotacion_l2 = -np.pi + q2
        angulo_rotacion_l3 = np.pi/2 - q1 - q2
>>>>>>> dev

        # Link 1
        self.T.append(translation_along_zaxis(self.a[0]))
        self.R.append(rotation_around_zaxis(angulo_rotacion_l0))

        # Link 2
        self.T.append(translation_along_zaxis(self.a[1]))
        self.R.append(rotation_around_yaxis(angulo_rotacion_l1))

        # Link 3
        self.T.append(translation_along_zaxis(self.a[2]))
        self.R.append(rotation_around_yaxis(angulo_rotacion_l2))

        # Link 4
        self.T.append(translation_along_zaxis(self.a[3]))
        self.R.append(rotation_around_yaxis(angulo_rotacion_l3))
        ## TODO: Revisar que ondi el ultimo link

        # Link 5
        self.T.append(translation_along_zaxis(self.a[4]))

    def inverse_kinematics(self, x, y, z):
        ## TAREA BONUS :)
        q0 = 0
        q1 = 0
        q2 = 0
        return [q0, q1, q2]
        
    def get_joint_positions(self):
        """Este método entrega las coordenadas de cada joint en tres listas; es para que el codigo se vea mas limpio :)"""
        X_pos = np.zeros(4)
        Y_pos = np.zeros(4)
        Z_pos = np.zeros(4)

        for i in range(len(self.pose)):
            X_pos[i] = np.round(self.pose[i][0, 3], 3)
            Y_pos[i] = np.round(self.pose[i][1, 3], 3)
            Z_pos[i] = np.round(self.pose[i][2, 3], 3)

        return [X_pos, Y_pos, Z_pos]
