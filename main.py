from flask import Flask,request,render_template
import pickle

modelo = pickle.load(open('modelo.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html',titulo="Sistema de Recomendação")

@app.route('/predicaoform',methods=['POST'])
def form():
    resultado = modelo.predict([[request.form['idioma'],request.form['anoLancamento'],request.form['categoria1'],request.form['categoria2'],request.form['categoria3'],request.form['categoria4']]])
    if (resultado) == 0:
        filmes = ["1 - Kids Return","2 - Broken Wings","3 - Dead Birds","4 - Rude Boy","5 - Man Who Planted Trees, The","6 - Valerie and Her Week of Wonders","7 - Babylon 5: The Gathering","8 - Private Parts","9 - Save the Green Planet!","10 - Girl Who Leapt Through Time, The"]
    if (resultado) == 1:
        filmes = ["1 - Freedom Downtime","2 - Bordertown","3 - 10 Rillington Place","4 - Shadowboxer","5 - Images","6 - Hole, The","7 - Ringu 0: Bâsudei","8 - No Turning Back","9 - Great Waldo Pepper, The","10 - Magic"]
    if (resultado) == 2:
        filmes = ["1 - Dedication","2 - Chinese Ghost Story II, A","3 - Bon Cop, Bad Cop","4 - Some Girls","5 - Samsara","6 - Azumi","7 - Undead","8 - Beowulf & Grendel","9 - Samurai Fiction","10 - Good Year, A"]
    
    return render_template('resultado.html',titulo="Top 10 dos filmes mais bem avaliados", resultado=resultado, filmes=filmes)


app.run(debug=True)