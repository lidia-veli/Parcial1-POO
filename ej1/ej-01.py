class Libro:
    def __init__(self, titulo, autor, isbn, paginas,clasificacion):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.clasificacion = clasificacion

    def __str__(self):
        return f"Titulo: {self.titulo}, autor: {self.autor}"

    def __long__(self):
        return self.paginas

