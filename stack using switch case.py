class user_difine_stack_oprations:
 def __init__(self,initial_stack):
  self.initial_stack=initial_stack
 def stack_isempty(self):
  if len(self.initial_stack)==0:
    print("-----> STACK IS EMPTY \n")
 else:
 print("-----> STACK IS NOT EMPTY\n")
 def push_elements(self,value_for_push):
  self.value_for_push=value_for_push
 self.initial_stack.append(value_for_push)
 print("-----> SUCCESSFULLY OPRATION PUSH\n")
 
 def display_stack(self):
  print("\n-----> UPDATED STACK : \n")
 for x in reversed(self.initial_stack):
  print(" ",x)
 
 def pop_element(self,enter):
  self.enter=enter
 if enter=='1':
  self.initial_stack.pop()
 print("-----> ELEMENT POP SUCCESSFULLY ")
 else:
 print("-----> YOU ENTERED WRONG NUMBER ")
stack1=['dolar','rajesh','jain','paddhariya']
obj1=user_difine_stack_oprations(stack1)
while True:
 print("-----> ENTER YOUR CHOICE :")
 choice=input("\n1.DISPLAY STACK\n2.STACK EMPTY?\n3.PUSH\n4.POP\n0.EXIT\n-----> choice :")
 if choice=='1':
  obj1.display_stack()
 elif choice=='2':
  obj1.stack_isempty()
 elif choice=='3':
  obj1.push_elements(value_for_push=input("-----> ENTER value YOU WANT TO PUSH :"),) 
 elif choice=='4':
  obj1.pop_element(enter=input("-----> ENTER 1 IF YOU WANT TO POP ELEMENT FROM STACK :"))
 elif choice=='0':
     break 