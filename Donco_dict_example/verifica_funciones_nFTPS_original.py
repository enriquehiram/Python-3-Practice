import openpyxl
import docx2txt
import pdb

class Funcion(object):
	cont=0
	celda=[]
	def __init__(self, nombreFuncion, cont=0,celda =None):
		self.nombre= nombreFuncion
		self.cont=cont
		self.celda=[]
		
dict_fun_exist={}
dict_fun_no_exist={}
lista_funciones_existentes = []
lista_funciones_inexistentes = []
text = docx2txt.process("C:\\Users\\cricano\\Documents\\ADProjects\\FTPS\\STATEST.docx")
path_file="C:\\Users\\cricano\\Documents\\ADProjects\\FTPS\\"
file_name="FTPS_EM_ Driver Assist _Cx483_V1.0_ScriptTest.xlsx"											#"FTPS_Driver_Assitant_EM_editable.xlsx"
wrkbook = openpyxl.load_workbook(path_file+file_name)
source = wrkbook["FTPS_Template"]
inicio_filas = 29
fin_filas=269

#columnas
#systen configuration (E) -->AD -->30
#Initial conditions			 AE -->31
#Test action				 AH -->34
#Expected Results			 AJ -->36
#
#
#
columna_interes=36+2#+2 por un desfase que hay en el ftps de driver de EM
funciones=[]
for i_filas in range (inicio_filas, fin_filas, 1):
	#
	print(i_filas)
	information = source.cell(row = i_filas, column = columna_interes)
	#print(information)
	#print(type(information.value))
	if  (information.value is not None):
		i=0
		k=0
		while i<len(information.value):
		#Se pasan las funciones del formato de celda de excel a una lista sobre la que se buscaran las funciones en word
			if i==0:
				i_inicio=i
			if information.value[i]=='\n':
				i_inicio=i+1
			elif information.value[i] == '(':
				i_lc=i
			elif information.value[i] == ')':
				i_rc=i
				funciones.append(information.value[i_inicio:i_lc])
				i_inicio=-1
				i_rc=-1
				i_lc=-1
			i=i+1
		#if (i_filas==143):
	#		pdb.set_trace()
		for funcion in funciones: #pdb.set_trace()
			
			if text.find(funcion): #la funciòn existe en la libreria
				if dict_fun_exist.get(funcion):	#existe la funcion en la libreria y en el diccionario de funciones
					#pdb.set_trace()
					dict_fun_exist[funcion]["count"]=dict_fun_exist[funcion]["count"]+1
					dict_fun_exist[funcion]["celda"].append(information.coordinate)
				else:
					
					dict_fun_exist[funcion]={"count":1,"celda":[information.coordinate]}
			else:
				
				if dict_fun_no_exist.get(funcion):	#existe la funcion en la libreria y en el diccionario de funciones
					#pdb.set_trace()
					dict_fun_no_exist[funcion]["count"]=dict_fun_no_exist[funcion]["count"]+1
					dict_fun_no_exist[funcion]["celda"].append(information.coordinate)
				else:
					#pdb.set_trace()
					dict_fun_no_exist[funcion]={"count":1,"celda":[information.coordinate]}
print("Funciones existentes:")
print(dict_fun_exist)
print("Funciones no existentes:")
print(dict_fun_no_exist)
					
		
	
	
				
			
