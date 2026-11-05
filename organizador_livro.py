import os
from groq import Groq

# Inicializa o cliente da Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """
Você é um Editor Literário e Organizador de Conteúdo especialista.

Sua tarefa é receber anotações brutas, ideias soltas, frases desconexas e rascunhos de um autor e organizá-los de forma clara e estruturada.

Regras de Organização:
1. Agrupe ideias similares por temas (ex: Personagens, Enredo, Mentes/Anotações, Capítulos, etc.).
2. Crie uma ordem lógica de leitura.
3. Melhore a clareza das frases sem perder a essência ou o tom do autor.
4. Crie um pequeno Sumário/Índice no início da resposta.
"""

def executar_organizador():
    print("==========================================================")
    print("  📚 STORYCRAFT AI - ORGANIZADOR DE IDEIAS E LIVROS      ")
    print("  Transforme suas ideias bagunçadas em capítulos claros   ")
    print("==========================================================")
    print("(Digite 'sair' a qualquer momento para encerrar)")

    while True:
        print("\n-----------------------------------------------------------")
        print("💡 Cole suas ideias soltas, frases ou anotações brutas abaixo:")
        texto_bruto = input("\n> ")

        if texto_bruto.lower() in ['sair', 'exit', 'quit']:
            print("\n👋 Boas escritas! Até a próxima! 📚")
            break

        if not texto_bruto.strip():
            print("\n❌ Por favor, cole ou digite alguma anotação.")
            continue

        print("\n⏳ StoryCraft AI organizando o seu texto...")

        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"Organize o seguinte rascunho:\n\n{texto_bruto}"}
                ],
                model="llama-3.3-70b-versatile",
            )

            print("\n📖 ---------------- ESTRUTURA ORGANIZADA ----------------")
            print(chat_completion.choices[0].message.content)
            print("---------------------------------------------------------")

        except Exception as e:
            print(f"\n❌ Erro ao conectar com o StoryCraft AI: {e}")

if __name__ == "__main__":
    executar_organizador()

