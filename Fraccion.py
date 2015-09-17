import matriz

class frac:
 def __init__(self,numerador,denominador=1):
  if self.validar(numerador) and self.validar(denominador):
   if self.isneg(denominador):
    self.__num,self.__den = -numerador,-denominador
   else:
    self.__num,self.__den = numerador,denominador
   self.simplificar(False)
  else:
   raise TypeError
  
 def validar(self,variable):
  try:
   float(variable)
   return self.isint(variable) or self.islong(variable)
  except OverflowError:
   raise OverflowError
  
 def isinf(self,variable):
  return abs(variable) == float('inf')
  
 def isint(self,variable):
  return type(variable) == int
  
 def isfloat(self,variable):
  return type(variable) == float
  
 def islong(self,variable):
  return type(variable) == long
  
 def istuple(self,variable):
  return type(variable) == tuple
  
 def ismatriz(self,variable):
  return isinstance(variable,matriz.matriz)
  
 def isfrac(self,variable):
  return isinstance(variable,frac)
  
 def isneg(self,variable):
  return variable<0
  
 def istype_cmp(self,other):
  return self.isint(other) or self.isfloat(other) or self.islong(other) or self.isfrac(other)
  
 def simplificar(self,retornar=True):
  if self.__num==0:
   if retornar:
    return 0
  elif self.__den==0:
   if retornar:
    return float('inf')
  else:
   mcd=self.__mcd(self.__num,self.__den)
   self.__num,self.__den=self.__num/mcd,self.__den/mcd
   if retornar:
    return frac(self.__num,self.__den)
	
 def __mcd(self,num,den):
  num,den = abs(num),abs(den)
  if(num < den):
   num,den = den,num
  while(den != 0):
   residuo = num%den
   num,den = den,residuo
  return num
  
 def get_num(self):
  return self.__num
 
 def get_den(self):
  return self.__den
  
 def __trypow(self,base,potencia):
  try:
   potencia = float(potencia[0]/float(potencia[1])) if self.istuple(potencia) else float(potencia) if self.isint(potencia) else potencia
  except:
   raise Exception('Error al potenciar')
  if self.isfloat(potencia):
   try:
    return base**potencia
   except OverflowError,ZeroDivisionError:
    return float('inf')
   except ValueError,ex:
    raise ex
  else:
   raise Exception('Error al potenciar')
  
 def potenciar(self,other,metodo):
  if metodo==1:
   return self.__trypow(self.__num,(other.__num,other.__den)),self.__trypow(self.__den,(other.__num,other.__den))
  elif metodo==2:
   return self.__trypow(self.__num,other),self.__trypow(self.__den,other)
  elif metodo==3:
   raise TypeError, 'unsupported operand type for **: '+str(type(other))
  else:
   raise Exception('Error al potenciar')
   
 def multiplicar(self,other,metodo):
  if metodo==1:
   return self.__num*float(other.__num),self.__den*float(other.__den)
  elif metodo==2:
   return self.__num*float(other),self.__den
  elif metodo==3:
   return other*self
  else:
   raise Exception('Error al multiplicar')
   
 def dividir(self,other,metodo):
  if metodo==1:
   return self.__num*float(other.__den),self.__den*float(other.__num)
  elif metodo==2:
   return self.__num,self.__den*float(other)
  elif metodo==3:
   other = other.inv()
   return other*self
  else:
   raise Exception('Error al dividir')
   
 def sumar(self,other,metodo):
  if metodo==1:
   return (self.__num*float(other.__den))+(other.__num*float(self.__den)),self.__den*float(other.__den)
  elif metodo==2:
   return self.__num+(other*float(self.__den)),self.__den
  elif metodo==3:
   return other+self
  else:
   raise Exception('Error al sumar')
   
 def restar(self,other,metodo):
  if metodo==1:
   return (self.__num*float(other.__den))-(other.__num*float(self.__den)),self.__den*float(other.__den)
  elif metodo==2:
   return self.__num-(other*float(self.__den)),self.__den
  elif metodo==3:
   #Revisar posible error
   return (other*-1)+self
  else:
   raise Exception('Error al restar')
   
 def return_resultado(self,fraccion):
  numerador,denominador=fraccion
  if self.isinf(numerador) or self.isinf(denominador):
   return numerador/denominador
  elif numerador%1!=0 or denominador%1!=0:
   return numerador/denominador
  else:
   return frac(int(numerador),int(denominador)).simplificar()
   
 def calcular(self,other,operador):
  switch={'**':self.potenciar,'*':self.multiplicar,'/':self.dividir,'+':self.sumar,'-':self.restar}
  if isinstance(other,frac):
   return self.return_resultado(switch[operador](other,1))
  elif self.isint(other) or self.islong(other):
   return self.return_resultado(switch[operador](other,2))
  elif self.ismatriz(other):
   return switch[operador](other,3)
  elif self.isfloat(other):
   resul_num,resul_den=switch[operador](other,2)
   return resul_num/resul_den
  else:
   raise TypeError
   
 def __str__(self):
  if self.islong(int(self.__num)):
   if self.islong(int(self.__den)):
    return '%e/%e'%(self.__num,self.__den)
   else:
    return '%e'%self.__num if self.__den==1 else '%e/%d'%(self.__num,self.__den)
  elif self.islong(int(self.__den)):
   return '%d/%e'%(self.__num,self.__den)
  else:
   return '%d'%self.__num if self.__den==1 else '%d/%d'%(self.__num,self.__den)
   
 def __abs__(self):
  return frac(abs(self.__num),abs(self.__den))
  
 def __float__(self):
  return self.__num/float(self.__den)
  
 def __eq__(self,other):
  if self.istype_cmp(other):
   resta=self-other
   if isinstance(resta,frac):
    return resta.__num==0
   else:
    return resta==0
  else:
   return False
  
 def __ne__(self,other):
  return not (self==other)
  
 def __lt__(self,other):
  if self.istype_cmp(other):
   resta=self-other
   if isinstance(resta,frac):
    return resta.__num<0
   else:
    return resta<0
  else:
   raise TypeError, str(type(other))+' no es compatible'
   
 def __gt__(self,other):
  if self.istype_cmp(other):
   resta=self-other
   if isinstance(resta,frac):
    return resta.__num>0
   else:
    return resta>0
  else:
   return TypeError, str(type(other))+' no es compatible'
   
 def __le__(self,other):
  return (self<other) or (self==other)
  
 def __ge__(self,other):
  return (self>other) or (self==other)
  
 def __pow__(self,other):
  return self.calcular(other,'**')
   
 def __rpow__(self,other):
  if self.isint(other) or self.islong(other) or self.isfloat(other):
   return self.__trypow(other,(self.__num,self.__den))
  else:
   raise TypeError
  
 def __mul__(self,other):
  return self.calcular(other,'*')
   
 def __rmul__(self,other):
  return self.calcular(other,'*')
  
 def __div__(self,other):
  return self.calcular(other,'/')
   
 def __rdiv__(self,other):
  if self.isint(other) or self.islong(other):
   return self.return_resultado((self.__den*float(other),self.__num))
  elif self.isfloat(other):
   resul_num,resul_den=self.__den*float(other),self.__num
   return resul_num/resul_den
  else:
   raise TypeError
  
 def __add__(self,other):
  return self.calcular(other,'+')
  
 def __radd__(self,other):
  return self.calcular(other,'+')
  
 def __sub__(self,other):
  return self.calcular(other,'-')
  
 def __rsub__(self,other):
  if self.isint(other) or self.islong(other):
   return self.return_resultado(((other*float(self.__den))-self.__num,self.__den))
  elif self.isfloat(other):
   resul_num,resul_den = (other*float(self.__den))-self.__num,self.__den
   return resul_num/resul_den
  else:
   raise TypeError