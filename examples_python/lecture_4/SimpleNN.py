import numpy as np
import matplotlib.pyplot as plt

#---------------------------
def sigmoid(x):
    return 1/(1 + np.exp(-x))
#---------------------------

#this class assumes three layers with 8x3x8 nodes
class SimpleNN:
    def __init__(self, par_alpha, par_lambda):
        
        #learing rate parameter
        self.par_alpha = par_alpha
        
        #weight decay parameter
        self.par_lambda = par_lambda

        # init the weight matrices1
        np.random.seed(1)
        
        self.theta_layer1 = np.random.rand(3,8)
        self.theta_layer2 = np.random.rand(8,3)

        # init biases
        self.b_layer1 = np.random.rand(3)
        self.b_layer2 = np.random.rand(8)

        # init activations
        self.a_layer1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0]])
        self.a_layer2 = np.array([[0, 0, 0]])
        self.a_layer3 = np.array([[0, 0, 0, 0, 0, 0, 0, 0]])

        # init storage for all standard deviatons for delta_layer 3 (all runs)
        self.std_d3_CompleteRun = np.array([[0,0,0,0,0,0,0,0]])

    # input_values and output_values are a nx8 matrix for n number testsets
    def trainNN(self, input_values, output_values, number_epochs):
        for epoch in range(number_epochs):
            
            # Step 1: Init
            
            Dtheta_layer1 = 0 * np.ones(self.theta_layer1.shape)
            Dtheta_layer2 = 0 * np.ones(self.theta_layer2.shape)
            Db_layer1 = 0 * np.ones(3)
            Db_layer2 = 0 * np.ones(8)

            std_d3_current_epoche = np.zeros(8)

            # Step 2
            for i in range(len(input_values)):
                # get input and output as vector from the input and output matrices
                y = output_values[i, :]
                self.a_layer1 = input_values[i, :]

                # forward propagation
                z_layer2 = (self.theta_layer1 @ self.a_layer1) + self.b_layer1
                self.a_layer2 = sigmoid(z_layer2)

                z_layer3 = (self.theta_layer2 @ self.a_layer2) + self.b_layer2
                self.a_layer3 = sigmoid(z_layer3)  # layer 3 is already the output (=y)

                # backpropagation
                d_layer3 =  -(y - self.a_layer3) * self.a_layer3 * (1 - self.a_layer3)
                std_d3_current_epoche[i] = np.std(d_layer3) # store standard deviation values

                d_layer2 = self.a_layer2 * (1 - self.a_layer2) * (self.theta_layer2.T @ d_layer3)

                # partial derivatives
                jDtheta_layer2 = d_layer3[np.newaxis, :].T * self.a_layer2

                Dtheta_layer2 = Dtheta_layer2 + jDtheta_layer2
                Db_layer2 = Db_layer2 + d_layer3

                # partial derivatives
                jDtheta_layer1 = d_layer2[np.newaxis, :].T * self.a_layer1

                Dtheta_layer1 = Dtheta_layer1 + jDtheta_layer1
                Db_layer1 = Db_layer1 + d_layer2

            # add the vector standard deviation vector (value for all testsets in the current epoche) to the global storage
            self.std_d3_CompleteRun = np.r_[self.std_d3_CompleteRun, [std_d3_current_epoche]]

            #Step 3
            self.theta_layer2 = self.theta_layer2 - (self.par_alpha * ((1 / len(input_values)) * Dtheta_layer2 + self.par_lambda * self.theta_layer2))
            self.b_layer2 = self.b_layer2 - (self.par_alpha * ((1 / len(input_values)) * Db_layer2))

            self.theta_layer1 = self.theta_layer1 - (self.par_alpha * ((1 / len(input_values)) * Dtheta_layer1 + self.par_lambda * self.theta_layer1))
            self.b_layer1 = self.b_layer1 - (self.par_alpha * ((1 / len(input_values)) * Db_layer1))

        # selete first row, because the first row was just initialized with zeros
        self.std_d3_CompleteRun = np.delete(self.std_d3_CompleteRun, 0, 0)

    # forward propagation for the inputs. Each row is a test stet. With visualize=True the Network is visualized
    def predict(self, testset_x, visualize):

        z_layer2 = (self.theta_layer1 @ testset_x.T) + np.array([self.b_layer1, ] * len(testset_x)).T
        a_layer2 = sigmoid(z_layer2)

        z_layer3 = (self.theta_layer2 @ a_layer2) + np.array([self.b_layer2, ] * len(testset_x)).T
        a_layer3 = sigmoid(z_layer3)

        y = a_layer3

        if(visualize):
            self.visualizeNN(testset_x, a_layer2, a_layer3, self.b_layer1, self.b_layer2, self.theta_layer1, self.theta_layer2);

        #for x in testset_x:
        #    # forward propagation
        #    z_layer2 = (self.theta_layer1 @ x) + self.b_layer1;
        #    self.a_layer2 = hf.sigmoid(z_layer2);

        #    z_layer3 = (self.theta_layer2 @ self.a_layer2) + self.b_layer2;
        #    self.a_layer3 = hf.sigmoid(z_layer3);  # layer 3 is already the output

        #    y = np.r_[y, [self.a_layer3]];
        #y = np.delete(y, 0, 0);


        return y

    def visualizeNN(self, a1_matrix, a2_matrix, a3_matrix, b1_vector, b2_vector, weight_matrix1, weight_matrix_2):

        plt.figure(figsize=(15, 8))

        plt.subplot(2, 5, 1)
        plt.imshow(np.expand_dims(b1_vector, axis=0), cmap='seismic', interpolation='nearest', vmin=-3, vmax=3)
        plt.xlabel('neurons')
        plt.title('b Layer 1')
        #plt.colorbar()

        plt.subplot(2, 5, 6)
        plt.imshow(a1_matrix, cmap='seismic', interpolation='nearest', vmin=-3, vmax=3)
        plt.xlabel('neurons')
        plt.ylabel('test set')
        plt.title('A Layer 1')
        #plt.colorbar()

        plt.subplot(2, 5, 7)
        plt.imshow(weight_matrix1.T, cmap='seismic', interpolation='nearest', vmin=-3, vmax=3)
        plt.xlabel('neurons layer 2')
        plt.ylabel('neurons layer 1')
        plt.title('Weights Layer 1')
        #plt.colorbar()

        plt.subplot(2, 5, 3)
        plt.imshow(np.expand_dims(b2_vector, axis=0), cmap='seismic', interpolation='nearest', vmin=-3, vmax=3)
        plt.xlabel('neurons')
        plt.title('b Layer 2')
        #plt.colorbar()

        plt.subplot(2, 5, 8)
        plt.imshow(a2_matrix.T, cmap='seismic', interpolation='nearest', vmin=-3, vmax=3)
        plt.ylabel('test set')
        plt.xlabel('neurons')
        plt.title('A Layer 2')
        #plt.colorbar()

        plt.subplot(2, 5, 9)
        plt.imshow(weight_matrix_2.T, cmap='seismic', interpolation='nearest', vmin=-3, vmax=3)
        plt.xlabel('neurons layer 3')
        plt.ylabel('neurons layer 2')
        plt.title('Weights Layer 2')
        #plt.colorbar()

        plt.subplot(2, 5, 10)
        plt.imshow(a3_matrix.T, cmap='seismic', interpolation='nearest', vmin=-3, vmax=3)
        plt.title('A Layer 3')
        plt.ylabel('test set')
        plt.xlabel('neurons')
        plt.colorbar()

        plt.show()

        return
