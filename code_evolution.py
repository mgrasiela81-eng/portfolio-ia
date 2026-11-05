import os
from groq import Groq

# Inicializa o cliente da Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

ARQUIVO_CODIGO = "codigo_atual.py"

SYSTEM_PROMPT = """
Você é um Engenheiro de Software Python Sênior.
Sua missão é pegar o código atual e aprimorá-lo com as instruções do usuário.
Regras:
1. Retorne SEMPRE o código Python COMPLETO.
2. Explique brevemente o que foi melhorado.
"""

def carregar_codigo():
    if os.path.exists(ARQUIVO_CODIGO):
        with open(ARQUIVO_CODIGO, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def salvar_codigo(novo_codigo):
    with open(ARQUIVO_CODIGO, "w", encoding="utf-8") as f:
        f.write(novo_codigo)

def executar_evolucao():
    print("==========================================================")
    print("  💻 CODE EVOLUTION AI - APERFEIÇOADOR DE CÓDIGO PYTHON   ")
    print("==========================================================")
    print("(Digite 'reset' para começar do zero ou 'sair' para encerrar)")

    while True:
        codigo_atual = carregar_codigo()
        
        print("\n-----------------------------------------------------------")
        if codigo_atual:
            print("📜 Existe um código salvo na memória atual!")
        else:
            print("🆕 NENHUM CÓDIGO NA MEMÓRIA. Mande sua ideia inicial!")

        pedido = input("\n💬 O que você quer adicionar ou melhorar no código?\n> ")

        if pedido.lower() in ['sair', 'exit', 'quit']:
            print("\n👋 Até a próxima! 🚀")
            break

        if pedido.lower() == 'reset':
            if os.path.exists(ARQUIVO_CODIGO):
                os.remove(ARQUIVO_CODIGO)
            print("\n🧹 Memória de código resetada com sucesso!")
            continue

        if not pedido.strip():
            continue

        texto_codigo = codigo_atual if codigo_atual else "# Nenhum código fornecido ainda."
        prompt_usuario = (
            "CÓDIGO PYTHON ATUAL DA MEMÓRIA:\n"
            f"{texto_codigo}\n\n"
            "INSTRUÇÃO DE MELHORIA / NOVO RECURSO:\n"
            f"{pedido}\n\n"
            "Reescreva e evolua este código mantendo o que funciona."
        )

        print("\n⏳ Robô refatorando o código Python...")

        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt_usuario}
                ],
                model="llama-3.3-70b-versatile",
            )

            resposta = chat_completion.choices[0].message.content

            print("\n🤖 ---------------- CÓDIGO EVOLUÍDO ----------------")
            print(resposta)
            print("-----------------------------------------------------")

            if "```python" in resposta:
                codigo_extraido = resposta.split("```python")[1].split("```")[0].strip()
                salvar_codigo(codigo_extraido)
                print(f"\n✅ Nova versão salva automaticamente em '{ARQUIVO_CODIGO}'!")

        except Exception as e:
            print(f"\n❌ Erro ao conectar com o robô: {e}")

if __name__ == "__main__":
    executar_evolucao()
