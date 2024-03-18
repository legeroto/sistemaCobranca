# BOAS VINDAS
print("Bem-vindo ao Copy & Print do Leandro Geroto Soares!")
print("")
print("Catálogo de serviços:")
print("DIG - Digitalização")
print("ICO - Impressão Colorida")
print("IBO - Impressão Preto e Branco")
print("FOT - Fotocópia")
print("")

# CÓDIGO PARA DEFINIR O VALOR DO SERVIÇO ESCOLHIDO
def escolhaServico():
    while True:
        servico = input("Digite o serviço desejado (dig/ico/ibo/fot): ").lower()
        if servico in ['dig', 'ico', 'ibo', 'fot']:
            if servico == 'dig':
                return 'Digitalização', 1.10
            elif servico == 'ico':
                return 'Impressão Colorida', 1.00
            elif servico == 'ibo':
                return 'Impressão Preto e Branco', 0.40
            elif servico == 'fot':
                return 'Fotocópia', 0.20
        else:
            print("Opção de serviço inválida. Por favor, escolha entre 'dig', 'ico', 'ibo' ou 'fot'.")
            print("")

# CÓDIGO PARA DEFINIR O DESCONTO SE HOUVER
def numPagina():
    while True:
        try:
            numPag = int(input("Digite o número de páginas: "))
            if numPag < 20:
                return numPag
            elif 20 <= numPag < 200:
                return numPag, numPag * 0.85
            elif 200 <= numPag < 2000:
                return numPag, numPag * 0.80
            elif 2000 <= numPag < 20000:
                return numPag, numPag * 0.75
            else:
                print("Não aceitamos pedidos com mais de 20.000 páginas.")
                print("Por favor, escolha um número de páginas válido.")
        except ValueError:
            print("Por favor, digite um valor numérico para o número de páginas.")

# CÓDIGO PARA DEFINIR SERVIÇO EXTRA SE SOLICITADO
def servicoExtra():
    while True:
        try:
            print("Serviços adicionais:")
            print("0 - Nenhum serviço adicional (R$0.00)")
            print("1 - Encadernação simples (R$15.00)")
            print("2 - Encadernação de capa dura (R$40.00)")
            servicoAdicional = int(input(
                "Deseja algum serviço adicional? (0 para nenhum, 1 para encadernação simples, 2 para encadernação de capa dura): "))
            if servicoAdicional in [0, 1, 2]:
                if servicoAdicional == 1:
                    return 'Encadernação simples', 15
                elif servicoAdicional == 2:
                    return 'Encadernação de capa dura', 40
                else:
                    return 'Nenhum serviço adicional', 0
            else:
                print("Opção de serviço adicional inválida. Por favor, escolha entre 0, 1 ou 2.")
        except ValueError:
            print("Por favor, digite um valor numérico para o serviço adicional.")

# CÓDIGO DE VERIFICAÇÃO DO PEDIDO
def main():
    try:
        servicoNome, servicoValor = escolhaServico()
        numPaginas, numPaginasComDesconto = numPagina()
        servicoAdicionalNome, servicoAdicionalValor = servicoExtra()

        total = servicoValor * numPaginasComDesconto + servicoAdicionalValor

# CÓDIGO PARA EXIBIR RESUMO DO PEDIDO:
        print("\nResumo do Pedido:")
        print("Serviço contratado:", servicoNome)
        print("Número de páginas:", numPaginas)
        print("Serviço adicional:", servicoAdicionalNome)
        print("Total a pagar: R$", total)

    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
    except Exception as e:
        print("Ocorreu um erro:", e)

# CÓDIGO PARA CHAMAR A FUNÇÃO:
if __name__ == "__main__":
    main()
