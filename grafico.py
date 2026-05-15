import pandas as pd
import matplotlib.pyplot as plt #cria graficos

# Lendo o arquivo Excel
dados = pd.read_excel("dados.xlsx")

# Separando as colunas
periodo = dados["Periodo"]
valor = dados["Valor"]

# Criando o gráfico
plt.figure(figsize=(10, 5)) #criar janela, tamanho do grafico
#plt.plot(periodo, valor, marker="o")#o que eu quero colocar , ele faz a intececção e coloca uma bolinha
#plt.bar(periodo,valor)# grafico de barras
plt.fill_between(periodo,valor) #outro grafico

# Deixando as legendas do eixo X na vertical
plt.xticks(rotation=90) #rotacionar 90 graus

# Configurações do gráfico
plt.title("Evolução dos Valores ao Longo do Tempo") #titulo do grafico
plt.xlabel("Período") # texto no eixo x 
plt.ylabel("Valor") # texto no eixo y
plt.grid(axis="y") #linha de grade

# Ajusta automaticamente os espaços
plt.tight_layout()

# Exibindo o gráfico
plt.show()