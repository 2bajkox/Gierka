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
    # Ustawienie czarnego tła na start dla budowania napięcia
    scene black with dissolve
    stop music fadeout 2.0
    
    "Budzi cię tępy, pulsujący ból z tyłu czaszki. Próbujesz otworzyć oczy, ale powieki są ciężkie jak ołów."
    "W ustach czujesz metaliczny posmak krwi i stęchliznę."
    "Próbujesz się podnieść. Mięśnie drżą, odmawiając posłuszeństwa. Jesteś słaby... Zbyt słaby."
    
    scene bg PokojStartowy with fade
    
    "Wokół panuje półmrok. Zarysy mebli są niewyraźne, obce."
    "Wydaje ci się, że słyszysz znajomy głos, dobiegający zewsząd i znikąd zarazem. Pamięć jest czarną dziurą."
    
    # Efekt dźwiękowy włączenia głośników/interferencji
    # play sound "audio/static_noise_start.ogg" 
    
    "???" "Haloo... Odbiór...?"
    "???" "Kalibracja w toku. Raz... Dwa... Trzy..."
    
    show radio at right with easeinright
    r "Czy ten zlepek tkanki organicznej wreszcie funkcjonuje?"
    
    show hero_poczatek at left with dissolve
    ja "Kto... Kto tam jest? Gdzie ja jestem?!"
    
    r "Och, wspaniale! Funkcje życiowe w dolnej granicy normy, ale aktywność kory mózgowej... cóż, pozostawia wiele do życzenia."
    r "Widzę usterkę w sektorze pamięci. Reset systemu musiał być bardziej... inwazyjny niż zakładałem."
    r "Witaj w Bunkrze. Jestem Pan Radio. Twój jedyny przyjaciel, nadzorca i... być może sędzia."

    label Choice:   
        menu:
            " "
            "Odpowiesz na moje pytanie?!":
                hide hero_poczatek
                show hero_wkurw at left
                ja "Pytam kim jesteś i co ja tu do cholery robię?!"
                
                hide hero_wkurw
                show hero_podstawowy at left
                
                r "Adrenalina rośnie. Puls przyspiesza. Fascynujące, ale bezcelowe."
                r "Powiedziałem wyraźnie: jestem Pan Radio. Jestem głosem w ścianach."
                r "Mogę być kim zechcę, ale dla ciebie jestem Bogiem tego małego, betonowego świata."
                r "Nie irytuj mnie. Sprzężenie zwrotne bywa bolesne."
               
            "(Milcz i rozglądaj się)":  
                ja "..."
                "Rozglądasz się nerwowo, szukając źródła głosu, ale głośniki są ukryte głęboko w rdzewiejących ścianach."
                
                hide hero_poczatek
                show hero_podstawowy at left
            
    r "W każdym razie, cieszę się, że odzyskałeś przytomność. Statystyki przeżywalności właśnie drgnęły w górę."
    r "Sytuacja jest prosta: drzwi są zaryglowane, system wentylacji... powiedzmy, że ma gorszy dzień, a tlenu ubywa."
    r "Musisz stąd wyjść, zanim udusisz się we własnych wyziewach. Proste, prawda?"
    r "A właśnie... Jak mam opisać ten obiekt w raporcie? Jak się nazywasz?"

    $ player_name = renpy.input("Wpisz swoje imię: ", length=15).strip()
    if player_name == "":
        $ player_name = "Obiekt Zero"
    
    ja "Nazywam się... [player_name]."
    ja "Jak mam stąd wyjść? Drzwi nie mają klamki!"
    
    r "Użyj tego, co zostało ci między uszami. Eksploruj. Imrowizuj. Przetrwaj."
    r "I mała rada: unikaj czerwonych stref. Chyba że lubisz zapach smażonego mięsa."
    
    hide radio with easeoutright    
    
    ja "Cholera jasna... Muszę się stąd wydostać, zanim oszaleję."
    
    hide hero_podstawowy
    
    # Dźwięk awarii zasilania
    # play sound "audio/power_down.ogg"
    
    "Nagle słyszysz głośne buczenie transformatora gdzieś za ścianą. Światła zaczynają migotać, by po chwili zgasnąć całkowicie."
    
    scene bg PokojStartowybezswiatla
    
    "Zostajesz w absolutnej ciemności."
    
    show hero_wkurw at left
    ja "Świetnie... Po prostu świetnie."
    hide hero_wkurw 
    
    #-----------------------------------PĘTLA ZAGADKI-------------------------------------
    
    label Pokój_startowy_zagadka:
        menu:
            "Co robisz?"
            
            "Spróbuj otworzyć drzwi":
                if ma_lom == False:
                    "Pchasz drzwi z całej siły, zapierając się nogami o podłogę. Ani drgną. Są ciężkie, pancerne."
                    show hero_poczatek at left
                    ja "Bez szans. Potrzebuję dźwigni, jakiegoś narzędzia..."
                    hide hero_poczatek
                    
                    if ma_latarke == False:
                        show hero_wkurw at left
                        ja "Jest tu tak ciemno, że nie widzę własnych rąk. Muszę znaleźć źródło światła."
                        hide hero_wkurw
                    else:
                        "Światło latarki pada na framugę. Zauważasz, że zawiasy są skorodowane. Wystarczy coś, czym można je podważyć."
                    
                    jump Pokój_startowy_zagadka
                
                else:
                    "Wsuwasz łom w szczelinę między drzwiami a framugą. Metal zgrzyta przeraźliwie."
                    "Napierasz całym ciężarem ciała. Rdza puszcza z głośnym trzaskiem."
                    
                    show hero_szczesliwy at left
                    ja "Mamy to!"
                    hide hero_szczesliwy
                    
                    jump korytarz_wyjscie_z_pokoju

            "Zajrzyj pod łóżko":  
                if ma_latarke == False:
                    "Klękasz i macasz ręką w ciemności pod łóżkiem. Dotykasz czegoś lepkiego i kurzu, ale nic nie widzisz."
                    ja "Nic z tego. Potrzebuję światła."
                else:
                    if ma_lom == False:
                        "Kierujesz strumień światła pod brudny materac. Coś odbija blask."
                        "Sięgasz głębiej i wyciągasz ciężki, zardzewiały łom."
                        
                        $ backpack.add(przedmiot_lom, 0, 0)
                        $ ma_lom = True
                        
                        show hero_podstawowy2 at left
                        ja "Solidny kawał żelastwa. Może posłużyć jako klucz... albo broń."
                        hide hero_podstawowy2
                    else:
                        "Ponownie oświetlasz przestrzeń pod łóżkiem."
                        "Dostrzegasz wyschnięte truchło szczura wciśnięte w kąt. Jego małe zęby są wyszczerzone w wiecznym grymasie."
                        
                        show hero_dziwny at left
                        ja "Obrzydlistwo..."
                        ja "Czy ja spałem nad tym czymś? Nic dziwnego, że boli mnie głowa..."
                        hide hero_dziwny
                
                jump Pokój_startowy_zagadka     

            "Przeszukaj szafkę nocną":
                if ma_latarke == True:
                    "Szafka jest pusta. Zabrałeś już wszystko, co było w środku."
                    jump Pokój_startowy_zagadka
                else:
                    "Podchodzisz po omacku do szafki. Twoje palce trafiają na chłodny metal."
                    "Otwierasz szufladę. Coś ciężkiego turla się w twoją stronę."
                    "To latarka. Klikasz włącznik – działa! Snop bladego światła przecina ciemność."
                    
                    $ backpack.add(przedmiot_latarka, 0, 0)
                    $ ma_latarke = True
                    
                    show hero_podstawowy2 at left
                    ja "Nareszcie coś widzę."
                    hide hero_podstawowy2
                
                jump Pokój_startowy_zagadka

