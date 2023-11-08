print('Ola mundo!!!')

nome = input('Qual é o seu nome?')
print(nome)

def calcular_tempo_para_meta(meta, economia_mensal):
    if economia_mensal <= 0:
        return 'A economia mensal deve ser maior que zero.'

    meses_necessarios = meta / economia_mensal
    return meses_necessarios

# Solicitar entrada do usuário com tratamento de erros
while True:
    try:
        meta = float(input('Informe o valor da meta financeira: R$'))
        if meta < 0:
            print('A meta financeira não pode ser negativa. Tente novamente.')
            continue
        economia_mensal = float(input('Informe a economia mensal: R$'))
        if economia_mensal <= 0:
            print('A economia mensal deve ser maior que zero. Tente novamente.')
            continue
        break
    except ValueError:
        print('Entrada inválida. Insira um valor numérico.')

tempo_necessario = calcular_tempo_para_meta(meta, economia_mensal)

if tempo_necessario == 'A economia mensal deve ser maior que zero.':
    print(tempo_necessario)
elif tempo_necessario > 1:
    print(f'Você levará aproximadamente {int(tempo_necessario)} meses para atingir a meta financeira de R${meta:.2f}.')
elif tempo_necessario == 1:
    print(f'{nome} levará 1 mês para atingir a meta financeira de R${meta:.2f}.')
else:
    print('Você já atingiu a sua meta financeira e pode investir em seus sonhos.')
