from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, category = "Electronics", condition = 0, age = None):
        super().__init__(category ,condition, age)
        
        
    def __str__(self):
        return "A gadget full of buttons and secrets."
    
    def condition_description(self):
        super().condition_description(self)