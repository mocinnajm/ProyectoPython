class Proyecto:
    def __init__(self, nombre, duracion, lenguaje_principal):
        self.nombre = nombre
        self.duracion = duracion
        self.lenguaje_principal = lenguaje_principal
        self.equipo = None
        self.tareas = []

    def asignar_equipo(self, equipo):
        self.equipo = equipo

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def detalles(self):
        equipo = self.equipo.detalles() if self.equipo else "non tines equipo"
        tareas = "\n".join([t.detalles() for t in self.tareas]) or "non tareas"
        return f"{self.nombre} ({self.duracion} meses, {self.lenguaje_principal})\nEquipo:\n{equipo}\nTareas:\n{tareas}"


class ProyectoInterno(Proyecto):
    def __init__(self, nombre, duracion, lenguaje_principal, responsable, departamento):
        super().__init__(nombre, duracion, lenguaje_principal)
        self.responsable = responsable
        self.departamento = departamento

    def detalles(self):
        origen = super().detalles()
        return f"{origen}\nResponsable: {self.responsable}, Departamento: {self.departamento}"


class ProyectoExterno(Proyecto):
    def __init__(self, nombre, duracion, lenguaje_principal, cliente, presupuesto):
        super().__init__(nombre, duracion, lenguaje_principal)
        self.cliente = cliente
        self.presupuesto = presupuesto

    def detalles(self):
        base = super().detalles()
        return f"{base}\nCliente: {self.cliente}, Presupuesto: euros {self.presupuesto}"


class Miembro:
    def __init__(self, nombre, rol, experiencia):
        self.nombre = nombre
        self.rol = rol
        self.experiencia = experiencia

    def detalles(self):
        return f"{self.nombre} ({self.rol}, {self.experiencia} años)"


class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)

    def detalles(self):
        miembros = "\n".join([m.detalles() for m in self.miembros])
        return f"{self.nombre}:\n{miembros}"


class Tarea:
    def __init__(self, titulo, estado, responsable):
        self.titulo = titulo
        self.estado = estado
        self.responsable = responsable

    def detalles(self):
        return f"{self.titulo} ({self.estado}) - Responsable: {self.responsable.nombre}"



if __name__ == "__main__":
    print("El mejor equipo muchas gracias por vuestra aportacion")

    equipo = Equipo("equipo de mohcine")
    equipo.agregar_miembro(Miembro("Mohcine Najm", "Desarrollador", 1))
    equipo.agregar_miembro(Miembro("Redu", "Administrador", 3))

    proyecto_interno = ProyectoInterno("Desarrollo de software", 6, "Python", "Nayla Najm", "TI")
    proyecto_interno.asignar_equipo(equipo)
    proyecto_interno.agregar_tarea(Tarea("Operación de sistemas en grandes centros de datos", "En progreso", equipo.miembros[0]))
    proyecto_interno.agregar_tarea(Tarea("Definir requerimientos", "Completada", equipo.miembros[1]))

    proyecto_externo = ProyectoExterno("Desrrollo web", 12, "Php", "Prat Eduacion", 10000)
    proyecto_externo.asignar_equipo(equipo)
    proyecto_externo.agregar_tarea(Tarea("Desarrollo de backend", "En progreso", equipo.miembros[0]))

    print(proyecto_interno.detalles())
    print(proyecto_externo.detalles())
