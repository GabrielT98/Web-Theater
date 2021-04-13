from flask import Flask,render_template
import os
from application.model.entily.categoria import Categoria
from application.model.entily.video import Video
app = Flask(__name__)



app = Flask(__name__,template_folder=os.path.abspath('application/view/templates'),static_folder=os.path.abspath('application/view/static'))

video1 = Video()
video1.setUrlVideo("{{url_for('static',filename = 'midia/duality.mp4')}}")
video1.setUrlCapa("{{url_for('static',filename = 'img/capaduality.jpg')}}")
video1.setId(3)
video1.setTitulo("Duality")
video1.setDescricao("Musica mais famosa da banda Slipknot")
video1.setDataPublicacao("12/10/2010")
video1.setVisualizacoes(10000)
video1.setCurtidas(500)

video2 = Video()
video2.setUrlVideo("{{url_for('static',filename = 'midia/numb.mp4')}}")
video2.setUrlCapa("{{url_for('static', filename = 'img/numbcapa.jpg')}}")
video2.setId(4)
video2.setTitulo("Numb")
video2.setDescricao("Musica da banda Slipknot")
video2.setDataPublicacao("11/12/2012")
video2.setVisualizacoes(2000)
video2.setCurtidas(100)

video3 = Video()
video3.setId(5)
video3.setUrlVideo("{{url_for('static',filaneme = 'midia/De janeiro a janeiro.mp4')}}")
video3.setUrlCapa("{{url_for('static' , filename = 'img/dejaneirocapa.jpg')}}")
video3.setTitulo("De janeiro a janeiro")
video3.setDescricao("Musica de Nando Reis e Roberta Campos")
video3.setDataPublicacao("11/12/2012")
video3.setVisualizacoes(35000)
video3.setCurtidas(6700)

video4 = Video()
video4.setUrlVideo("{{url_for('static',filename='midia/PraVocêGuardeiOAmor.mp4')}}")
video4.setUrlCapa("{{url_for('static' ,filename= 'img/pravccapa.jpg')}}")
video4.setId(6)
video4.setTitulo("Pra voce guardei amor")
video4.setDescricao("Musica de Nando Reis")
video4.setDataPublicacao("17/08/2009")
video4.setVisualizacoes(34000)
video4.setCurtidas(1800)

categoria1= Categoria()
categoria1.setId(1)
categoria1.setTitulo("Rock")
categoria1.setDescricao("Assita o videos das melhores musicas de rock")
categoria1.setCapa("{{url_for('static',filename='img/rock.jpg')}}")
categoria1.setVideos(video1)
categoria1.setVideos(video2)




categoria2 = Categoria()
categoria2.setId(2)
categoria2.setTitulo("MPB")
categoria2.setDescricao("Assita a videos das melhores músicas do MPB")
categoria2.setCapa("{{url_for('static',filename='img/mpb.png')}}")
categoria2.setVideos(video3)
categoria2.setVideos(video4)



video1.setCategoria(categoria1)
video2.setCategoria(categoria1)
video3.setCategoria(categoria1)
video4.setCategoria(categoria1)



categorias =[]
categorias.append(categoria1)
categorias.append(categoria2)


print(categoria2.getId())
print(categoria2.getTitulo())
print(categoria2.getDescricao())
print(categoria1.getCapa())

for categoria in categorias:
    for video in categoria.getVideos():
        print(video.getTitulo())


@app.route('/')
def home():
    return render_template("index.html",categorias = categorias )

@app.route("/video/<id>")
def videos(id):
    for categoria in categorias :
        for video in categoria.getVideos():
            if str(video.getId) == id:
                return render_template("videos.html", video = video)
    return render_template("home.html",categorias = categorias)