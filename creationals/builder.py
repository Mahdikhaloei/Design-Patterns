"""
    Builder:
        is a creational design pattern that lets you construct complex objects step by step.
        The pattern allows you to produce different types and representations of an object
        using the same construction code.
"""
class Programmer:
    def __init__(self):
        self.name = None
        self.skills = {
            'languages': [],
            'frameworks': [],
            'databases': [],
            'tools': []
        }

    def set_name(self, name):
        self.name = name

    def add_skill(self, category, skill):
        if category in self.skills:
            if isinstance(skill, list):
                self.skills[category].extend(skill)
            else:
                self.skills[category].append(skill)
        else:
            raise ValueError(f"Invalid skill category: {category}")

    def __str__(self):
        skills_str = '\n'.join([f"{category.capitalize()}: {', '.join(skills)}"
                                for category, skills in self.skills.items()])
        return f"Name: {self.name}\n{skills_str}"


class ProgrammerBuilder:
    def __init__(self):
        self.programmer = Programmer()

    def set_name(self, name):
        self.programmer.set_name(name)

    def add_skill(self, category, skill):
        self.programmer.add_skill(category, skill)

    def get_programmer(self):
        return self.programmer


# example
builder = ProgrammerBuilder()
builder.set_name("Mahdi Khaloei")
builder.add_skill("languages", "Python")
builder.add_skill("frameworks", ["Django", "Django Rest Framework"])
builder.add_skill("databases", ["PostgreSQL", "MongoDB", "redis"])
builder.add_skill("tools", ["Git", "celery", "Docker", "nginx"])

programmer = builder.get_programmer()
print(programmer)