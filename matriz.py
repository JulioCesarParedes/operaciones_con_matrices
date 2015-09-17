import Fraccion

class matriz:
 def __init__(self,rmatriz):
  rmatriz = self.asignar_matriz(rmatriz)
  if self.isvalida(rmatriz):
   self.__matriz = rmatriz
  else:
   raise Exception('Datos incorrectos')
   
 def asignar_matriz(self,rmatriz):
  if self.islist(rmatriz) or self.istuple(rmatriz):
   listVacia=[]
   listVacia.append(rmatriz)
   return listVacia if self.isvacia(rmatriz) else rmatriz if self.haslen(rmatriz[0]) else listVacia
  else:
   raise Exception('Tipo de dato incorrecto: Tiene que ser de tipo list o tuple')
   
 def isvalida(self,rmatriz):
  return self.isElemValido(rmatriz) if self.ismatriz(rmatriz) else False
  
 def ismatriz(self,rmatriz):
  if self.islist(rmatriz) or self.istuple(rmatriz):
   for fila in rmatriz:
    if not (self.islist(fila) or self.istuple(fila)):
	 return False
   return True
  else:
   return False
   
 def isElemValido(self,rmatriz):
  if self.igual_len(rmatriz):
   for fila in rmatriz:
    for elemento in fila:
	 if not (self.isint(elemento) or self.isfloat(elemento) or self.islong(elemento) or self.isfrac(elemento)):
	  return False
   return True
  else:
   return False
   
 def igual_len(self,rmatriz):
  if len(rmatriz) != 1:
   for i in range(1,len(rmatriz)):
    if len(rmatriz[i-1]) != len(rmatriz[i]):
	 if raw_input("""
	 \rError: Cada fila debe tener el mismo num de elementos.
	 \rPresiona 'y' si quieres completar con 0's,
	 \rsi no lo deseas presina cualquier tecla:  
	 \r""") == 'y':
	  self.rellenar_con_0(rmatriz,self.mayor_len(rmatriz))
	  return True
	 else:
	  return False
  return True
  
 def mayor_len(self,rmatriz):
  mayor=0
  for fila in rmatriz:
   mayor = mayor if mayor > len(fila) else len(fila)
  return mayor
   
 def haslen(self,rmatriz):
  try:
   len(rmatriz)
   return True
  except:
   return False
   
 def isvacia(self,rmatriz):
  return len(rmatriz) == 0
  
 def rellenar_con_0(self,rmatriz,mayor):
  for fila in rmatriz:
   while len(fila) < mayor:
    fila.append(0)
  
 def isint(self,variable):
  return type(variable) == int
  
 def isfloat(self,variable):
  return type(variable) == float
  
 def islong(self,variable):
  return type(variable) == long
  
 def isfrac(self,variable):
  return isinstance(variable,Fraccion.frac)
  
 def islist(self,rmatriz):
  return type(rmatriz) == list
  
 def istuple(self,rmatriz):
  return type(rmatriz) == tuple
  
 def isneg(self,variable):
  return variable<0
	
 def hasfloat(self):
  for fila in self.__matriz:
   for elemento in fila:
    if self.isfloat(elemento):
	 return True
  return False
	
 def mayor_nums(self):
  use_round=self.hasfloat()
  mayor=[]
  for i in self.__matriz[0]:
   mayor.append(0)
  for fila in self.__matriz:
   for i in range(len(fila)):
    length=len(str(abs(round(fila[i],4)))) if use_round else len(str(abs(fila[i])))
    if length>mayor[i]:
	 mayor[i]=length
  return mayor
  
 def inicializar(self,other):
  matriz=[]
  lenFila = len(other.__matriz[0])
  for fila in self.__matriz:
   matriz.append([0]*lenFila)
  return matriz[:]
  
 def isdimension_valida(self,other,operacion):
  if operacion=='*' or operacion=='/':
   return len(self.__matriz[0]) == len(other.__matriz)
  elif operacion=='+' or operacion=='-':
   return len(self.__matriz) == len(other.__matriz) and len(self.__matriz[0]) == len(other.__matriz[0])
  
 def crear_matriz_identidad(self):
  matriz=[]
  for i in range(len(self.__matriz)):
   matriz.append([])
   for j in range(len(self.__matriz[i])):
    matriz[i].append(1) if i==j else matriz[i].append(0)
  return matriz[:]
  
 def is_square(self):
  return len(self.__matriz) == len(self.__matriz[0])
  
 def inf(self):
  return float('inf')
  
 def nan(self):
  return float('nan')
  
 def isother_valido(self,other):
  return self.isint(other) or self.islong(other) or self.isfloat(other) or self.isfrac(other)
  
 def transpuesta(self):
  resultado=[]
  for i in range(len(self.__matriz[0])):
   resultado.append([])
   for j in range(len(self.__matriz)):
    resultado[i].append(self.__matriz[j][i])
  return matriz(resultado[:])
  
 def inv(self):
  if self.is_square():
   matriz_copy=[]
   for i in range(len(self.__matriz)):
    matriz_copy.append(self.__matriz[i][:])
    matriz_identidad = self.crear_matriz_identidad()
   for i in range(len(matriz_copy)):
    dividendo = float(matriz_copy[i][i])
    for j in range(len(matriz_copy[i])):
	 if dividendo == 0:
	  raise Exception('Matriz no invertible')
	 else:
	  matriz_copy[i][j]/=dividendo
	  matriz_identidad[i][j]/=dividendo
    for k in range(len(matriz_copy)):
	 if k!=i:
	  multiplicador=matriz_copy[k][i]
	  for l in range(len(matriz_copy[k])):
	   matriz_copy[k][l]-=multiplicador*matriz_copy[i][l]
	   matriz_identidad[k][l]-=multiplicador*matriz_identidad[i][l]
   return matriz(matriz_identidad[:])
  else:
   raise Exception('Matrix must be square')
   
 def det(self):
  if self.is_square():
   length,lim,sum1,sum2=len(self.__matriz),len(self.__matriz)-1,0,0
   for i in range(length if length > 2 else 1):
    mult1,mult2=1,1
    for j in range(length):
	 mult1*=self.__matriz[j][(j+i)%length]
	 mult2*=self.__matriz[j][(lim+i-j)%length]
    sum1+=mult1
    sum2+=mult2
   return sum1-sum2
  else:
   raise Exception('Matrix must be square')
   
 def potenciar(self,num1,num2):
  return num1**num2
  
 def multiplicar(self,num1,num2):
  return num1*num2
  
 def dividir(self,num1,num2):
  if num2 == 0:
   return float('inf')
  else:
   return num1/float(num2)
   
 def sumar(self,num1,num2):
  return num1+num2
  
 def restar(self,num1,num2):
  return num1-num2
  
 def calcular(self,other,operador):
  switch={'**':self.potenciar,'*':self.multiplicar,'/':self.dividir,'+':self.sumar,'-':self.restar}
  if isinstance(other,matriz) or self.islist(other) or self.istuple(other):
   matriz_other=matriz(other) if self.islist(other) or self.istuple(other) else other
   if self.isdimension_valida(matriz_other,operador):
    resultado=matriz(self.inicializar(matriz_other))
    for i in range(len(resultado.__matriz)):
	 for j in range(len(resultado.__matriz[i])):
	  if operador=='*':
	   for k in range(len(self.__matriz[i])):
	    resultado.__matriz[i][j]+=switch[operador](self.__matriz[i][k],matriz_other[k][j])
	  elif operador=='+' or operador=='-':
	   resultado.__matriz[i][j]=switch[operador](self.__matriz[i][j],matriz_other[i][j])
    return resultado
   else:
    raise Exception('Inner matrix dimensions must agree')
  elif self.isother_valido(other):
   resultado=matriz(self.inicializar(self))
   for i in range(len(resultado.__matriz)):
    for j in range(len(resultado.__matriz[i])):
	 resultado.__matriz[i][j]=switch[operador](self.__matriz[i][j],other)
   return resultado
  else:
   raise TypeError
   
 def __str__(self):
  if self.isvacia(self.__matriz[0]):
   return '\n[]\n'
  else:
   use_round=self.hasfloat()
   cadena='\n'
   mayor=self.mayor_nums()
   for fila in self.__matriz:
    for i in range(len(fila)):
	 if self.isneg(fila[i]):
	  elemento=str(abs(round(fila[i],4))).ljust(mayor[i],'0') if use_round else str(abs(fila[i])).ljust(mayor[i],' ')
	  cadena+='-'+elemento+'   '
	 else:
	  elemento=str(round(fila[i],4)).ljust(mayor[i],'0')if use_round else str(fila[i]).ljust(mayor[i],' ')
	  cadena+=' '+elemento+'   '
    cadena+='\n'
   return cadena
   
 def __getitem__(self,key):
  try:
   return self.__matriz[key]
  except IndexError, ex:
   print "IndexError:", ex
  except TypeError, ex:
   print "TypeError:", ex
   
 def __len__(self):
  return len(self.__matriz)
  
 def __calcular_pow(self,matriz_self,matriz_other):
  if len(matriz_self[0]) == len(matriz_other):
   resultado=matriz(self.inicializar(matriz_other))
   for i in range(len(resultado)):
    for j in range(len(resultado[i])):
	 for k in range(len(matriz_self[i])):
	  resultado[i][j]+=matriz_self[i][k]*matriz_other[k][j]
   return resultado
  else:
   raise Exception('Inner matrix dimensions must agree')
   
 def __pow__(self,other):
  if isinstance(other,matriz):
   raise Exception('Inputs must be a scalar')
  elif self.isother_valido(other):
   if self.is_square():
    if self.isint(other) or self.isfloat(other):
	 matriz_self=self.inv() if self.isneg(other) else self;
	 resul=matriz_self
	 cont=1
	 while(cont<abs(other)):
	  resul=self.__calcular_pow(matriz_self,resul)
	  cont+=1
	 return resul
    else:
	 raise TypeError, 'unsupported operand type for **: '+str(type(other))
   else:
    raise Exception('Inputs must be  a square matrix')
 
 def __mul__(self,other):
  return self.calcular(other,'*')
   
 def __rmul__(self,other):
  return self.calcular(other,'*')
   
 def __div__(self,other):
  return self.calcular(other.inv(),'*') if isinstance(other,matriz) else self.calcular(other,'/')
  
 def __rdiv__(self,other):
  if self.isother_valido(other):
   matriz_self = self.inv()
   resultado=matriz(self.inicializar(matriz_self))
   for i in range(len(resultado.__matriz)):
    for j in range(len(resultado.__matriz[i])):
	 resultado.__matriz[i][j]=matriz_self[i][j]*other
   return resultado
  else:
   raise TypeError
   
 def __add__(self,other):
  return self.calcular(other,'+')
  
 def __radd__(self,other):
  return self.calcular(other,'+')
  
 def __sub__(self,other):
  return self.calcular(other,'-')
  
 def __rsub__(self,other):
  if isinstance(other,matriz) or self.islist(other) or self.istuple(other):
   matriz_other=matriz(other) if self.islist(other) or self.istuple(other) else other
   if self.isdimension_valida(matriz_other,'-'):
    resultado=matriz(self.inicializar(matriz_other))
    for i in range(len(resultado.__matriz)):
	 for j in range(len(resultado.__matriz[i])):
	  resultado.__matriz[i][j]=self.sumar(self.__matriz[i][j]*-1,matriz_other[i][j])
    return resultado
   else:
    raise Exception('Inner matrix dimensions must agree')
  elif self.isother_valido(other):
   resultado=matriz(self.inicializar(self))
   for i in range(len(resultado.__matriz)):
    for j in range(len(resultado.__matriz[i])):
	 resultado.__matriz[i][j]=self.sumar(self.__matriz[i][j]*-1,other)
   return resultado
  else:
   raise TypeError

   
