import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Evita problemes de CORS amb el FrontEnd

def obtenir_resposta_json(missatge_usuari):
    try:
        # Obrim el fitxer faqs.json que tenim al repositori de GitHub
        with open('faqs.json', 'r', encoding='utf-8') as f:
            faqs = json.load(f)
        
        msg = missatge_usuari.lower()
        id_buscada = None
        
        # Lògica intel·ligent de mapatge de paraules clau de la LAN Party
        if "conect" in msg or "red" in msg or "xarxa" in msg:
            id_buscada = 1
        elif "cable" in msg:
            id_buscada = 2
        elif "periferic" in msg or "raton" in msg or "teclado" in msg or "cascos" in msg:
            id_buscada = 3
        elif "corriente" in msg or "enchufe" in msg or "regleta" in msg or "electricitat" in msg:
            id_buscada = 4
        elif "nevera" in msg or "ventilador" in msg:
            id_buscada = 5
        elif "valor" in msg or "segur" in msg or "robar" in msg or "perdre" in msg:
            id_buscada = 6
            
        # Busquem la resposta corresponent a la ID trobada dins del JSON array
        if id_buscada is not None:
            for faq in faqs:
                if faq["id"] == id_buscada:
                    return faq["respuesta"]
                    
        return "Ho sento, no tinc informació exacta sobre aquesta consulta de la LAN Party. Prova preguntant per 'red', 'cable', 'perifèrics' o 'corrent'."
            
    except FileNotFoundError:
        return "Error intern: No s'ha trobat el fitxer faqs.json al servidor."
    except json.JSONDecodeError:
        return "Error intern: El fitxer JSON de la LAN Party té un format erroni."
    except Exception as e:
        return f"Error inesperat: {str(e)}"

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    try:
        dades = request.get_json()
        if not dades or 'message' not in dades:
            return jsonify({'reply': 'Error: Petició buida o incorrecta.'}), 400
            
        missatge_usuari = dades['message']
        
        # Truquem a la funció que llegeix el fitxer de dades JSON de GitHub
        resposta_final = obtenir_resposta_json(missatge_usuari)
        
        return jsonify({'reply': resposta_final}), 200
        
    except Exception as e:
        return jsonify({'reply': 'S’ha produït un error crític processant la petició.'}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)