class Categoria :
    def __init__(self):
        self.id = id
        self.titulo = None
        self.descriaoo  = None
        self.capa = None
        self.videos = []

    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id
    
    def setTitulo(self,titulo):
        self.titulo = titulo

    def getTitulo(self):
        return self.titulo
    
    def setDescricao(self,descricao):
        self.descricao = descricao

    def getDescricao(self):
        return self.descricao
    def setCapa(self,capa):
        self.capa = capa
    def getCapa(self):
        return self.capa

    def setVideos(self,video):
        self.videos.append(video)

    def getVideos(self):
        return self.videos



