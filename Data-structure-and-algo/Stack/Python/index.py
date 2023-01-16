print("******************* Stacks - push(), pop(), peek(), isEmpty(), isFull() using array")
class Stack:
    def __init__(self):
        self.stackList=[]
        self.stackSize=0
    def push(self,item):
        self.stackList.append(item)
        self.stackSize+=1
    def pop(self):
        try:
            if self.stackSize==0:
                raise Exception("Stack is Empty, returning None")
            temp=self.stackList.pop()
            self.stackSize-=1
            return temp
        except Exception as e:
            print(str(e))
    def is_empty(self):
        if len(self.stackList)==0:
            return True
        else:
            return False
    def peek(self):
        if self.stackList:
          return self.stackList[-1] # # this will get the last element of stack
        else:
          return None
    def size(self):
        return len(self.stackList)

#Execution
s=Stack()
#push element
print("1. Push element into stack!")
s.push(1)
s.push(3)
s.push(5)
s.push(2)
s.push(8)
#pop element
print("2. popped element is:")
print(s.pop())
#peek method
print("3. See first element inside stack: ")
print(s.peek())
#is_empty method
print("4. Check if stack empty or not: ")
print(s.is_empty())
#check size of stack
print("5. Length of the stack: ")
print(s.size())