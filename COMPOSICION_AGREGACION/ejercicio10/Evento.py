class Persona:
    def __init__(self, nombre, apellido, edad, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ci = ci

class Participante(Persona):
    def __init__(self, nombre, apellido, edad, ci, nroTicket):
        super().__init__(nombre, apellido, edad, ci)
        self.nroTicket = nroTicket

class Speaker(Persona):
    def __init__(self, nombre, apellido, edad, ci, especialidad):
        super().__init__(nombre, apellido, edad, ci)
        self.especialidad = especialidad
        
class Charla:
    def __init__(self, lugar, nombreCharla, nombreS, apellidoS, edadS, ciS, especialidadS, np, participantes):
        self.lugar = lugar
        self.nombreCharla = nombreCharla
        self.S = Speaker(nombreS, apellidoS, edadS, ciS, especialidadS)
        self.np = np
        self.participantes = participantes
        
    def promedioEdad(self):
        total = 0
        for p in self.participantes:
            total += p.edad
        print("\nPromedio de edad de los participantes:")
        print(total / len(self.participantes))
        print()
    
    def eliminarSpeaker(self, ci):
        for p in self.S:
            if p.ci == ci:
                self.S.remove(p)
    
        
class Evento:
    def __init__(self, nombre, nc, charlas):
        self.nombre = nombre
        self.nc = nc
        self.charlas = charlas

    def mostrar_info(self):
        print(f"\n===== EVENTO: {self.nombre} =====")
        for charla in self.charlas:
            print(f"\nCharla: {charla.nombreCharla}")
            print(f"Lugar: {charla.lugar}")
            print(f"Speaker: {charla.S.nombre} {charla.S.apellido} - {charla.S.especialidad}")
            print("Participantes:")
            for p in charla.participantes:
                print(f" - {p.nombre} {p.apellido} (Ticket {p.nroTicket})")
            print("==============================")
    
    def persona_esta(self, nombre, apellido):
        participanteX = False
        speakerX = False
        for charla in self.charlas:
            for p in charla.participantes:
                if p.nombre == nombre and p.apellido == apellido:
                    participanteX = True
        for charla in self.charlas:
            for speaker in charla.participantes:
                if speaker.nombre == nombre and speaker.apellido == apellido:
                    speakerX = True
        if participanteX:
            print(f"\nLa persona {nombre} {apellido} participa en el evento.")
        elif speakerX:
            print(f"\nLa persona {nombre} {apellido} es speaker en el evento.")
        else:
            print(f"\nLa persona {nombre} {apellido} no participa en el evento.")
        print("==============================")
    
    def speaker_no_participa(self, ci):
        speakerX = False
        for charla in self.charlas:
            for speaker in charla.speaker:
                if speaker.ci == ci:
                    speakerX = True
                if  speakerX:
                    charla.eliminarSpeaker(ci)
                    
        if speakerX:
            print(f"\nEl speaker con CI {ci} participa en el evento.")
            
        else:
            print(f"\nEl speaker con CI {ci} no participa en el evento.")
        print("==============================")
    
    def ordenar_nro_participantes(self):
        self.charlas.sort(key=lambda charla: charla.np)
        print("\nCharlas ordenadas por número de participantes:")
        for charla in self.charlas:
            print(f" - {charla.nombreCharla}: {charla.np} participantes")
        print("==============================")

p1 = Participante("Ana", "Gutiérrez", 22, "123456", 101)
p2 = Participante("Luis", "Paredes", 25, "789101", 102)

charla1 = Charla(
    "Auditorio A",
    "Introducción al Hacking Ético",
    "Carlos", "Rivas", 40, "111222", "Ciberseguridad",
    2,
    [p1, p2]
)

charla2 = Charla("Sala B", "Machine Learning", "Lucía", "Mora", 35, "555333", "IA", 5, [p1])
charla3 = Charla("Sala C", "Redes y Seguridad", "Julio", "Lopez", 45, "888777", "Networking", 1, [])


evento = Evento(
    "Tech Summit 2025",
    1,
    [charla1]
)

evento.mostrar_info()
charla1.promedioEdad()

evento = Evento("Tech Summit 2025", 3, [charla1, charla2, charla3])

evento.ordenar_nro_participantes()

evento.persona_esta("Ana", "Gutiérrez")
