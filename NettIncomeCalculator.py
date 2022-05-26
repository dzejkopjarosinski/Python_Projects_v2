class Pracownik:
  laczny_koszt=0
  def __init__(self, imie, nazwisko):
    self._imie = imie
    self._wynagrodzenie = nazwisko

  def wyniki(self):
      sk_emeryt=round(self._wynagrodzenie*0.0976,2)
      sk_rent=round(self._wynagrodzenie*0.015,2)
      sk_chor=round(self._wynagrodzenie*0.0245,2)
      sk=round(sk_emeryt+sk_rent+sk_chor,2)
      podstawa_a=round(self._wynagrodzenie-sk,2)
      ubez_zdr_a=round(podstawa_a*0.09,2)
      ubez_zdr_b=round(podstawa_a*0.0775,2)
      podst_b=round(self._wynagrodzenie-111.25-sk,0)
      zal_a=round(round(podst_b*0.18,2)-46.33,2)
      zal_b=round(zal_a-ubez_zdr_b,0)
      
      wyplata=round(self._wynagrodzenie-sk-ubez_zdr_a-zal_b,2)
      skladki=round(self._wynagrodzenie*0.0976,2)+round(self._wynagrodzenie*0.065,2)+round(self._wynagrodzenie*0.0193,2)+round(self._wynagrodzenie*0.0245,2)+round(self._wynagrodzenie*0.001,2)
      koszt_pracodawcy=round(self._wynagrodzenie+skladki,2)
      Pracownik.laczny_koszt+=koszt_pracodawcy
      print(self._imie,"{:.2f}".format(wyplata),"{:.2f}".format(skladki),"{:.2f}".format(koszt_pracodawcy))

liczba_pracownikow=int(input())
pracownicy_lista=[]
for pracownicy in range(liczba_pracownikow):
  imie_wynagrodzenie=input()
  pracownicy_lista.append(imie_wynagrodzenie)

for pracownik2 in pracownicy_lista:   
  pr=pracownik2.split(' ')
  imie_pr=pr[0]
  wynagrodzenie_pr=float(pr[1])
  pr2=Pracownik(imie_pr,wynagrodzenie_pr)
  pr2.wyniki()

print(Pracownik.laczny_koszt)