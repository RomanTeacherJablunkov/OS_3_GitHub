class UmiProgramovat:
    def popis(self):
        print("Umí programovat")
class UmiNavrhovat:
    def popis(self):
        print("Umí navrhovat")
class ITSpecialista(UmiProgramovat, UmiNavrhovat):
        pass
specialista = ITSpecialista()
specialista.popis()