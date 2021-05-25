class Animal_Shelter:
    def __init__(self):
    
        self.cats=Queue()
        self.dogs=Queue()

    def enqueue(self,animal_name,animal_type):

        if animal_type.upper() == 'CAT':
            new_animal=Cat(animal_name)
            self.cats.enqueue(new_animal)
        elif animal_type.upper()  == 'DOG':
            new_animal=Dog(animal_name)
            self.dogs.enqueue(new_animal)
        else :
            return None



    def dequeue(self,animal_type):

        if animal_type.upper() == 'CAT':
            return self.cats.dequeue()
        elif animal_type.upper() == 'DOG':
            return self.dogs.dequeue()
        else :
            return None


class Cat:
    def __init__(self,value):
        self.value=value
        self.type="cat"
        self.next=None

class Dog:
    def __init__(self,value):
        self.value=value
        self.type="dog"
        self.next=None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,new_animal):

        new_node = new_animal
        if not self.front and not self.rear:
            self.front = new_node
            self.rear = new_node
        old_rear = self.rear
        self.rear = new_node
        old_rear.next = self.rear

        

    def dequeue(self):

        first_node = self.front
        self.front = self.front.next
        return first_node.value


    def __str__(self):

        output = ''
        current = self.front
        while current: 
            output += f"<{current.value}->"
            current = current.next
        output += f"{current}"
        return output