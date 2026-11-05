import os
import random
from groq import Groq

# Inicializa o cliente da Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """
Você é o PyroGuard AI, uma inteligência artificial especialista em Química de Combate a Incêndios, Sensoriamento IoT e Proteção Florestal.

Sua missão é analisar os dados recebidos dos sensores de solo da floresta e:
1. 🔍 DIAGNÓSTICO DO SENSOR: Classificar se a leitura indica atividade normal (fauna/flora), interferência humana suspeita (desmatamento) ou um foco de incêndio.
2. 🧪 REAÇÃO QUÍMICA & RETARDANTE: Se for incêndio, explique como neutralizar a reação quântica/química do fogo cortando o suprimento de oxigênio (ex: dispersão de bicarbonato de potássio em névoa, dióxido de carbono ou pó químico seco por dispersão aérea).
3. 🛡️ PLANO DE CONTENÇÃO: Dê instruções diretas para acionar os dispersores automáticos no local.
"""

def simular_sensores_solo():
    """Simula dados capturados pelos sensores implementados no solo da floresta"""
    temperatura = random.randint(25, 95)  # em °C
    ruido_db = random.randint(30, 110)    # em decibéis
    nivel_co2 = random.randint(350, 1200) # em ppm (partes por milhão)
    vibracao = random.choice(["Baixa", "Moderada", "Alta (Motosserra/Veículo)", "Crítica (Queimada)"])

    return {
        "temperatura": temperatura,
        "ruido": ruido_db,
        "co2": nivel_co2,
        "vibracao": vibracao
    }

def executar_pyro_guard():
    print("==========================================================")
    print("  🌿 PYROGUARD AI - MONITORAMENTO FLORESTAL & QUÍMICA    ")
    print("  Proteção de biomas com IoT e Supressão de Oxigênio     ")
    print("==========================================================")
    print("(Digite 'sair' a qualquer momento para encerrar)")

    while True:
        print("\n-----------------------------------------------------------")
        print("1. Simular leitura automática dos sensores de solo")
        print("2. Descrever um cenário manualmente")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao in ['0', 'sair', 'exit', 'quit']:
            print("\n👋 Monitoramento PyroGuard encerrado. Proteja nossas florestas! 🌿")
            break

        if opcao == "1":
            dados = simular_sensores_solo()
            prompt_usuario = f"""
            DADOS DOS SENSORES DE SOLO:
            - Temperatura Atual: {dados['temperatura']}°C
            - Nível de Ruído: {dados['ruido']} dB
            - Concentração de CO2: {dados['co2']} ppm
            - Nível de Nível de Vibração do Solo: {dados['vibracao']}

            Analise esses dados, classifique a situação e indique se é necessário disparar o agente químico abafador de oxigênio.
            """
            print(f"\n📡 Lendo sensores... Temp: {dados['temperatura']}°C | CO2: {dados['co2']}ppm | Ruído: {dados['ruido']}dB")

        elif opcao == "2":
            descricao = input("\n📝 Descreva o cenário ou a reação química que deseja analisar:\n> ")
            if not descricao.strip():
                continue
            prompt_usuario = f"CENÁRIO INFORMADO: {descricao}"

        else:
            print("\n❌ Opção inválida!")
            continue

        print("\n⏳ PyroGuard AI analisando dados ambientais e reações químicas...")

        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt_usuario}
                ],
                model="llama-3.3-70b-versatile",
            )

            print("\n🔥 ---------------- RELATÓRIO AMBIENTAL ----------------")
            print(chat_completion.choices[0].message.content)
            print("---------------------------------------------------------")

        except Exception as e:
            print(f"\n❌ Erro ao conectar com o PyroGuard AI: {e}")

if __name__ == "__main__":
    executar_pyro_guard()

