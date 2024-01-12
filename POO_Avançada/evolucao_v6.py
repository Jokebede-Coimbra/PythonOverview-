from abc import ABCMeta, abstractproperty

class Humano(metaclass=ABCMeta):
    # atributo de classe
    especie = 'Homo Sapiens'
    
    def __init__(self, nome):
        self.nome = nome
        self._idade = None
    
    @abstractproperty
    def inteligente(self):
        pass
    
    @property    
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError('Idade deve ser um número psitivo')
        self._idade = idade
    
    def das_cavernas(self):
        self.especie = 'Homo Neanderxxxx'     
        
    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)
    
    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]

class Neanderthal(Humano):
    especie = Humano.especies()[-2]
    
    @property
    def inteligente(self):
        return False

class HomoSapiens(Humano):
    especie = Humano.especies()[-1]
    
    @property
    def inteligente(self):
        return True 
        
if __name__ == '__main__':
    

    try:
        anonimo = Humano('John Toe')  
        print(anonimo.inteligente)
    except TypeError:
        print('classe abstrata')    

    jose = HomoSapiens('José')
    print(f'{jose.nome}, da classe {jose.__class__.__name__}, {jose.inteligente}')
    
    grogn = Neanderthal('Grogn')
    print(f'{grogn.nome}, da classe {grogn.__class__.__name__}, {grogn.inteligente}')
    
  