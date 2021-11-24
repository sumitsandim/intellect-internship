class Qoperations:
 def __init__(self,initial_queue):
  self.initial_queue=initial_queue
 def addQ(self):
  self.value=value=input("\nENTER VALUE FOR ADD ELEMENTS :")
  return self.initial_queue.append(value)
 def removeQ(self):
  if len(self.initial_queue)!=0:
   return self.initial_queue.pop(0)
  else:
   print("\nQueue Is Empty Already you can't remove element ")
 def displayQ(self):
  for item in self.initial_queue:
   print(item,end=" ")
 print("\n")
 def Qisempty(self):
  if len(self.initial_queue)==0:
   print("\nQueue is Empty")
  else:
   print("\nQueue is Not Empty")
Q1=[10,20,30,40,50,]
Queue1=Qoperations(Q1)
while True:
 print("\n1.Check Queue is Empty ?\n2.Add Elements to Queue\n3.Remove Elements from 
Queue\n4.Display Queue\n0.EXIT.")
 choice=input("\nEnter your choice :")
 if choice=='1':
  Queue1.Qisempty()
 elif choice=='2':
  Queue1.addQ()
 elif choice=='3':
   Queue1.removeQ()
 elif choice=='4':
  Queue1.displayQ()
 elif choice=='0':
  break