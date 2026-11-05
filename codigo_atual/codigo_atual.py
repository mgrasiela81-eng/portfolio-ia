# Programa para calcular a média de um aluno

def calcular_media(notas):
    """
    Calcula a média de uma lista de notas.
    
    Args:
        notas (list): Lista de notas.
    
    Returns:
        float: Média das notas.
    """
    return sum(notas) / len(notas)


def main():
    # Pedir o nome do aluno
    nome_aluno = input("Digite o nome do aluno: ")
    
    # Pedir as notas do aluno
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input(f"Digite a nota {i+1}: "))
                if nota < 0 or nota > 10:
                    print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
                else:
                    notas.append(nota)
                    break
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")
    
    # Calcular a média
    media = calcular_media(notas)
    
    # Imprimir o resultado
    print(f"O aluno {nome_aluno} tem uma média de {media:.2f}")


if __name__ == "__main__":
    main()