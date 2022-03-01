# we want to implement linked list in Python 

from itertools import count
from logging import exception, raiseExceptions


class Node:  # This first class represent the element in the linklist. It has to class memebers
             # the first is data which rep the list and next which is a pointer to the next element
    def __init__(self,data=None, next=None):
        self.data = data
        self.next =next

class LinkedList:
    def __init__(self):
        self.head = None   #we need this head variable to point to the head of the link list

    # we can start imlementing our methods 
    #method 1
    def insert_at_begining(self, data): # this will take our data linked list
        node = Node(data, self.head) #create a node with the value data and the current element will be the head
        self.head = node  #therefore our head is the node

    #Test by printing
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr =self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print (llstr)   

    def insert_at_end (self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr =self.head
        while itr.next:
            itr =itr.next
        
        itr.next = Node(data,None)

    #This new method will take a list of value as a list and create a fresh new list
    #  out all values and create a new one
    def insert_values (self, data_list):
        for data in data_list:
            self.insert_at_end(data)


    # create a function that will give the length of the link list
    def get_length (self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count


    #method to remove an element in a linked list
    def remove_at(self, index):
        if index < 0 or index >=self.get_length():
            raise exception("invalid index")
        
        if index ==0:
            self.head = self.head.next
            return

        count = 0
        itr =self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr=itr.next
            count +=1

    #method to insert an element in a linked list
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invaid index")

        if index==0:
            self.insert_at_begining(data)   #since we already have out insert method for the begining
            return

        count =0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next


    # method to insert after value
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
            
        if self.head.data==data_after :
                self.head.next = Node(data_to_insert, self.head.next)
                return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next
    
    #method to remove by value
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
        


if __name__ == '__main__':
    ll = LinkedList()
    #ll.insert_at_begining(5)
    #ll.insert_at_begining(89)
    #ll.insert_at_end(189)
    #ll.insert_values(["banana","mango", "grapes", "orange"])
    #ll.print()
    #print ("length", ll.get_length())
    #ll.remove_at(2)
    #print ("length", ll.get_length())
    #ll.insert_at(0, "figs")
    #ll.print()


    ll.insert_values(["banana","mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()