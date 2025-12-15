##Definicje postaci 
default player_name = "hero"
define ja = Character("[player_name]", who_color="#00ccff")
define r = Character("Radio",who_color="#1bdb8b")
define m = Character("???",who_color="#ff0000") # Potwór
## zmienne logiczne ( flagi) do śledzenia postępów
default ma_lom = False
default ma_latarke = False
default ma_bezpiecznik = False
default ma_karta_dostepu= False
default ma_mapa= False
default prad_wlaczony = False
default drzwi_wyjsciowe_otwarte = False
default zbrojownia_otwarta =False
default serwerownia_otwarta = False
default generator_otwarty= False

## ----TŁA---------
image bg PokojStartowy ="pokoj1"
image bg PokojStartowybezswiatla ="pokoj1_no"
image bg Korytarz_no_light ="korytarz_no"
image bg Korytarz = "korytarz"
image bg stolowka ="stoufka"
image bg apteka1 ="apteka"
image bg apteka2 ="apteka2"
image bg generator_swiatlo ="generator_light"
image bg generator_no_swiatlo ="generator_no_light"
image bg serwerownia ="komputerownia"
image bg zbrojownia ="zbrojownia"
image bg drzwi_wyjsciowe ="drzwi_wyjscie"

# ------------------------------------------------------Tutaj sobie możesz sceny na starcie pominąć niebedzie potrzeby przeklikiwania :3
label start:
    show screen plecak_ikona
    menu:
        "TEST SKIPNIJ JAK POTRZEBUJESZ PRZEJŚĆ DALEJ"
        "START GRY":
            jump początek_gry
        "PO WYJŚCIU Z POKOJU":
            jump korytarz_wyjscie_z_pokoju
            $ backpack.add(przedmiot_lom, 0, 0)
            $ ma_lom = True
            $ backpack.add(przedmiot_latarka, 0, 0)
            $ ma_latarke = True
    
#--------------------------------to je muj test-------
    # $ backpack.add(przedmiot_bezpiecznik, 0, 0)
    # $ ma_bezpiecznik = True
    # $ backpack.add(przedmiot_karta, 0, 0)
    # $ ma_karta_dostepu = True
    # $ backpack.add(przedmiot_lom, 0, 0)
    # $ ma_lom = True
    # $ backpack.add(przedmiot_latarka, 0, 0)
    # $ ma_latarke = True
#------------------tak ma być przez ó ------------------------

#------------------------------------------------------------Scena Pierwsza Gdy Gracz zaczyna gre-----------------------------------------------------
    label początek_gry:
        scene bg PokojStartowy 
        "Budzi cię potworny ból głowy. Wokół panuje półmrok, a powietrze pachnie stęchlizną i metalem."
        "Próbujesz wstać, ale twoje ciało odmawia posłuszeństwa"
        "Wydaje ci się że słyszysz znajomy głos, ale nic ci nie jesteś wstanie sobie nic przypomieć"
        "Haloo, haloo???"
        ## play sound "audio/blablabla.ogg" #dzwięk zgaszenia światła
        show radio at right
        r "Odbiór. Raz, dwa, trzy. Czy ten kawał mięsa jeszcze funkcjonuje?"
        show hero_poczatek at left
        ja "Kto... Kto mówi? Gdzie ja jestem?!"
        r "Och. Wspaniale! Funkcje życiowe w normie, ale widzę usterkę w twojej pamięci..."
        r "Chyba za mocno ci wtedy przyjebałem.. No nic"
        r "Witaj w Bunkrze ... . Jestem Pan Radio. Twoim jedynym i ostatnim przyjacielem."
    label Choice:   
        menu:
            " "
            "Odpowiesz na moje pytanie?!" :
                hide hero_poczatek
                show hero_wkurw at left                            # <------- Bohater ???
                ja "Kim jesteś! i co ja tu robie??!"
                hide hero_wkurw
                show hero_podstawowy at left                            # <------- Bohater ???                    
                r "wyluzuuj! bo ci żyłka pęknie"
                r"Jak powiedziałem jestem i nazywam się Pan Radio"
                r"jak chcesz mogę być również Panią"
                hide radio
                show PaniRaddio at right                            # <----- Niedziała 
                r"Widzisz mam wiele wcieleń"
                r"Ha ha ha ha"
                hide PaniRaddio 
                show radio at right
                
            "(Milcz)":  
                ja "Huuuh...?"
                hide hero_poczatek
                show hero_podstawowy at left                             # <------- Bohater ???
            
        r "W każdym razie, cieszę się, że tu jesteś."
        r "Sytuacja jest prosta: drzwi są zamknięte, tlen się kończy a ja się nudzę. Wyjdź stąd, zanim zginiesz."
        r "A właśnie jak ci tam było?"
        $ player_name = renpy.input("Jak masz na imię? ", length=15).strip()
        if player_name == "":
            $ player_name = "hero"
        ja "Możesz na mnie mówić [player_name]"
        ja "Właśnie jak mam stąd wyjść"
        r "Eksploruj. Kombinuj. I na litość boską, nie dotykaj czerwonych przycisków......"
        hide radio    
        ja "Psia mać! muszę coś wykombinować bo oszaleje.."
        hide hero_podstawowy
        "słyszysz jak coś buczy po za twoim pomieszczniem, zaczynają mrugać światła i po chwili kompletnie gasną"
