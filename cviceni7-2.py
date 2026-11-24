class  ChybnaCastka(Exception):
    def __str__(self):
        return "Chybna castka"

class BankovniUcet:
    def __init__(self,jmeno, urok):
        self.jmeno = jmeno
        self.jmeno = urok
        self._zustatek = 0

    def __str__(self):
        return f"Na ucte {self.jmeno} je {self._zustatek} kc"

    def vloz(self, castka):
        if castka <= 0:
            raise ChybnaCastka(xxx)
        self._zustatek += castka

    def vyber(self, castka):
        if castka <= 0:
            raise ChybnaCastka(xxx)
        if castka > self._zustatek:
            raise ChybnaCastka(xxx)
        self._zustatek -= castka

    def pricti_uroky(self):
        pass