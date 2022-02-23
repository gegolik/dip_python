class persona:
    def _init_ (self, nombre, apellido_pat, apellido_mat, telefono, email)
        self.nombre = nombre
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat   
        self.telefono = telefono
        self.email = email
    
    def getnombre(self):
        return self.nombre
    def getapellido_pat(self):
        return self.apellido_pat
    def getapellido_mat(self):
        return self.apellido_mat
    def gettelefono(self):
        return self.telefono
    def getemail(self):
        return self.email