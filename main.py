
import csv

class Imovel:
    def __init__(self, cliente):
        self.cliente = cliente
        self.valor_contrato = 2000.00 

class Apartamento(Imovel):
    def calcular(self, quartos, tem_crianca, tem_garagem):
        v = 700.00 
        if quartos == 2: v += 200.00 
        if tem_garagem: v += 300.00 
        if not tem_crianca: v *= 0.95 
        return v

class Casa(Imovel):
    def calcular(self, quartos, tem_garagem):
        v = 900.00 
        if quartos == 2: v += 250.00 
        if tem_garagem: v += 300.00 
        return v

class Estudio(Imovel):
    def calcular(self, vagas):
        v = 1200.00 
        if vagas >= 2:
            v += 250.00 + (max(0, vagas - 2) * 60.00) 
        return v

def exportar_csv(nome, mensalidade, total_contrato):
    with open(f'orcamento_{nome}.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['Mes', 'Aluguel Mensal', 'Parcela Contrato', 'Total Mensal'])
        for i in range(1, 13):
            p_c = (total_contrato / 5) if i <= 5 else 0
            w.writerow([f'Mes {i}', f'R$ {mensalidade:.2f}', f'R$ {p_c:.2f}', f'R$ {mensalidade + p_c:.2f}'])
    print(f"\nArquivo 'orcamento_{nome}.csv' gerado com sucesso!")

# --- Execução Principal ---
print("--- Sistema de Orçamentos R.M ---")
nome = input("Nome do Cliente: ")
tipo = input("Tipo (Apto/Casa/Estudio): ").strip().lower()

if tipo == "apto":
    imovel = Apartamento(nome)
    q = int(input("Quartos (1 ou 2): "))
    c = input("Possui crianças? (s/n): ").lower() == 's'
    g = input("Vaga de garagem? (s/n): ").lower() == 's'
    valor = imovel.calcular(q, c, g)
elif tipo == "casa":
    imovel = Casa(nome)
    q = int(input("Quartos (1 ou 2): "))
    g = input("Vaga de garagem? (s/n): ").lower() == 's'
    valor = imovel.calcular(q, g)
elif tipo == "estudio":
    imovel = Estudio(nome)
    v = int(input("Quantidade de vagas de estacionamento: "))
    valor = imovel.calcular(v)
else:
    print("Tipo de imóvel inválido!")
    exit()

print(f"\nOrçamento Mensal: R$ {valor:.2f}")
exportar_csv(nome, valor, imovel.valor_contrato)