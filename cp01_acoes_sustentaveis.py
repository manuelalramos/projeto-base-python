# Lena Haidar Halawi - RM 572258
# Lyvia Correa de Amorim - RM 569851
# Manuela de Lima Ramos - RM 572956
# Tailyni Victoria Renovato Satirio - RM 570517
# Yasmin Souza Silva Martins - RM 571202

acao = input('Qual ação sustentável você deseja registrar?\nInsira aqui: ')

impacto = int(input('Como você avalia o impacto desta ação? Digite\n1 --> Para impacto baixo. Foi uma ação simples e individual.\n2 --> Para impacto médio. Foi uma ação com efeito moderado.\n3 --> Para impacto alto. Foi uma ação com maior relevância ou alcance.\nInsira aqui: '))

if impacto < 1 or impacto > 3:
    print('Formato errado! Tente novamente.')
    exit()

frequencia = int(input('Quantas vezes essa mesma ação foi realizada neste mês?\nInsira aqui: '))

validacao = input('Essa ação já foi validada pela plataforma por foto, comprovante ou conferência? Responda com Sim ou Não\nInsira aqui: ').upper()

if validacao != 'SIM' and validacao != 'NAO' and validacao != 'NÃO':
    print('Entrada inválida! Digite apenas SIM ou NÃO.')
    exit()

if validacao == 'NAO' or validacao == 'NÃO':
    print('Sem Classificação! ')
    print('Por favor, valide a sua ação na plataforma para dar continuidade')
    exit()
else:
    coletiva = input('Essa ação foi coletiva ou gerou benefício para outras pessoas? Responda com Sim ou Não.\nInsira aqui: ').upper()
    
    if coletiva != 'SIM' and coletiva != 'NAO' and coletiva != 'NÃO':
        print('Entrada inválida! Digite apenas SIM ou NÃO.')
        exit()

    if impacto == 3 and coletiva == 'SIM':
        print('Destaque Sustentável! Liberando bônus especial...')
        print('Bônus especial liberado! Continue assim!')
        exit()
    elif impacto == 3 or frequencia >=5:
        print('Pontuação Bônus! Registrando ação com bônus...')
        print('Ação registrada com bônus! Obrigado pela sua ação!')
        exit()
    else:
        print('Registrando participação...')
        print('Participação registrada! Obrigado!')

    



