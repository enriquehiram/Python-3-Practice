lista_req=["enem1","enem2","enem3","enem4","enem1","enem1"]
dict_req={}


for i in lista_req:
	if dict_req.get(i) is None:
		dict_req[i]=1
	else:
		dict_req[i]=1+dict_req.get(i)
print(dict_req)