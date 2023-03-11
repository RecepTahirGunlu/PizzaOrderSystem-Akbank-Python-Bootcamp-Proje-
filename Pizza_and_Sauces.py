# Pizza sınıfını oluşturma
class Pizza:
    #Pizza sınıfının özelliklerini oluşturma
    def __init__(self, description, cost):
        self.__description = description
        self.__cost = cost

    #Pizzanın tanımı veren fonksiyon   
    def get_description(self):
        return self.__description
    
    #Pizzanın maliyetini veren fonksiyon
    def get_cost(self):
        return self.__cost
    
# Pizza sınıfı miras alan diğer pizza sınıfları   
class ClassicPizza(Pizza):
    # Üst sınıftan miras alarak sınıfın özellliklerini belirleme
    def __init__(self):
        description = "Klasik Pizza"
        cost = 99.0
        super().__init__(description, cost)
        
class MargheritaPizza(Pizza):
    def __init__(self):
        description = "Margherita Pizza"
        cost = 119.0
        super().__init__(description, cost)
        
class TurkishPizza(Pizza):
    def __init__(self):
        description = "Türk Pizza"
        cost = 109.0
        super().__init__(description, cost)
        
class PlainPizza(Pizza):
    def __init__(self):
        description = "Sade Pizza"
        cost = 99.0
        super().__init__(description, cost)

# Pizzaya sos eklemek için Pizza sınıfından miras alan Decorator'ü oluşturma
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component


class Olive(Decorator):
    def __init__(self, component):
        self.__cost = 6.0
        self.__description = "Zeytin"
        super().__init__(component)

    # Pizzanın üzerine eklenen soslarla beraber oluşan fiyatını hesaplama
    def get_cost(self):
        return self.component.get_cost() + self.__cost
    
    # Pizzanın üzerine eklenen sosları gösterme
    def get_description(self):
        return  self.component.get_description() + ' ' + self.__description


class Mushroom(Decorator):
    def __init__(self, component):
        self.__cost = 6.0
        self.__description = "Mantar"
        super().__init__(component)

    def get_cost(self):
        return self.component.get_cost() + self.__cost

    def get_description(self):
        return self.component.get_description() + ' ' + self.__description

class GoatCheese(Decorator):
    def __init__(self, component):
        self.__cost = 6.0
        self.__description = "Keçi Peyniri"
        super().__init__(component)

    def get_cost(self):
        return self.component.get_cost() + self.__cost

    def get_description(self):
        return self.component.get_description() + ' ' + self.__description
    
class Meat(Decorator):
    def __init__(self, component):
        self.__cost = 12.0
        self.__description = "Et"
        super().__init__(component)

    def get_cost(self):
        return self.component.get_cost() + self.__cost

    def get_description(self):
        return self.component.get_description() + ' ' + self.__description


class Onion(Decorator):
    def __init__(self, component):
        self.__cost = 4.5
        self.__description = "Soğan"
        super().__init__(component)

    def get_cost(self):
        return self.component.get_cost() + self.__cost

    def get_description(self):
        return self.component.get_description() + ' ' + self.__description


class Corn(Decorator):
    def __init__(self, component):
        self.__cost = 5.0
        self.__description = "Mısır"
        super().__init__(component)

    def get_cost(self):
        return self.component.get_cost() + self.__cost

    def get_description(self):
        return self.component.get_description() + ' ' + self.__description
