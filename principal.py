from random import choice, shuffle
from time import sleep
from equipe import Equipe

def menu(tipo_menu, rodada=0):
    if tipo_menu == 1:
        print('[1] COMEÇAR A SIMULAÇÃO',
              '\n[2] MODIFICAR STATS DOS TIMES',
              '\n[3] SAIR')
    elif tipo_menu == 2:
        print(f'-=-' * 15)
        print(f'E chegamos ao fim da {rodada - 1}° rodada do BRASILEIRÃO 2022')
        sleep(1)
        print('[1] CONTINUAR SIMULANDO')
        print('[2] VER TABELA')
        print('[3] PARAR DE SIMULAR')

    opcao = 0
    while True:
        opcao = int(input(''))
        if opcao != 1 and opcao != 2 and opcao != 3:
            print('Opção inválida. Tente novamente.')
            sleep(1)
        else:
            break
    return opcao

def confrontoSimulado(time1, time2):
    valores = []
    p1 = Equipe(time1.getNome(), time1.getAtaque(), time1.getDefesa(), time1.getCasa(), time1.getFora(), time1.getSigla(), time1.getPontos())
    p2 = Equipe(time2.getNome(), time2.getAtaque(), time2.getDefesa(), time2.getCasa(), time2.getFora(), time2.getSigla(), time2.getPontos())
    div = 0
    if p1.getCasa() >= 9.0:
        div = 1.3
    elif 8.5 <= p1.getCasa() <= 8.9:
        div = 1.5
    elif 8.0 <= p1.getCasa() <= 8.4:
        div = 1.8
    elif 7.5 <= p1.getCasa() <= 7.9:
        div = 2.3
    elif 7.0 <= p1.getCasa() <= 7.4:
        div = 2.6
    else:
        div = 3.2
    p1.setAtaque(p1.getAtaque() * ((100 + (p1.getCasa() / div)) / 100))
    p1.setDefesa(p1.getDefesa() * ((100 + (p1.getCasa() / div)) / 100))
    if p2.getFora() >= 9.0:
        div = 1.7
    elif 8.5 <= p2.getFora() <= 8.9:
        div = 2.1
    elif 8.0 <= p2.getFora() <= 8.4:
        div = 2.5
    elif 7.5 <= p2.getFora() <= 7.9:
        div = 2.8
    elif 7.0 <= p2.getFora() <= 7.4:
        div = 3.4
    else:
        div = 4.0
    p2.setAtaque(p2.getAtaque() * ((100 + (p2.getFora() / div)) / 100))
    p2.setDefesa(p2.getDefesa() * ((100 + (p2.getFora() / div)) / 100))
    totemp = 0
    if ((p1.getAtaque() * (85 / 100) > p2.getAtaque() or (p1.getAtaque() * (85 / 100) > p2.getDefesa()))) or ((p2.getAtaque() * (85 / 100) > p1.getAtaque() or (p2.getAtaque() * (85 / 100) > p1.getDefesa()))):
        totemp = (p1.getAtaque() + p1.getDefesa() + p2.getAtaque() + p2.getDefesa())
    elif ((p1.getAtaque() * (90 / 100) > p2.getAtaque() or (p1.getAtaque() * (90 / 100) > p2.getDefesa()))) or ((p2.getAtaque() * (90 / 100) > p1.getAtaque() or (p2.getAtaque() * (90 / 100) > p1.getDefesa()))):
        totemp = (p1.getAtaque() + p1.getDefesa() + p2.getAtaque() + p2.getDefesa())
    else:
        totemp = (p1.getAtaque() + p1.getDefesa() + p2.getAtaque() + p2.getDefesa()) * 2
    totalp1 = (p1.getAtaque() ** 2) + (p1.getDefesa() ** 2)

    for c in range(round(totalp1)):
        valores += [1]
    totalp2 = (p2.getAtaque() ** 2) + (p2.getDefesa() ** 2)

    for c in range(round(totalp2)):
        valores += [2]
    for c in range(round(totemp)):
        valores += [3]

    vencedor = choice(valores)
    if vencedor == 1:
        time1.setPontos(3)
    elif vencedor == 2:
        time2.setPontos(3)
    elif vencedor == 3:
        time1.setPontos(1)
        time2.setPontos(1)



# Time / [Ataque / Defesa / Casa / Fora, Sigla]

'''times = ['AMÉRICA-MG', [65, 71, 75, 63], 'ATHLETICO-PR', [72, 79, 79, 75], 'ATLÉTICO-GO', [69, 66, 65, 65],
         'ATLÉTICO-MG', [84, 82, 86, 75], 'AVAÍ', [68, 62, 72, 63], 'BOTAFOGO', [71, 70, 73, 73], 'BRAGANTINO',
         [76, 68, 69, 70], 'CEARÁ', [69, 68, 64, 71], 'CORINTHIANS', [77, 79, 83, 77], 'CORITIBA', [70, 64, 77, 62],
         'CUIABÁ', [61, 65, 64, 68], 'FLAMENGO', [84, 77, 80, 77], 'FLUMINENSE', [78, 77, 77, 77], 'FORTALEZA',
         [72, 72, 75, 67], 'GOIÁS', [65, 63, 63, 66],'JUVENTUDE', [61, 63, 67, 61], 'INTERNACIONAL', (73, 75, 74, 76),
         'PALMEIRAS', [84, 87, 85, 80], 'SANTOS', [74, 71, 74, 72], 'SÃO PAULO', [77, 75, 78, 72]]'''

