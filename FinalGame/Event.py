class Event:
    def __init__(self, title, description, characters):
        self.title = title
        self.description = description
        self.characters = characters
    
    def toString(self):
        nameList = []
        for c in self.characters:
            nameList.append(c.name)
        involved = ", ".join(nameList)
        message = f"""
--- {self.title} ---
{self.description}

Characters Involved: {involved}

"""
        return message
    def getDescription(self):
        return self.description
    
    def toDict(self):
        return {
            "title": self.title,
            "description": self.description,
            "characters": [c.name for c in self.characters]
        }
