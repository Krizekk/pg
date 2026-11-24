import json
class InvalidData(Exception):
    pass

class Osoba:
    def __init__(self, jmeno, telefon, email):
        self.__jmeno = jmeno
        self.__telefon = telefon
        self.__email = email


    @property
    def jmeno(self):
        return self.__jmeno
    @jmeno.setter
    def jmeno(self,hodnota):
        if hodnota.replace(" ", "").isalpha():
            self.__jmeno = hodnota
        else:
            raise InvalidData("Jmeno musi obsahovat pouze pismena")

    @property
    def telefon(self):
        return self.__telefon
    @telefon.setter
    def telefon(self, hodnota):
        if hodnota.isnumeric():
            self.__telefon = hodnota
        else:
            raise InvalidData("telfon musi obsahovat poue cisla")
        
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, hodnota):
        if "@" not in hodnota:
            raise InvalidData("Email musi obsahovat @")
        if "." not in hodnota:
            raise InvalidData("Email musi obsahovat tecku")
        if hodnota.replace("@", "").replace(".", "").isalnum():
            self.__email = hodnota
        else:
            raise InvalidData("Email musi obsahovat pouze pismena a cisla")

    def __str__(self):
        return f"Osoba: {self.jmeno}, {self.telefon}, {self.email}"
    def __repr__(self):
        return f"Osoba: {self.jmeno}, {self.telefon}, {self.email}"

    @classmethod
    def load_json_data(cls, data):
        if "jmeno" not in data or "telefon" not in data or "email" not in data:
            return None
        return cls(data["jmeno"], data["telefon"], data["email"])



if __name__ == "__main__":
    #o = Osoba("Jan Novak", "+420606618524", "jan.novak@email.cz" )
    #o.jmeno = "Jan Novak"
    #o.telefon = "601103485"
    #o.email = "jan.novak@email.cz"

    osoby = []
    with open("osoby.json") as f:
        data = json.loads(f.read())
        print(data)
        for record in data:
            osoby.append(Osoba.load_json_data(record))
    print(osoby)