# ----------------------------------------------SCENA DRUGA: KORYTARZ-------------------------------------------------

label korytarz_wyjscie_z_pokoju:
    scene bg Korytarz_no_light with wipeleft
    
    "Drzwi ustępują z jękiem. Wychodzisz na korytarz. Echo twoich kroków niesie się w nieskończoność."
    "Głośniki w korytarzu budzą się do życia z cichym trzaskiem."
    
    show radio at right
    r "Brawo. Pierwszy test inteligencji zaliczony."
    r "Szczerze? Obstawiałem, że umrzesz z głodu wpatrując się w klamkę."
    r "Ale nie świętuj jeszcze. To dopiero przedsionek."
    
    ja "Zamknij się. Co teraz?"
    ja "Dlaczego nie ma zasilania?"
    
    r "Bystrzak. Zasilanie główne padło dekady temu. Działamy na oparach."
    r "Musisz dostać się do serwerowni i zrestartować generator. Potrzebujemy energii."
    
    menu:
        " "
        "Po co ci energia?":
            r "A po co tobie tlen?"
            r "Bez energii systemy podtrzymywania życia ostatecznie padną. Twoja koścista dupa zostanie tu na zawsze."
            r "Jako eksponat."
        
        "(Milcz)":
            ja "..."
            r "Milczenie jest złotem, ale działanie jest życiem."
    
    r "Ruszaj się, [player_name]. Zegar tyka."
    r "I uważaj na cienie. Czasem... mają zęby."
    
    hide radio
    
    "Korytarz ciągnie się w mrok. Ściskasz łom w dłoni tak mocno, że bieleją ci knykcie."
    
    # Koniec demo lub przejście dalej
    return