class eq(matriz):
 def __init__(self,coef,resul,var='x'):
  matriz.__init__(self,coef)
  var = self.det_vars(var,len(self._matriz__matriz[0]))
  if self.is_square():
   if self.iseq_valida(var,resul):
    self.resul = self.asignar_resul(resul)
    self.var = var
   else:
    raise Exception('Datos incorrectos')
  else:
   raise Exception('Coef\'s matrix must be square')
 
 def iseq_valida(self,var,resul):
  if self.isvalido_resul(resul) and len(self._matriz__matriz)==len(resul):
   return True if self.isvalido_var(var) and len(self._matriz__matriz[0])==len(var) else False
  else:
   return False
	
 def isvalido_resul(self,resul):
  if self.islist(resul):
   for elemento in resul:
    if not (self.isint(elemento) or self.islong(elemento) or self.isfloat(elemento) or self.isfrac(elemento)):
	 return False
   return True
  else:
   return False
   
 def isvalido_var(self,var):
  if self.islist(var):
   for elemento in var:
    if not self.isstr(elemento):
	 return False
   return True
  else:
   return False
   
 def det_vars(self,var,length):
  if self.isstr(var):
   lista=[]
   for i in range(length):
    lista.append(var+str(i+1))
   return lista[:]
  else:
   return var[:]
   
 def asignar_resul(self,resul):
  lista=[]
  for elemento in resul:
   lista.append([elemento])
  return lista[:]
  
 def isstr(self,variable):
  return type(variable) == str
  
 def solve(self):
  inversa=self.inv()
  inv_x_resul=inversa*self.resul[:]
  resultado=[]
  for elemento in inv_x_resul[:]:
   resultado.append(round(elemento[0],12))
  return resultado[:]
  
 def __str__(self):
  cadena='\n'
  mayor=self.mayor_nums()
  for i in range(len(self._matriz__matriz)):
   for j in range(len(self._matriz__matriz[i])):
    if self.isneg(self._matriz__matriz[i][j]):
	 cadena+=('-' if j==0 else ' - ')+(str(abs(self._matriz__matriz[i][j]))+self.var[j]).ljust(mayor[j]+len(self.var[j]),' ')
    else:
	 cadena+=(' ' if j==0 else ' + ')+(str(self._matriz__matriz[i][j])+self.var[j]).ljust(mayor[j]+len(self.var[j]),' ')
   cadena+=' = '+str(self.resul[i][0])+'\n'
  return cadena