nome_barman = 'Frigobar'

#PRESENTAZIONE
print("Ciao Viandante! Benvenuto al DarkBar!" + '\nMi chiamo ' + str(nome_barman) + " piacere di conoscerti!")
pub_aperto = True
delivery = True
if pub_aperto and delivery:
    print("\nSiamo pronti per il servizio e per le consegne!")
if pub_aperto and not delivery:
    print("\nSiamo pronti per il servizio, ma niente consegne.")
    
print("Qui il nostro must si chiama ESTUS," + " e oggi ne abbiamo preparati per il pubblico:\n")
drink_speciale = "ESTUS"
quantità_drink = "30 pezzi"
print(quantità_drink)
print('\nlo puoi acquistare alla modica cifra di:')
prezzo_drink = 3.5
sconto = 2
prezzo_scontato = prezzo_drink - sconto
print(prezzo_drink)

#CONOSCIMENTO
print("\nCome ti chiami capo?")
nome_cliente = input()
print("\nBenvenuto carissimo "  + str(nome_cliente))
print("\nIn che anno sei nato?")
anno_nascita = int(input())
anni_cliente = 2026 - anno_nascita
print("\nQuindi hai: " + str(anni_cliente) +" anni," + " Grande!")
lista_cocktail_anal = ('\nGirolamo' + '\nAstolfo' + '\nBettina' + '\nTony Pitony')
lista_cocktail = ("\nSekiro" + "\nJojo" + "\nNexus" + "\nThe World" + "\nBloodborne" + "\nEstus" + "\nSerpente solido")

if anni_cliente <18:
    print("\nSpiace capo, solo analcolici 4 u" + "\nPer i bimbi come te abbiamo questi cocktail: " + "\n" + str(lista_cocktail_anal))
if anni_cliente >18:
    print("\nVisto che sei maggiorenne ho una sorpresa per te; alcolici!" + "\nQuesti sono i cocktail che puoi acquistare: " "\n" + str(lista_cocktail))
print("\nQuale di questi gradisci?")
lista_cocktail = input()

if lista_cocktail == "Sekiro":
    print("\nMi piace come ragioni Lupo! Il costo è 12$")
if lista_cocktail == "Jojo":
    print("\nPronto a tirare fuori lo Stand? To you 11$")
if lista_cocktail == "Nexus":
    print("\nQual'è la tua attitudine? 6 Fiorini!")
if lista_cocktail == "The Wold":
    print("\nVuoi fermare il tempo? 10$")
if lista_cocktail == "Bloodborne":
    print("\nPronto per la caccia eh? 15 Fiale")
if lista_cocktail == "Estus":
    print("\nCerca di non diventare vuoto. 3.5 anime")
if lista_cocktail == "Serpente solido":
    print("\nKept you waiting uh? 14.15$")
          
recensione = (" \n1* pessimo" + " \n2* meh" + " \n3* decente" + "\n4* ottimo" + "\n5* sta un altro?")
print("\nCosa ne pensi del Cocktail?? Lascia una recensione da 1 a 5! " "\n" + str(recensione))
recensione = input()
          
if recensione == "1*":
    print("\nMi dispiace :c")
if recensione == "2*":
    print("\nPossiamo migliorare")
if recensione == "3*":
    print("\nLe critiche sono costruttive!")
if recensione == "4*":
    print("\nTi ringrazio molto!")
if recensione == "5*":
    print("\nSto volando *-*")
print("\nGRAZIE PER AVERCI SCELTO! TORNA AL PIù PRESTO!!!")

    



    