#-----------------Tło się zmienia na brak światła---------
        scene bg PokojStartowybezswiatla
        show hero_wkurw at left
        ja "Świetnie jeszcze tego brakowało.."
        hide hero_wkurw 
    
#-----------------------------------Pierwsza "Zagadka" w grze dzięki niej gracz otrzymuje latarkę i łom-------------------------------------
    label Pokój_startowy_zagadka:
        menu:
            "Co robisz?"
            "Otwórz drzwi" :
                if(ma_lom == False):
                    "Pchasz z całej siły, lecz tylko lekko się poruszają"
                    show hero_poczatek
                    ja "Kurde potrzebuje jakiegoś narzedzia.."
                    hide hero_poczatek
                    if(ma_latarke == False):
                        show hero_wkurw
                        ja "ale tak tu kurwa ciemno że nic nie widzę"
                        hide hero_wkurw
                    else:
                        "zauważasz niewielką szczelinę. Dzięki niej mógłbyś podważyć drzwi"
                    jump Pokój_startowy_zagadka
                else:
                    "wpychasz łom w szczeline i gwałtownie ciągniesz "
                    "zamek od dzrzwi pod naporem się łamie!"
                    show hero_szczesliwy at left
                    ja "Pora iść dalej!"
                    hide hero_szczesliwy
                    jump korytarz_wyjscie_z_pokoju
            "Zajrzyj pod łóżko":  
                if(ma_latarke == False):
                    "próbujesz wypatrzeć cokolwiek ale nic nie widzisz"
                else:
                    if (ma_lom == False):
                        "Gdy spoglądasz pod łóżkiem światło latarki odbija światło coś metalowego"
                        "Ku lekkiemu zdziwieniu znalazłeś łom"
                        $ backpack.add(przedmiot_lom, 0, 0)
                        $ ma_lom = True
                        show hero_podstawowy2 at left
                        ja "Wkońcu będę mógł wyjść"
                        hide hero_podstawowy2
                    else:
                        "Gdy jeszcze raz spoglądasz pod łóżko.. "
                        "zauważasz rozkładające się ciało szczura"
                        "Gdy go zauważyłeś równiez poczułeś odór stęchlizny"
                        show hero_dziwny at left
                        ja "Fuj..."
                        ja " I ja pod tym spałem cały czas?? "
                        ja " nic dziwnego że boli mnie głowa..."
                        hide hero_dziwny
                jump Pokój_startowy_zagadka     
            "podejdź do szafki":
                if (ma_latarke == True):
                    "Szafka jest pusta. Już zabrałeś stąd latarkę."
                    jump Pokój_startowy_zagadka
                else:
                    "powoli podchodzisz do szafki"
                    "Gdy ją otworzyłeś wypadła z niej latarka"
                    $ backpack.add(przedmiot_latarka, 0, 0)
                    $ ma_latarke = True
                    show hero_podstawowy2 at left
                    ja "Super! W końcu coś przydatnego."
                    hide hero_podstawowy2
                jump Pokój_startowy_zagadka
# ----------------------------------------------Scena Druga kiedy Gracz wyjdzie z Pokoju-------------------------------------------------
    label korytarz_wyjscie_z_pokoju:
        scene bg Korytarz_no_light
        "Po otawrciu tych zardzewiałych drzwi, odbija się głośne echo wraz z nim odezwał sie... "
        show radio at right
        r "No wkońcu..."
        r "Dłużej się nie dało..?"
        r "ile można było czekac... Klamki nie umiesz pociągnąć!?"
        ja "ale.. niebyło kla-"
        r "DOBRA słuchaj niema nic do stracenia potrzbujemy zasilania do serwerowni"
        menu:
            " "
            "po co?" :
                r "???"
                r "a twoja koścista dupa chciała by stad wyjść?!"
            "...":
                ja "..."
        r "tak myśle!"
        r "w drogę! Miernoto!"


