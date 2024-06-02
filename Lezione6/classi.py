class Person:
  
  def __init__(self, name, age):
   self.name = name
   self.age = age
   

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(bob.age)

if bob.age == alice.age:
  print(f"Bob e Alice hanno la stessa età.")
elif bob.age > alice.age:
  print(bob.age)
else:
  print(alice.age)

michele = Person("Michele", 25)
people = [ bob,
          alice,
          Person("Vincenzo", 24), 
          michele,
          Person("Carmen", 42)
        ]
vincenzo = people[2]
print(vincenzo.name, people[2].age)
#people[2].age = 13
print(vincenzo.age)

giovane = people[0]
for person in people:
  if person.age < giovane.age:
    giovane = person
print(giovane.name, giovane.age)
