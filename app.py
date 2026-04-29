from flask import Flask, render_template, request
import os
from supabase import create_client

app = Flask(__name__)

# Pegando variáveis de ambiente (Render)
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    dados = {
        "q1": request.form.get("q1"),
        "q2": request.form.get("q2"),
        "q3": request.form.get("q3"),
        "q4": request.form.get("q4"),
        "q5": request.form.get("q5"),
        "q6": request.form.get("q6"),
        "q7": request.form.get("q7"),
        "q8": request.form.get("q8"),
        "q9": request.form.get("q9"),
        "q10": request.form.get("q10")
    }

    # Inserir no Supabase
    supabase.table("respostas").insert(dados).execute()

    return render_template("sucesso.html")

if __name__ == "__main__":
    app.run()