class Carta:
    def __init__(self, codigo, descripcion, remitente, destinatario):
        self.codigo = codigo
        self.descripcion = descripcion
        self.remitente = remitente
        self.destinatario = destinatario    

class Buzon:
    def __init__(self, nro):
        self.nro = nro
        self.cartas = [] 

    def agregar_carta(self, carta):
        self.cartas.append(carta)

    def contar_cartas_destinatario(self, destinatario):
        return sum(1 for carta in self.cartas if carta.destinatario == destinatario)

    def eliminar_carta_por_codigo(self, codigo):
        self.cartas = [carta for carta in self.cartas if carta.codigo != codigo]

    def remitentes_con_cartas(self):
        return set(carta.remitente for carta in self.cartas)

    def buscar_palabra_clave(self, palabra_clave):
        coincidencias = []
        for carta in self.cartas:
            if palabra_clave.lower() in carta.descripcion.lower():
                coincidencias.append((carta.codigo, carta.remitente, carta.destinatario))
        return coincidencias

buzon1 = Buzon(nro="001")
buzon2 = Buzon(nro="002")

carta1 = Carta("c456", "Querido amigo, te extraño mucho.", "Alice", "Bob")
carta2 = Carta("c789", "Hola Bob, espero que estés bien.", "Charlie", "Bob")
carta3 = Carta("c123", "Estimado Alice, nos vemos pronto.", "Bob", "Alice")
carta4 = Carta("c321", "Querido Charlie, gracias por tu apoyo.", "Alice", "Charlie")
carta5 = Carta("c654", "Hola Alice, te envío un abrazo.", "Bob", "Alice")
carta6 = Carta("c987", "Querido amigo, el amor es maravilloso.", "Charlie", "Bob")

buzon1.agregar_carta(carta1)
buzon1.agregar_carta(carta2)
buzon1.agregar_carta(carta3)
buzon2.agregar_carta(carta4)
buzon2.agregar_carta(carta5)
buzon2.agregar_carta(carta6)

print("Cartas para Bob en buzón 1:", buzon1.contar_cartas_destinatario("Bob"))
print("Cartas para Alice en buzón 2:", buzon2.contar_cartas_destinatario("Alice"))
print("Remitentes con cartas en buzón 2:", buzon2.remitentes_con_cartas())
print("Buscar palabra 'amigo' en buzón 2:", buzon2.buscar_palabra_clave("amigo"))

buzon1.eliminar_carta_por_codigo("c789")
print("Cartas restantes en buzón 1:", [c.codigo for c in buzon1.cartas])
