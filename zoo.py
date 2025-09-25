import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

class Layer_Dense:
    def __init__(self,n_inputs,n_neurons) -> None:
        self.weights = 0.1 * np.random.randn(n_neurons,n_inputs)
        self.biases = np.zeros((n_neurons,1))
        
    def forward(self,inputs):
        self.output = np.dot(self.weights,inputs) + self.biases
        return self.output

class Activation_ReLU:
    def forward(self,inputs):
        self.output = np.maximum(inputs,0)

class Activation_SoftMax:
    def forward(self,inputs):
        exp_values = np.exp(inputs - np.max(inputs,axis=0,keepdims=True))
        probabilities = exp_values / np.sum(exp_values,axis=0,keepdims=True)
        self.output = probabilities        
        
class Loss:
    def calculate(self,output,target):
        squared_error = (output-target)**2
        return np.mean(squared_error)


class NN:
    
    def __init__(self,hl1_in,hl1_out,hl2_in,hl2_out,hl3_in,hl3_out,
                            output_layer_in,output_layer_out) -> None:
        self.layer1 = Layer_Dense(hl1_in,hl1_out)
        self.activation1 = Activation_ReLU()
        
        self.layer2 = Layer_Dense(hl2_in,hl2_out)
        self.activation2 = Activation_ReLU()
    
        self.layer3 = Layer_Dense(hl3_in,hl3_out)
        self.activation3 = Activation_ReLU()
        
        self.output_layer = Layer_Dense(output_layer_in,output_layer_out)
        self.output_activation = Activation_SoftMax()
        
        self.loss = Loss()
    
    def forward_propagation(self,X):
        self.layer1.forward(X)
        self.activation1.forward(self.layer1.output)
        
        # print(f"Z1 and A1 shape = {self.activation1.output.shape}")

        
        self.layer2.forward(self.activation1.output)
        self.activation2.forward(self.layer2.output)
        
        # print(f"Z2 and A2 shape = {self.activation2.output.shape}")
        
        
        self.layer3.forward(self.activation2.output)
        self.activation3.forward(self.layer3.output)
        
        # print(f"Z3 and A3 shape = {self.activation3.output.shape}")

        
        self.output_layer.forward(self.activation3.output)
        self.output_activation.forward(self.output_layer.output)
        
        # print(f"Z4 and A4 shape = {self.output_activation.output.shape}")
                
        return self.output_activation.output
    
    def one_hot(self,Y,limit=7):
        one_hot_list = []
        for value in Y:
            temp = []
            for i in range(limit):
                if value==i+1:
                    temp.append(1)
                else:
                    temp.append(0)
            one_hot_list.append(temp)
        return np.array(one_hot_list).astype(float)
    
    def derive_ReLU(self,inputs):
        return inputs>0
    
    def backpropagation(self,X,target,m=91,n=16):
        one_hot_target = self.one_hot(target).T
        self.dZ4 = self.output_activation.output - one_hot_target
        self.dW4 = (1/m)*np.dot(self.dZ4,self.activation3.output.T)
        self.dB4 = (1/m)*np.sum(self.dZ4)
        
        # print(f"self.dW4 shape = {self.dW4.shape}")
        
        self.dZ3 = np.dot(self.output_layer.weights.T,self.dZ4)*self.derive_ReLU(self.layer3.output)
        self.dW3 = (1/m)*np.dot(self.dZ3,self.activation2.output.T)
        self.dB3 = (1/m)*np.sum(self.dZ3)
        
        # print(f"self.dW3 shape = {self.dW3.shape}")
        
        self.dZ2 = np.dot(self.layer3.weights.T,self.dZ3)*self.derive_ReLU(self.layer2.output)
        self.dW2 = (1/m)*np.dot(self.dZ2,self.activation1.output.T)
        self.dB2 = (1/m)*np.sum(self.dZ2)
        
        # print(f"self.dW2 shape = {self.dW2.shape}")
        
        self.dZ1 = np.dot(self.layer2.weights.T,self.dZ2)*self.derive_ReLU(self.layer1.output)
        self.dW1 = (1/m)*np.dot(self.dZ1,X.T)
        self.dB1 = (1/m)*np.sum(self.dZ1)
        
        # print(f"self.dW1 shape = {self.dW1.shape}")
        
        return self.loss.calculate(self.output_activation.output,one_hot_target)
        
    def update_weights_and_biases(self,alpha=0.1):
        self.layer1.weights =self.layer1.weights - (alpha*self.dW1)
        self.layer1.biases = self.layer1.biases - (alpha*self.dB1)

        self.layer2.weights =self.layer2.weights - (alpha*self.dW2)
        self.layer2.biases = self.layer2.biases - (alpha*self.dB2)
        
        self.layer3.weights =self.layer3.weights - (alpha*self.dW3)
        self.layer3.biases = self.layer3.biases - (alpha*self.dB3)

        self.output_layer.weights =self.output_layer.weights - (alpha*self.dW4)
        self.output_layer.biases = self.output_layer.biases - (alpha*self.dB4)

    def predict(self):
        return np.argmax(self.output_activation.output,0)+1
    
    def accuracy(self,predictions,target):
        return np.sum(predictions==target)/target.size
    

data = pd.read_csv('zoo.csv')
data = np.array(data)
m, n = data.shape
np.random.shuffle(data)

data_dev = data[0:10]
Y_dev = data_dev.T[-1]
X_dev = data_dev.T[1:17].T.astype(float).T

data_train = data[10:m]
Y_train = data_train.T[-1]
X_train = data_train.T[1:17].T.astype(float).T
_,m_train = X_train.shape

        
neural_network = NN(16,12,12,10,10,8,8,7)
iteration = 0
while True:
    iteration +=1
    neural_network.forward_propagation(X_train)
    loss = neural_network.backpropagation(X_train,Y_train)
    neural_network.update_weights_and_biases()
    
    if loss<0.01:
        break
    
print(f"Total iteration required = {iteration}")
# test the neural network
neural_network.forward_propagation(X_dev)
print(f"Accuracy of testing = {neural_network.accuracy(neural_network.predict(),Y_dev)}")


