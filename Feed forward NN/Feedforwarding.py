from math import exp

def sig_activation(val):
  return 1/(1+exp(-val)) 

def feed_forward(neural_net,initial_input, bias):
   input = initial_input
   for layers in neural_net:      # looping through multiple layers of the network
     conn_input=[]

     for layer in layers:
       net_input=0
       weight_list = layer['Weight']

       #calculating net input
       for i in range(len(layer['Weight'])-1):
         net_input+=weight_list[i] * input[i] + bias
       
       #calling activation function
       output=sig_activation(net_input)

       conn_input.append(output)
       layer['Output'] = output

   
     input=conn_input  # this becomes the input of the next layer or the final outcome

   return input


def call_output():
  neural_network = [[{'Weight': [0.5,0.2,0.3]}], [{'Weight': [0.4,0.33]}, {'Weight': [0.2,0.5]}]]
  input=[0,0.4,0.3]
  bias = 0.23
  output = feed_forward(neural_network, input, bias)
  print(output)


call_output()  