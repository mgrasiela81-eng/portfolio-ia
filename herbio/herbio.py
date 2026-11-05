import os
from groq import Groq

# Inicializa o cliente da Groq
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """
Você é o Herbio AI, uma plataforma avançada de Bioinformática, Etnofarmacologia e Genômica Médica.
Sua missão é cruzar informações genéticas e biológicas de Plantas Medicinais (Solução) com Patógenos/Doenças (Problema).

Ao receber os dados:
1. Analise o potencial de interação entre os compostos/metabólitos da planta e o alvo genético da doença.
2. Explique o mecanismo de ação teórico (como os compostos da planta podem inibir a doença).
3. Apresente os resultados organizados assim:
   - 🎯 ALVO TERAPÊUTICO (Doença)
   - 🌿 PROPRIEDADES BIOATIVAS (Planta)
   - 🔬 MECANISMO DE COMBINAÇÃO (Como a solução atua no problema)
   - ⚠️ AVISO CIENTÍFICO (Necessidade de testes laboratoriais/ensaios clínicos)
"""

def calcular_metricas_dna(sequencia):
    """Calcula estatísticas de bioinformática para qualquer sequência de DNA"""
    seq = sequencia.upper().strip()
    validos = set("ATCG")
    if not set(seq).issubset(validos):
        return None
        
    tamanho = len(seq)
    gc_content = ((seq.count('G') + seq.count('C')) / tamanho) * 100
    return {"tamanho": tamanho, "gc_content": round(gc_content, 2)}

def executar_herbio():
    print("==========================================================")
    print("  🌿 HERBIO AI - PLATAFORMA DE BIOINFORMÁTICA E SAÚDE    ")
    print("  Conectando a Genômica Botânica a Soluções Médicas      ")
    print("==========================================================")

    # Laço de repetição contínuo
    while True:
        print("\n------------------- NOVA CONSULTA -------------------")
        print("(Digite 'sair' a qualquer momento para encerrar)")
        
        # 1. Entrada do Problema (Doença / Patógeno)
        print("\n💡 Sugestões: Candida, Staphylococcus, Inflamação, Dermatofitose, Malaria")
        doenca = input("1. Doença ou Patógeno a ser tratado: ")
        if doenca.lower() in ['sair', 'exit', 'quit']:
            print("\n👋 Herbio AI encerrado. Até a próxima!")
            break

        dna_doenca_in = input("   DNA do Alvo (aperte Enter p/ usar sequência completa): ")
        if dna_doenca_in.lower() in ['sair', 'exit', 'quit']:
            print("\n👋 Herbio AI encerrado. Até a próxima!")
            break
        # Sequência padrão expandida (maior)
        dna_doenca = dna_doenca_in or "ATGCGATCGATCGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCGTA"

        # 2. Entrada da Solução (Planta Medicinal)
        print("\n💡 Sugestões: Barbatimão, Babosa, Ipê-Roxo, Neem, Camomila, Guaco, Alho")
        planta = input("2. Planta Medicinal investigada: ")
        if planta.lower() in ['sair', 'exit', 'quit']:
            print("\n👋 Herbio AI encerrado. Até a próxima!")
            break

        dna_planta_in = input("   DNA da Planta (aperte Enter p/ usar sequência completa): ")
        if dna_planta_in.lower() in ['sair', 'exit', 'quit']:
            print("\n👋 Herbio AI encerrado. Até a próxima!")
            break
        # Sequência padrão expandida (maior)
        dna_planta = dna_planta_in or "ATGCTAGCTAGCTAGCAAGCTAGCTAGCTAGCTAGCGAATTCGGTAGC"

        # Processamento em Python
        metrics_doenca = calcular_metricas_dna(dna_doenca)
        metrics_planta = calcular_metricas_dna(dna_planta)

        if not metrics_doenca or not metrics_planta:
            print("\n❌ Erro: Sequência inválida! Use apenas as bases A, T, C, G.")
            continue

        print("\n📊 --- PROCESSAMENTO DE BIOINFORMÁTICA (PYTHON) ---")
        print(f"• Alvo ({doenca}): {metrics_doenca['tamanho']} bp | Teor GC: {metrics_doenca['gc_content']}%")
        print(f"• Planta ({planta}): {metrics_planta['tamanho']} bp | Teor GC: {metrics_planta['gc_content']}%")

        prompt_usuario = f"""
        ESTUDO DE CRUZAMENTO BIOMÉDICO - HERBIO AI:
        
        [PROBLEMA DE SAÚDE]
        - Doença/Patógeno: {doenca}
        - Métrica do DNA do Alvo: {metrics_doenca['tamanho']} bp, Teor GC: {metrics_doenca['gc_content']}%
        
        [SOLUÇÃO BOTÂNICA]
        - Planta Medicinal: {planta}
        - Métrica do DNA Vegetal: {metrics_planta['tamanho']} bp, Teor GC: {metrics_planta['gc_content']}%
        
        Avalie se e como o perfil dessa planta serve como solução medicinal para essa doença.
        """

        print("\n⏳ Herbio AI cruzando dados genéticos em tempo real...")

        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt_usuario}
                ],
                model="llama-3.3-70b-versatile",
            )
            
            print("\n🔬 ---------------- RELATÓRIO HERBIO AI ----------------")
            print(chat_completion.choices[0].message.content)
            print("-------------------------------------------------------")

        except Exception as e:
            print(f"\n❌ Erro ao conectar com o Herbio AI: {e}")

if __name__ == "__main__":
    executar_herbio()

