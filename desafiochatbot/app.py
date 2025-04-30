from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = ""

generos = {
    "comedia": ["Superbad", "O Máskara", "Se Beber, Não Case"],
    "acao": ["Mad Max: Estrada da Fúria", "John Wick", "Gladiador"],
    "romance": ["La La Land", "Orgulho e Preconceito", "Simplesmente Acontece"],
    "ficcao": ["Matrix", "Interestelar", "Blade Runner 2049"]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mensagem', methods=['POST'])
def mensagem():
    texto = request.json.get('mensagem', '').strip().lower()
    
    if texto in ['oi', 'olá', 'eae']:
        return jsonify({"resposta": "Oi! 👋 Quer uma sugestão de filme? Me diga um gênero como comédia, ação ou romance."})

    elif texto in generos:
        filmes = generos[texto]
        respostas = []
        for filme in filmes:
            info = buscar_filme(filme)
            if info:
                respostas.append(info)
        return jsonify({"resposta": respostas})

    elif len(texto) > 2:
        info = buscar_filme(texto)
        return jsonify({"resposta": info or "❌ Não encontrei esse filme."})

    return jsonify({"resposta": "❓ Não entendi. Tente digitar um gênero ou nome de filme."})


def buscar_filme(nome):
    url = f"https://www.omdbapi.com/?t={nome}&apikey={API_KEY}&language=pt-BR"
    response = requests.get(url)
    data = response.json()

    if data.get("Response") == "True":
        return f"""
            🎬 <strong>{data.get("Title")}</strong> ({data.get("Year")})<br>
            ⭐ IMDb: {data.get("imdbRating")}<br>
            🎭 Gênero: {data.get("Genre")}<br>
            📖 Sinopse: {data.get("Plot")}<br>
            <img src="{data.get("Poster")}" style="width:150px;">
        """
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
