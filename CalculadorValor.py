# Calculador de Preços
# Por Taiara Regis

from time import sleep

resposta = ''

print('{:=^40}'.format(' O TEXUGO ELETRO '))

preco = float(input('\033[32mQual o valor do produto? R$ \033[m'))
print('''\033[31m1 \033[33mDinheiro/Pix com 10% de desconto\033[m
\033[31m2 \033[33mÀ vista no cartão com 5% de desconto\033[m
\033[31m3 \033[33mParcelado em 2x sem juros\033[m
\033[31m4 \033[33mParcelado acima de 3x com juros de 20%\033[m''')
pagamento = int(input('\033[32mQual será a forma de pagamento? \033[m'))
print('\033[37mCalculando...\033[m')
sleep(2)

if pagamento == 1:
    print(f'\033[32mO valor final da sua compra será \033[34mR$ {preco * 0.90:.2f}\033[m')
elif pagamento == 2:
    print(f'\033[32mO valor final da sua compra será \033[34mR$ {preco * 0.95:.2f}\033[m')
elif pagamento == 3:
    print(f'\033[32mO valor final da sua compra será \033[34mR$ {preco:.2f}\033[m')
elif pagamento == 4:
    int(input('\033[33mEm quantas parcelas? \033[m'))
    print(f'\033[32mO valor final da sua compra será \033[34mR$ {preco * 1.20:.2f}\033[m')
else:
    sleep(0.5)
    print('\033[37mOpção inválida, tente novamente.\033[m')