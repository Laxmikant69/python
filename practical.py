class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push_back(self,newElement):
        newNode=Node(newElement)
        if(self.head==None):
           self.head=newNode
           return
        else:
           temp=self.head
           while(temp.next!=None):
               temp=temp.next
           temp.next=newNode



def searchElement(self,searchValue):
    temp=self.head
    found=0
    i=0

    if(temp!=None):
        while(temp!=None):
            i +=1
            if(temp.data==searchValue):
                found +=1
                break
            temp = temp.next
            if(found==1):
                print(searchValue,"is found",i)
            else:
                print(searchValue,"is not found")
        else:
            print("the list is empty")



    def PrintList(self):
        temp=self.head
        if(temp!=None):
            print("the list contain:",end="")
            while(temp!=None):
              print(temp.data,enf="")
              temp=temp.next
          print()
       else:
           print("the list is empty")





MyList=LinkedList()

MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)

MyList.PrintList()

MyList.searchValue(10)
MyList.searchValue(13)
MyList.searchValue(20)
