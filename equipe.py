import emoji

class Equipe:
    def __init__(self, nome, ataque, defesa, casa, fora, sigla, pontos):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.casa = casa
        self.fora = fora
        self.sigla = sigla
        self.pontos = pontos

    def estrelas(self):
        total = self.ataque + self.defesa + self.casa + self.fora
        aux = 0
        if total >= 33:
            aux = 5
        elif 30 <= total < 33:
             aux = 4
        elif 27 <= total < 30:
            aux = 3
        else:
            aux = 2
        return emoji.emojize('\u2B50', use_aliases=True) * aux


    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getAtaque(self):
        return self.ataque

    def setAtaque(self, ataque):
        self.ataque = ataque

    def getDefesa(self):
        return self.defesa

    def setDefesa(self, defesa):
        self.defesa = defesa

    def getCasa(self):
        return self.casa

    def setCasa(self, casa):
        self.casa = casa

    def getFora(self):
        return self.fora

    def setFora(self, fora):
        self.fora = fora

    def getSigla(self):
        return self.sigla

    def setSigla(self, sigla):
        self.sigla = sigla

    def getPontos(self):
        return self.pontos

    def setPontos(self, pontos):
        self.pontos += pontos