from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

exercices = {
    "math": [
        "Calcule: 12 × 8",
        "Résous: x + 5 = 12",
        "Quel est le PGCD de 12 et 18 ?"
    ],
    "informatique": [
        "C’est quoi un algorithme ?",
        "Différence entre RAM et ROM ?",
        "À quoi sert Python ?"
    ],
    "reseau": [
        "Définition d’une adresse IP",
        "C’est quoi le modèle OSI ?",
        "Différence TCP / UDP ?"
    ]
}

history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message", "").lower().strip()

        if not user_message:
            return jsonify({"reply": "❓ Message vide !"})

        if "math" in user_message:
            reply = random.choice(exercices["math"])

        elif "info" in user_message:
            reply = random.choice(exercices["informatique"])

        elif "reseau" in user_message:
            reply = random.choice(exercices["reseau"])

        elif "bonjour" in user_message or "salut" in user_message:
            reply = "👋 Bonjour ! Choisis un domaine: math, info, réseau."

        else:
reply = "❓ Écris un domaine: math / info / reseau"
        history.append({
            "user": user_message,
            "bot": reply
        })

        return jsonify({"reply": reply})

    except Exception:
        return jsonify({"reply": "⚠️ Erreur serveur"})

if __name__ == "__main__":
    app.run(debug=True)