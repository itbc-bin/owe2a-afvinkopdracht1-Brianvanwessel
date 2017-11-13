# Naam:Brian van Wessel
# Datum:2-11-17
# Versie: 1

# Voel je vrij om de variabelen/functies andere namen te geven als je die logischer vind.

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand, met 5 tot 10 fasta's.
# Ga je runnen met het echte bestand, geef je programma dan even de tijd.

def main():


    bestand = input("geef de naam van het bestand")
    
    if bestand == "GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna":
        bestand2 = open(bestand)
        headers, seqs = lees_inhoud(bestand2)

        zoekwoord = input("Geef een zoekwoord op: ")
        i = 0
        for line in headers[:10]:
            if zoekwoord in line:
                print(80*'-')
                print(headers[i])
                print(seqs[i])
                print(80*'-')
                print(DNA[i])   
                print(80*'-')
            
                if Knipt[i] == "":
                    print("geen match gevonden")
                else:
                    print("Match gevonden met enzym",Knipt[i])
            
                i +=1
            else:
                i += 1
    else:
        print("bestand bestaat niet")
                                                                                    # Voer hier de bestandsnaam van het juiste bestand in, of hernoem je bestand

    DNA = is_dna(seqs)
    Knipt = knipt(seqs)
    """
    Hier onder vind je de aanroep van de lees_inhoud functie, die gebruikt maakt van de bestand variabele als argument.
    De resultaten van de functie, de lijst met headers en de lijst met sequenties, sla je op deze manier op in twee losse resultaten.
    """
        


    
    # schrijf hier de rest van de code nodig om de aanroepen te doen
    is_dna(seqs)
    knipt(seqs)
    
    
def lees_inhoud(bestand):
    bestand = open("GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna")
    headers = []
    seqs = []

    for line in bestand:
        if line[0] == ">" or line[0] == "\t":
            headers.append(line.rstrip())
        else:
            seqs.append(line.rstrip())

    
   
        
    
    
    """
    Schrijf hier je eigen code die het bestand inleest en deze splitst in headers en sequenties.
    Lever twee lijsten op:
        - headers = [] met daarin alle headers
        - seqs = [] met daarin alle sequenties behorend bij de headers
    Hieronder vind je de return nodig om deze twee lijsten op te leveren
    """ 
    
    return headers, seqs

    
def is_dna(seqs):
    """
    Deze functie bepaald of de sequentie (een element uit seqs) DNA is.
    Indien ja, return True
    Zo niet, return False
    """
    hoeveelheidA = []
    hoeveelheidT = []
    hoeveelheidC = []
    hoeveelheidG = []
    totaal = []
    DNA = []
    for line in seqs[:12]:
        A = line.count("A")
        T = line.count("T")
        C = line.count("C")
        G = line.count("G")
        hoeveelheidA.append(A)
        hoeveelheidT.append(T)
        hoeveelheidC.append(C)
        hoeveelheidG.append(G)
        tot = line.count("")
        totaal.append(tot)
    i = 0
    while i < 11 :
        i += 1
        if hoeveelheidA[i] + hoeveelheidT[i] + hoeveelheidC[i] + hoeveelheidG[i] == totaal[i] - 1:
            DNA.append("DNA")
        else:
            DNA.append("Geen DNA")
    return DNA
   


def knipt(seqs):
    """
    Bij deze functie kan je een deel van de code die je de afgelopen 2 afvinkopdrachten geschreven hebt herbruiken

    Deze functie bepaald of een restrictie enzym in de sequentie (een element uit seqs) knipt.
    Hiervoor mag je kiezen wat je returnt, of wellicht wil je alleen maar printjes maken.
    """
    bestand = open ("enzymen.txt")
    list1=[]
    knipt = []
    i2= 0
    while i2 < 9:
        for line in bestand.readlines():    
            enzym, seq = line.split()       
            seq = seq.replace("^","")   
            list1.append(seq)
            x= seqs[i2].find(seq)
            if x > 0:
                #print(80*"-")
                #print("Match met",enzym,"op positie",x)
                #print(seqs[i2])
                #print(80*"-")
                knipt.append(enzym)
                i2 += 1
            else:
                #print(80*"-")
                #print("geen match gevonden")
                #print(80*"-")
                knipt.append("")
                i2 +=1
    return knipt    
main()
