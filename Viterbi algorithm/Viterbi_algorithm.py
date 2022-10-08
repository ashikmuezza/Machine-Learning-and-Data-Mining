def viterbi_algorithm(o,s,i_prob,t_prob,e_prob):
  v = [{}]
  for i in s:
    v[0][i] = i_prob[i] * e_prob[i][o[0]] 

  print(v)
  
  for t in range(1, len(o)):
    v.append({})
    for i in s:
      prob = []
      for j in s:
        prob.append(v[t-1][j] * t_prob[j][i] * e_prob[i][o[t]])
      v[t][i] = max(prob)
  print(v)
  
  max_prob,seq = [],[]
  for i in v:
    values = i.values()
    max_value = max(values)
    max_prob.append(max_value)
    keys = [key for key, value in i.items() if i[key] == max_value ]
    seq.append(keys[0])

  print (f'\nFor the given observed sequence {o} the predicted states are {seq} \nand the maximum propabilities are {max_prob}')

o = ('sunny','rainy')
s = ('Happy', 'Sad' )
i_prob = {"Happy": 0.1, "Sad": 0.9}
t_prob = {"Happy": {"Happy": 0.7, "Sad": 0.4},"Sad": {"Happy": 0.3, "Sad": 0.6},}
e_prob = {"Happy": {"sunny": 0.8, "rainy": 0.2},"Sad": {"sunny": 0.4, "rainy": 0.6},}

viterbi_algorithm(o,s,i_prob,t_prob,e_prob)