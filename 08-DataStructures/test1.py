class Tekst():

    @staticmethod
    def gwiazdki(tekst):
        return tekst[:3] + '*'*len(tekst[3:])

    @staticmethod
    def wyrazy(tekst):
        return len(tekst.split())


print(Tekst.wyrazy('Ala2 22    m\
                   a k ota '))
