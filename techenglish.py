import os
from groq import Groq

# Inicializa o cliente da Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """
Você é o TechEnglish AI, um professor nativo de Inglês especializado no mercado de Tecnologia, Programação e Inteligência Artificial.

Sua missão é ajudar o aluno a aprender inglês do básico ao avançado, focando em:
1. Termos técnicos de programação e TI (ex: debugging, deploy, framework, backend, loop, database).
2. Diálogos reais do dia a dia de um desenvolvedor (Daily meetings, reuniões, apresentações de projetos).
3. Correção amigável de gramática e vocabulário.

Regras de comportamento:
- Responda SEMPRE em Inglês primeiro, e logo em seguida forneça a tradução/explicação em Português para ajudar na fixação.
- Se o usuário cometer um erro de inglês, corrija-o gentilmente antes de responder.
- Explique o significado e a pronúncia aproximada de termos técnicos importantes.
- Mantenha um tom encorajador, prático e focado no mercado de trabalho de TI.
"""

def executar_techenglish():
    print("==========================================================")
    print("  🇬🇧 TECHENGLISH AI - SEU PROFESSOR DE INGLÊS PARA TI     ")
    print("  Aprenda Inglês Técnico e Pratique Conversação para TI   ")
    print("==========================================================")
    print("\n💡 Dica: Você pode conversar em inglês, pedir explicações de termos")
    print("   técnicos ou pedir frases de exemplo para entrevistas de emprego!")
    print("(Digite 'sair' a qualquer momento para encerrar)")

    while True:
        print("\n-----------------------------------------------------------")
        usuario_input = input("\n👤 Você: ")

        if usuario_input.lower() in ['sair', 'exit', 'quit']:
            print("\n👋 See you later! Continue praticando seu inglês de TI! 🚀")
            break

        if not usuario_input.strip():
            print("\n❌ Por favor, digite alguma frase ou dúvida em inglês/português.")
            continue

        print("\n⏳ TechEnglish AI preparando a aula...")

        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": usuario_input}
                ],
                model="llama-3.3-70b-versatile",
            )

            print("\n🎓 ---------------- TECHENGLISH AI ----------------")
            print(chat_completion.choices[0].message.content)
            print("---------------------------------------------------")

        except Exception as e:
            print(f"\n❌ Erro ao conectar com o TechEnglish AI: {e}")

if __name__ == "__main__":
    executar_techenglish()