times = ['AMÉRICA-MG', [6.5, 7.0, 7.5, 6.5, 'AMG'], 'ATHLETICO-PR', [7.5, 8.0, 8.5, 7.5, 'CAP'], 'ATLÉTICO-GO', [7.0, 7.0, 6.5, 6.5, 'ACG'],
         'ATLÉTICO-MG', [9.0, 8.0, 8.5, 8.0, 'CAM'], 'AVAÍ', [6.5, 6.5, 7.0, 6.0, 'AVA'], 'BOTAFOGO', [7.0, 7.0, 7.5, 7.5, 'BOT'], 'BRAGANTINO',
         [8.5, 7.0, 7.0, 6.5, 'BGT'], 'CEARÁ', [7.0, 7.0, 6.5, 7.0, 'CEA'], 'CORINTHIANS', [8.0, 8.0, 8.5, 7.5, 'COR'], 'CORITIBA', [7.0, 6.5, 8.0, 6.0, 'CFC'],
         'CUIABÁ', [6.0, 6.5, 6.5, 7.0, 'CUI'], 'FLAMENGO', [9.0, 8.0, 8.5, 8.0, 'FLA'], 'FLUMINENSE', [8.0, 8.0, 8.0, 7.5, 'FLU'], 'FORTALEZA',
         [7.5, 7.0, 7.5, 6.5, 'FOR'], 'GOIÁS', [6.5, 6.0, 6.5, 6.5, 'GOI'],'JUVENTUDE', [6.0, 6.0, 6.5, 6.0, 'JUV'], 'INTERNACIONAL', (7.5, 7.5, 7.5, 7.5, 'INT'),
         'PALMEIRAS', [9.0, 9.0, 9.0, 8.0, 'PAL'], 'SANTOS', [7.5, 7.0, 7.5, 7.0, 'SAN'], 'SÃO PAULO', [8.0, 7.5, 8.0, 6.5, 'SAO']]
list = [] # Guarda os objetos criados em um único array
partidas = []

print(f'\033[107;30;4;1m{" BEM-VINDO AO SIMULADOR DO BRASILEIRÃO! ":=^50} \033[m')
sleep(1)
while True:
    opcao = menu(1)
    if opcao == 1:
        print('COMEÇANDO...')
        print('-=-' * 15)
        aux = 0
        aux2 = 1
        print(f'\033[1;4m{"NOME DA EQUIPE":<15}', '|  CLASSIFICAÇÃO GERAL\033[m')
        for c in range(0, 20):
            list.append(Equipe(times[aux], times[aux2][0], times[aux2][1], times[aux2][2], times[aux2][3], times[aux2][4], 0))
            print(f'{list[c].getNome():<15}', f'|  {list[c].estrelas():}')
            aux += 2
            aux2 += 2
        rodada_atual = 1
        while True:
            opcao = int(input('Deseja simular até que rodada? (MAX: 38): '))
            if opcao <= rodada_atual or opcao > 38:
                print('\033[41;97;1m[ERRO]\033[m \033[4mRodada inválida. Tente novamente\033[m')
                continue
            else:
                print('\nSIMULANDO...')
                for rodada in range(rodada_atual, opcao + 1):
                    rodada_atual += 1
                    aux_teams = ['AMG', 'CAP', 'ACG', 'CAM', 'AVA', 'BOT', 'BGT', 'CEA', 'COR', 'CFC', 'CUI', 'FLA', 'FLU', 'FOR', 'GOI', 'JUV', 'INT', 'PAL', 'SAN', 'SAO']
                    while len(aux_teams) > 0:
                        time1 = choice(aux_teams)
                        time2 = time1
                        while time2 == time1:
                            time2 = choice(aux_teams)
                        if f'{time1}x{time2}' not in partidas and time1 != time2:
                            aux_teams.remove(time1)
                            aux_teams.remove(time2)
                            partidas += [f'{time1}x{time2}']
                            achou1 = achou2 = False
                            for objEquipe in list:
                                if objEquipe.getSigla() == time1:
                                    time1 = objEquipe
                                    achou1 = True
                                if objEquipe.getSigla() == time2:
                                    time2 = objEquipe
                                    achou2 = True

                                if achou1 == True and achou2 == True:
                                    confrontoSimulado(time1, time2)
                                    break
            opcao = menu(2, rodada_atual)
            if opcao == 1:
                continue
            elif opcao == 2:
                print(f'\033[1;4m{"NOME DA EQUIPE":<15}', '|  CLASSIFICAÇÃO GERAL\033[m')
                for c in list:
                    print(f'{c.getNome():<15}', f'|  {c.getPontos():}')

            else:
                break

    else:
        break