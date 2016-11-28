import numpy as np
"""
Formulas to calculate output

1. Weight sum = input1*weight1 + input2*weight2 + input3*weight3 etc...
2. Normalize weighted sum so we get a number between 0 and 1 - use sigmoid function
3. look into minimum firing threshold???
"""

"""
How to adjuct weights? - Error Weighted Derivative

error * input*SigmoidCurveGradiant(output)
SigmoidCurveGradiant = derivative of output (output * (1-output)
***This is SIMPLE - other ways to make neuron learn quicker
"""

"""
Layers (can add as many as needed)

1.combine all inputs
2. map the inputs to outputs using output of first layer as input
3. The output
"""

#sigmoid function - normalize weighted sum to get a number between 0 and 1
#if derivative is true, get derivative of sigmoid
def sigmoid_function(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

#example input data
input_nodes = np.array([[0,0,1],
                        [0,1,0],
                        [1,0,0],
                        [1,1,1]])

#example expected output data
output_nodes = np.array([[0],
              [1],
              [1],
              [0]])

np.random.seed(1)

#Weight of decision made - each input node gets a weight - pass this weight through formula  - use to calculate output - should be random in beginning
#3 elements in input (3 columns) and 4 elements in output (4 columns) - layer one to layer two
weight0 = 2*np.random.random((3,4)) - 1
#output of layer 2 to layer 3
weight1 = 2*np.random.random((4,1)) - 1

#loop to keep trying
for tries in xrange(60000):
    #populate all layers
    layer0 = input_nodes

    # input * weight (weighted sum) + sigmoid function to normalize so we get a number between 0 and 1
    layer1 = sigmoid_function(np.dot(layer0,weight0))
    layer2 = sigmoid_function(np.dot(layer1,weight1))

    #What is the error? what is the difference between AI's outcome and desired outcome? - adjust weight accordingly

    # layer 2 = final decision, how far off from desired output - returns a vector
    layer2error = output_nodes - layer2

    if (tries % 10000) == 0:
        #print error every 10000 try
        print "Error:" + str(np.mean(np.abs(layer2error)))
    if (tries % 60000) == 0:
        print layer2

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = layer2error*sigmoid_function(layer2,deriv=True)

    # how much did each layer 1 value contribute to the layer 2 error (according to the weights)?
    l1_error = l2_delta.dot(weight1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * sigmoid_function(layer1, deriv=True)

    weight1 += layer1.T.dot(l2_delta)
    weight0 += layer0.T.dot(l1_delta)

