class Restaurante:
   Restaurantes = []
   
   # método construtor (especial)
   def __init__(self, nome, categoria):
    self._nome = nome.title()
    self._categoria = categoria.upper()
    self._ativo = False
    Restaurante.Restaurantes.append(self)
   
   # método para exibir o objeto em formato texto (especial)
   def __str__(self):
    return f"Restaurante {self._nome} | Categoria {self._categoria} | Ativo: {self.ativo}"
   
   # método para listar o restaurante (próprio)
   def listar_restaurantes():
    print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | Status')
    for restaurante in Restaurante.Restaurantes:
        print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |  {restaurante.ativo}')
   
   @property
   def ativo(self):
    return '✅' if self._ativo == True else '❌'
    
restaurante_praca = Restaurante('Praça', 'Prato Feito')

# imprime as propriedades do objeto
# print(dir(restaurante_praca))

# imprime os atributos do objeto
# print(vars(restaurante_praca))

# imprime o valor de um atributo específico
# print(restaurante_praca._nome)

# mostra o objeto em formato texto
# print(restaurante_praca)

# chama o método listar_restaurantes
Restaurante.listar_restaurantes()