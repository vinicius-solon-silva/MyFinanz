import matplotlib.pyplot as plt

def generate(dict):
    get_categorias = dict.keys()
    get_limites = dict.values()

    plt.bar(get_categorias,  get_limites)
    plt.title('Gastos mensais')
    plt.xlabel('Categoria')
    plt.ylabel('Gastos em Reais')
    plt.savefig("Tcc\charts\chart.png")
