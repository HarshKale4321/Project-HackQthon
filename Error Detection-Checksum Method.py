#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile, Aer, IBMQ
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
import numpy as np

# Loading your IBM Quantum account(s)
provider = IBMQ.load_account()


# In[ ]:


from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute , BasicAer
from qiskit.visualization import plot_histogram
from pylatexenc import *


# In[ ]:


input_signal=input(" Enter the signal")



# In[ ]:


if input_signal%2==0:
    n=len(input_signal)/2
    a=input_signal[0:n]
    b=input_signal[n:-1]
    else:
        input_signal=input_signal.insert(0,0)
        n=len(input_signal)/2
        list_a=input_signal[0:n]
        list_b=input_signal[n:-1]
    


# In[ ]:


qr=QuantumRegister(len(list_a),name="qr")
cr=ClassicalRegister(len(list_b)+1,name="cr")
qg=QuantumCircuit(qr,cr)


# In[ ]:


def module(q,i,x,a):
    q.cx(i,2*len(a)+i)
    q.cx(i+1,2*len(a)+i)
    q.measure(2*len(a)+1,x[0])
    find_carry(q,i,i+1,2*len(a)+i-1,2*len(a)+i,2*len(a)+i+1,x)
    q.cx(2*len(a)+i-1,2*len(a)+1)
    q.barrier()
    


# In[ ]:


def set_up(a,b,q,cr):
    i=len(a)-1
    while i>=0:
        if a[i]=='1':
            q.x(2*len(a)-1-i)
        i-=1
    j=len(b)-1
    while j>=0:
        if b[j]=="1":
            q.x(2*(len(b)-1-j)+1)
        j-=1
    q.barrier()
    
    q.cx(0,2*len(a))
    q.cx(1,2*len(a))
    q.ccx(0,1,2*len(a)+1)
    q.barrier()
    
    for k in range(1, len(a)):
        module(q,2*k,cr,a)
        
    m=0
    while m<len(a):
        q.measure(2*(m+len(a)),m)
        m+=1
    q.measure(4*(len(a))-1,len(a))
    

    
    


# In[ ]:


set_up(list_a,list_b,qg,cr)
qg.draw()


# In[ ]:


sum=set_up(list_a,list_b,qg,cr)
def flip(sum):
    for n in range(len(sum))
    return sum[n]=1 if (sum[n] == '0') else sum[n]=0


# In[ ]:


checksum_value= flip(sum)


# In[ ]:


checksum_signal="checksum_value"+"input_signal"


# In[ ]:


set_up(sum,checksum_signal,qg,cr)
qg.draw()


# In[ ]:


result=set_up(sum,checksum_signal,qg,cr)
if flip(result)==np.repeat(0,len(a)):
    return "No Error"
else:
    "Error Detected"

