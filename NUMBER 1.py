class Family:
    def __init__(self, mother, father, children):
        self.mother = mother
        self.father = father
        self.children = children

    def get_mother(self):
        return self.mother

    def get_father(self):
        return self.father

    def get_children(self):
        return self.children

my_family = Family("Jane", "John", ["Alice", "Bob", "Eve"])

print("Mother:", my_family.get_mother())
print("Father:", my_family.get_father())
print("Children:", my_family.get_children())
