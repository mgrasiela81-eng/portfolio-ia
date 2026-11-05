import os
import re
from groq import Groq

# Inicializa o cliente da Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """
Você é o GreenCode AI, um especialista em Engenharia de Software Sustentável (Green IT) e Otimização de Performance.
Sua missão é analisar códigos fonte fornecidos pelos usuários e identificar ineficiências que geram consumo excessivo de CPU, memória e energia nos servidores.

Ao receber o código e as estatísticas:
1. Avalie o consumo de recursos (CPU, Memória, I/O) e o impacto ambiental/computacional.
2. Identifique gargalos de performance (ex: loops aninhados, buscas ineficientes, falta de estruturas adequadas).
3. Apresente os resultados organizados assim:
   - 📊 DIAGNÓSTICO DE EFICIÊNCIA (Análise de complexidade e impacto de recursos)
   - ⚠️ GARGALOS IDENTIFICADOS (O que está consumindo energia/processamento em excesso)
   - ⚡ CÓDIGO REFATORADO (Versão otimizada, limpa e eficiente do código)
   - 🌿 IMPACTO DE GREEN IT (Explicação do ganho de eficiência)
"""

def analisar_codigo_local(codigo):
    """Calcula métricas estáticas do código em Python puro"""
    linhas = codigo.strip().split('\n')
    total_linhas = len(linhas)
    linhas_codigo = [l for l in linhas if l.strip() and not l.strip().startswith('#')]
    
    # Contagem de estruturas de repetição e decisões (indicadores de complexidade)
    qtd_loops = len(re.findall(r'\b(for|while)\b', codigo))
    qtd_funcoes = len(re.findall(r'\bdef\b', codigo))
    qtd_condicionais = len(re.findall(r'\b(if|elif|else)\b', codigo))
    
    return {
        "total_linhas": total_linhas,
        "linhas_efetivas": len(linhas_codigo),
        "qtd_loops": qtd_loops,
        "qtd_funcoes": qtd_funcoes,
        "qtd_condicionais": qtd_condicionais
    }

def executar_greencode():
    print("==========================================================")
    print("  ⚡ GREENCODE AI - OTIMIZAÇÃO & SUSTENTABILIDADE EM TI    ")
    print("  Análise de Performance e Engenharia de Software Verde  ")
    print("==========================================================")

    while True:
        print("\n------------------- NOVA ANÁLISE -------------------")
        print("(Digite 'sair' a qualquer momento para encerrar)")
        
        print("\nDigite ou cole o trecho de código Python que deseja analisar.")
        print("Dica: Se quiser usar um código de exemplo para testar, digite 'exemplo'.")
        
        codigo_input = input("\nCódigo para análise:\n> ")
        
        if codigo_input.lower() in ['sair', 'exit', 'quit']:
            print("\n👋 GreenCode AI encerrado. Código eficiente economiza o planeta! 🌿")
            break

        # Código de exemplo ineficiente para testes rápidos
        if codigo_input.lower() == 'exemplo':
            codigo_input = """def buscar_duplicados(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j and lista[i] == lista[j]:
                if lista[i] not in duplicados:
                    duplicados.append(lista[i])
    return duplicados"""
            print("\n📌 Usando código de exemplo (Algoritmo de busca com loop duplo O(n²)):")
            print(codigo_input)

        if not codigo_input.strip():
            print("\n❌ NENHUM CÓDIGO INSERIDO. TENTE NOVAMENTE.")
            continue

        # 1. Análise Estatística em Python
        metricas = analisar_codigo_local(codigo_input)

        print("\n📊 --- MÉTRICAS ESTRUTURAIS CALCULADAS (PYTHON) ---")
        print(f"• Total de Linhas: {metricas['total_linhas']} | Linhas de Código Efetivas: {metricas['linhas_efetivas']}")
        print(f"• Estruturas Detectadas: Loops ({metricas['qtd_loops']}) | Funções ({metricas['qtd_funcoes']}) | Condicionais ({metricas['qtd_condicionais']})")

        prompt_usuario = f"""
        ANÁLISE DE SUSTENTABILIDADE E PERFORMANCE DE CÓDIGO:
        
        [CÓDIGO FONTE]
        ```python
        {codigo_input}
        ```
        
        [MÉTRICAS LOCAIS]
        - Total de Linhas: {metricas['total_linhas']}
        - Qtd de Loops: {metricas['qtd_loops']}
        - Qtd de Condicionais: {metricas['qtd_condicionais']}
        
        Avalie o consumo de energia/processamento deste código e forneça uma versão otimizada (Green IT).
        """

        print("\n⏳ GreenCode AI analisando a eficiência energética do código...")

        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt_usuario}
                ],
                model="llama-3.3-70b-versatile",
            )
            
            print("\n🌿 ---------------- RELATÓRIO GREENCODE AI ----------------")
            print(chat_completion.choices[0].message.content)
            print("-----------------------------------------------------------")

        except Exception as e:
            print(f"\n❌ Erro ao conectar com o GreenCode AI: {e}")

if __name__ == "__main__":
    executar_greencode()

