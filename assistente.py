import os
from groq import Groq

# Inicializa o cliente usando a chave Groq salva
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

print("==================================================")
print("  🤖 ASSISTENTE DE IA NO TERMUX - CI&T PROJECT   ")
print("  Modelo: Llama 3.3 (Rodando via Groq)           ")
print("  Digite 'sair' para encerrar a conversa.         ")
print("==================================================")

while True:
    pergunta = input("\nVocê: ")
    
    if pergunta.lower() in ['sair', 'exit', 'quit']:
        print("Até mais! Projeto finalizado.")
        break
        
    if not pergunta.strip():
        continue

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": pergunta}
            ],
            model="llama-3.3-70b-versatile",
        )
        print(f"\nIA: {chat_completion.choices[0].message.content}")
    except Exception as e:
        print(f"\nErro ao se conectar com a IA: {e}")


