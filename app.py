from flask import Flask, render_template, request
import os
from supabase import create_client

app = Flask(__name__)

# 🔐 Variáveis de ambiente (Render)
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# ⚠️ Segurança básica para evitar crash no deploy
if not SUPABASE_URL or not SUPABASE_KEY:
    print("ERRO: SUPABASE_URL ou SUPABASE_KEY não configuradas!")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# 🏠 Página inicial
@app.route("/")
def index():
    return render_template("index.html")


# 📩 Envio do formulário
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

    # 💾 Inserir no Supabase
    try:
        supabase.table("respostas").insert(dados).execute()
    except Exception as e:
        print("Erro ao salvar no Supabase:", e)

    return render_template("sucesso.html")


# 🚀 Render precisa disso (PORT obrigatório)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)