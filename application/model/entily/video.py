class Video():
    def __init__(self):
        self.id = None
        self.urlVideo = None
        self.urlCapa = None
        self.titulo = None
        self.categoria = None
        self.descricao = None
        self.dataPublicacao = None
        self.visualizacoes = None
        self.curtidas = None

    def setId(self,id):
        self.id = id
    def getId(self):
        return self.id
    def setUrlVideo(self,urlVideo):
        self.urlVideo = urlVideo
    def getUrlVideo(self):
        return self.urlVideo
    
    def setUrlCapa(self,urlCapa):
        self.urlCapa = urlCapa

    def getUrlCapa(self):
        return self.urlCapa
    
    def setTitulo(self,titulo):
        self.titulo = titulo

    def getTitulo(self):
        return self.titulo

    def setCategoria(self,categoria):
        self.categoria = categoria
    def getCategoria(self):
        return self.categoria
    
    def setDescricao(self,descricao):
        self.descricao = descricao

    def getDescricao(self):
        return self.descricao

    def setDataPublicacao(self,dataPublicacao):
        self.dataPublicacao = dataPublicacao
    
    def getDataPublicacao(self):
        return dataPublicacao
    
    def setVisualizacoes(self,visualizacoes):
        self.visualizacoes = visualizacoes
    
    def getVisualizacoes(self):
        return self.visualizacoes
    
    def setCurtidas(self,curtidas):
        self.curtidas = curtidas
    
    def getCurtidas(self):
        return self.curtidas
    