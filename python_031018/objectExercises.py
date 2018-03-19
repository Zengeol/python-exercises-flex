# This is modified after Aspen (2017)
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
         
    def greet(self, other_person):
        self.greeting_count += 1
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

    def __str__(self):
        return "Person: {} {} {}".format(self.name, self.email, self.phone)
    

    def print_contact_info(self):
        print("{name}'s Email: {email}\n{name}'s Phone Number: {phone}\n".format(
            name = self.name,
            email = self.email,
            phone = self.phone
        ))

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        return len(self.friends)

print("\n1. Instantiate an instance object of Person, sonny.")
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
print(sonny)

print("\n2. Instantiate another person Jordan.")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
print(jordan)

print("\n3. Have Sonny greet Jordan using the greet method.")
sonny.greet(jordan)

print("\n4. Have Jordan greet Sonny using the greet method.")
jordan.greet(sonny)

print("\n5. Write a print statement to print Sonny's contact info.")
sonny.print_contact_info()

print("\n6. Write another print statement to print Jordan's contact info.")
jordan.print_contact_info()

print("\n7. Add Jordan and Sonny to each others' friend lists.")
jordan.add_friend(sonny)
sonny.add_friend(jordan)
print("Sonny's friends: {}\nJordan's friends:{}".format(
    sonny.friends[0].name, jordan.friends[0].name))

print("\n8. Create a num_friends method.")
print("Jordan has", jordan.num_friends(), "friend(s).")
print("Sonny has", sonny.num_friends(), "friend(s).")