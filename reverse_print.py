'''
Node:
  data: value
  next: next node adress
'''

def print_linked_list_r(llist):
  if llist == None:  #base case
    return None
   else:
    print_linked_list_r(llist.next) # adding function call to the stack with the next node as a paramater before printing  the value
    print(llist.data)               # after the last function call returns None (base case) the stack will get emptied last in first out
