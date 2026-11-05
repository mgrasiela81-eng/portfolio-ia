import json
import random

class BioGenLab:
    def __init__(self):
        self.humanos = {}
        self.plantas = {}
        self.observacao = set()
        for i in range(1, 6):
            self.humanos[f"HUMAN-{i:03d}"] = "".join(random.choices(['A','T','C','G'], k=40))
            self.plantas[f"PLANT-{i:03d}"] = "".join(random.choices(['A','T','C','G'], k=40))

    def adicionar(self, tipo, sid, seq):
        if tipo == "humano":
            self.humanos[sid] = seq.upper()
            print(f"[SUCESSO] Humano {sid} registado.")
        else:
            self.plantas[sid] = seq.upper()
            print(f"[SUCESSO] Planta {sid} registada.")

    def alternar_obs(self, pid):
        if pid in self.plantas:
            if pid in self.observacao:
                self.observacao.remove(pid)
                print(f"[*] Planta {pid} removida da observacao.")
            else:
                self.observacao.add(pid)
                print(f"[👁️] Planta {pid} em OBSERVACAO CRITICA!")
        else:
            print("[ERRO] Planta nao encontrada.")

    def analisar(self, hid):
        if hid not in self.humanos:
            print("[ERRO] Humano nao encontrado.")
            return
        seq_h = self.humanos[hid]
        res = []
        for pid, seq_p in self.plantas.items():
            m = sum(1 for a, b in zip(seq_h, seq_p) if a == b)
            sim = (m / len(seq_h)) * 100
            res.append({
                "plant_id": pid,
                "painel": "CRITICO - OBSERVACAO" if pid in self.observacao else "NORMAL",
                "homologia": f"{round(sim, 2)}%"
            })
        res.sort(key=lambda x: float(x["homologia"].replace("%","")), reverse=True)
        rel = {
            "alvo_humano": hid,
            "total_humanos": len(self.humanos),
            "total_plantas": len(self.plantas),
            "plantas_observadas": list(self.observacao),
            "top_homologias": res[:3]
        }
        print("\n--- RELATORIO DE HOMOLOGIA ---")
        print(json.dumps(rel, indent=4))

def menu():
    lab = BioGenLab()
    while True:
        print("\n=== BIO-GEN LAB ===")
        print("1. Analisar Homologia")
        print("2. Adicionar Humano")
        print("3. Adicionar Planta")
        print("4. Observar Planta")
        print("0. Sair")
        op = input("Opcao: ").strip()
        if op == "1":
            lab.analisar(input("ID Humano (ex: HUMAN-001): ").strip())
        elif op == "2":
            lab.adicionar("humano", input("ID Humano: ").strip(), input("DNA (A,T,C,G): ").strip())
        elif op == "3":
            lab.adicionar("planta", input("ID Planta: ").strip(), input("DNA (A,T,C,G): ").strip())
        elif op == "4":
            lab.alternar_obs(input("ID Planta: ").strip())
        elif op == "0":
            break
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    menu()
