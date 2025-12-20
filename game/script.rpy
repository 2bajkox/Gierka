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
image bg stolowka_no = "stoufka_no"
image bg apteka_light ="szpital2"
image bg apteka_no_light ="szpital_no"
image bg generator_swiatlo ="generator"
image bg generator_no_swiatlo ="generator_no"
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
        "Wejście do pomieszczenia z generatorem":
            jump Pomieszczenie_Z_Generatorem_Fab
    
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

#------------------------------------------------------------Scena Pierwsza-----------------------------------------------------
#region Opis Sceny Pierwszej (btw możesz to zminimalizować)

#Gracz budzi się z ogromną amnezją, wita go Pan Radio i "tłumaczy" sytuacje w jakiej się znajduje na koniec rozmowy gasną światła.
#Gracz ma za zadanie odnaleźć przedmioty które pozwolą mu wyjść z tego ciemnego pomieszczenia. 

#endregion 
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
            
        r "W każdym razie, cieszę się, że tu jesteś."
        r "Sytuacja jest prosta: drzwi są zamknięte, tlen się kończy a ja się nudzę. Wyjdź stąd, zanim zginiesz."
        r "A właśnie jak ci tam było?"
        $ player_name = renpy.input("Jak masz na imię? ", length=15).strip()
        if player_name == "":
            $ player_name = "hero"
        ja "Możesz na mnie mówić [player_name]"
        ja "Właśnie jak mam stąd wyjść"
        r "Eksploruj. Kombinuj. i takie tam.."
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
#---Dialogi gdy gracz KLIKNIE W DRZWI Drzwi
            "Otwórz drzwi" :
#gdy niema łomu
                if(ma_lom == False):
                    "Pchasz z całej siły, lecz tylko lekko się poruszają"
                    show hero_poczatek
                    ja "Kurde potrzebuje jakiegoś narzedzia.."
                    hide hero_poczatek
                    
                    if ma_latarke == False:
                        show hero_wkurw at left
                        ja "Jest tu tak ciemno, że nie widzę własnych rąk. Muszę znaleźć źródło światła."
                        hide hero_wkurw
#gdy niema łomu, lecz ma latarkę
                    else:
                        "Światło latarki pada na framugę. Zauważasz, że zawiasy są skorodowane. Wystarczy coś, czym można je podważyć."
                    
                    jump Pokój_startowy_zagadka
#Jeśli ma łom przechodzi do nastepnej sceny
                else:
                    "Wsuwasz łom w szczelinę między drzwiami a framugą. Metal zgrzyta przeraźliwie."
                    "Napierasz całym ciężarem ciała. Rdza puszcza z głośnym trzaskiem."
                    
                    show hero_szczesliwy at left
                    ja "Mamy to!"
                    hide hero_szczesliwy
                    
                    jump korytarz_wyjscie_z_pokoju
#---Dialogi gdy gracz KLIKA W ŁÓŻKO
            "Zajrzyj pod łóżko":  
#JEZELI NIEMA LATARKI
                if(ma_latarke == False):
                    "próbujesz wypatrzeć cokolwiek ale nic nie widzisz"
                else:
#GDY MA LATARKĘ OTRZYMUJE ŁOM
                    if (ma_lom == False):
                        "Gdy spoglądasz pod łóżkiem światło latarki odbija światło coś metalowego"
                        "Ku lekkiemu zdziwieniu znalazłeś łom"
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
#---Dialogi gdy gracz KLIKA W SZAFKE
            "podejdź do szafki":
                if (ma_latarke == True):
                    "Szafka jest pusta. Już zabrałeś stąd latarkę."
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
# --------------------------------------------------------------------Scena Druga Korytarz -------------------------------------------------
#region Opis Sceny Drugiej
#-Gracz zostaje "Pochwalony" przez pana radio za rozwiązanie poprzedniej zagadki. Gracz dowiaduje się o następnym celu jakim jest odpalenie generatora by przywrócić zasilanie serwerowni by mógł wyjść z tej placówki.
#-Gra (pan radio) Prowadzi gracza do pomieszczenia z generatorem 
#-Gracz w tej scenie dowiaduję się o przeszłości tego bunkra (jaki był jego cel, jaki jest kryzys na powierzchni i co się stało w bunkrzę)
#- w dalszej części przechodzi do generatora
#endregion 
    label korytarz_wyjscie_z_pokoju:
        scene bg Korytarz_no_light
        "Po otwarciu tych zardzewiałych drzwi, odbija się głośne echo wraz z nim odezwał sie... "
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
                r "a twoja koścista dupa chciała wyjść z tej zapchlonej dziury?!"
            "...":
                ja "..."
        r "tak myśle!"
        r "w drogę! Miernoto!"
        hide radio
        "Zirytowany Pan radio prowadzi cię ku pomieszczeniu z generatorem, zmeczony zaczynasz iść za jego głosem"
        "Gdy Odpalasz latarkę zauważasz jak ściany są pokryte zardzewiałymi, brudnymi blachami,a co niektóre są spowitę mchem"
        "Zastanawia cię jednak, historia tej placówki, jak długo tutaj spałeś..? Kim jesteś? i czy możesz zaufać tej osobie za postacią radia..?"
        "Gdy próbowałeś co kolwiek sobie przypomieć po paru metrach nagle nadepnąłeś na jakąś dziwną substancję.. Przykleiła się do twojego buta..."
        "Gdy rozświetliłeś to latarką, zauważyłeś starą lekko już zeschniętą krew... Uświadomiłeś sobie w tym momencie, że tylko wy przetrwaliście.."
        "Gdy spojrzałeś przed siebie było jeszcze wiecej krwi na podłodzę jak i na ścianach, ale nie to cię najbardziej obawiało..."
        "Wielkie ślady szponów i wgnieceń na ścianach zmroziło twoją krew w żyłach.."
        "Z lekkim przerażeniem zacząłeś się wypytywać"
        ja "Co tu się stało? Kto to zrobił?"
        r "..."
        r "Ten bunkier miał za zadanie przeanalizować ciało obego i przedworzyć ją w broń biologiczną do powstrzymania kryzysu na powierzchni"
        ja "huuuh??!"
        label Rozmowa_O_Przeszłości:
            menu:
                "I ten obcy to wszystko zrobił?!":
                    r "HA!"
                    r "oczywiście że nie"
                    r "bo nieżył.."
                    r "Byliśmy już gotowi do masowej produkcji!"
                    r "ale.."
                    ja "Alee..?"
                    r "był pewien efekt uboczny.."
                    ja "jaki ??"
                    r "Patrz pod nogi lepiej"
                    jump Rozmowa_O_Przeszłości
                "O Jaki Kryzys ci chodzi?":
                    r "Wojna"
                    r "bunkier miał nam pozwolić na ukrycie się przed siłami wroga oraz.."
                    r "Ta..  'Broń'. Była naszym pewnym zwycięstwem dla naszwgo wojska"
                    r "Dlatego Ten Bunkier powstał.. Jako ośrodek badawczy."
                    r "Chcieli byśmy stworzyli broń na podstawie ciała obcego znaleźonego na wraku statku"
                    r "niewiadomo jednak czy był jednynym.."
                    jump Rozmowa_O_Przeszłości
                "Jaka Broń biologiczna ":
                    r "..."
                    r "nazywało się to Projektem Arka"
                    r "Ale zawiódł.."
                    jump Rozmowa_O_Przeszłości
                "Idź dalej":
                    "Postanawiasz iść dalej"
        "Po paru metrach zaczynasz zauważać tabliczkę nad drzwiami z napisem Generator"
        ja "Już Dotarłem!"
        r "Noo wkońcu!"
        r "Dłużej się nie dało?"
        jump Pomieszczenie_Z_Generatorem_Fab
#-------------------------------------------------------------------------Scena trzecia Gaenerator-----------------------------------------------------------------
#region Opis sceny Trzeciej
#-Gracz W pomieszczeniu z generatorem odkryje mape placówki do łatwiejszego przemieszczania się. 
#-Od tego momentu gra stawia na lekką swobodę do przemnieszczania się po pokojach.
#-Gracz by mógł odpalić generator potrzebuje bezpiecznika, znajdzie go w składzie medycznym.
#endregion Region name
    label Pomieszczenie_Z_Generatorem_Fab:
        scene bg generator_no_swiatlo
        "Wchodzisz Do ciemnego pomieszczenia czujesz w powietrzu jakby cos się spaliło"
        "Gdy rozświetlasz to pomieszczenia latarką zauważasz kilka łóżek i stół naprawczy"
        "najpewniej ten pokój słóżył jako pomieszczenie przmysłowe lub warsztat gdy próbujesz się jeszcze rozejrzeć przerywa ci Pan radio"
        r "I co widzisz ten generator??"
        ja "tak.. "
        r "najpewneiej bezpiecznik się znowu przepalił... na stole powinieneś znaleźć ich wiecej"
        "Rozglądasz się za bezpiecznikami zauważasz jedynie mape placówki!" #                                <-----------------------------Dostaje mapę
        ja "niema Ich"
        r "co?!"
        r "ehh.. idź je znaleźć!!! i to szybko zanim się przebu-"
        ja "co?"
        r "nic, idź"
#region Dodanie mapy!!!!!!
#---------------------W tym momencie gracz może se KLIKIIIIKAĆ GDZIE CHCEEEEEEEEE!!!!!!!!!!!!!!!!!!!!@!!!DDSFUJSDLFBDASLJN;FLkaASD NAAAAA MAPIEEEEEEEE-----------\
#endregion 
    menu:
        "Wybór Pomieszczeń (W tym momencie gracz może se KLIKIIIIKAĆ GDZIE CHCEEEEEEEEE!!!!!!!!!!!!!!!!!!!!@!!!DDSFUJSDLFBDASLJN;FLkaASD NAAAAA MAPIEEEEEEEE)"
        "Pomieszczenie Przemysłowe":
            jump Pomieszczenie_Z_Generatorem
        "Pomieszczenie startowe":
            jump Pomieszczenie_Startowe
        "pomieszczenie medyczne":
            jump Pomieszczenie_Medyczne
        "Serwerownia":
            jump Serwerownia
        "Zbrojownia":
            jump Zbrojownia
        "Stołówka":
            jump Stołówka
label Pomieszczenie_Z_Generatorem:
    if(prad_wlaczony):
        scene bg generator_swiatlo
    else:
        scene bg generator_no_swiatlo
    "Przechodzisz do pomieszczenia poszukać czegoś wiecej"

label Pomieszczenie_Startowe:
    if(prad_wlaczony):
        scene bg PokojStartowy
    else:
        scene bg PokojStartowybezswiatla
    "Przechodzisz do pomieszczenia poszukać czegoś wiecej"

label Pomieszczenie_Medyczne:
    if(prad_wlaczony):
        scene bg apteka_light
    else:
        scene bg apteka_no_light
    "Przechodzisz do pomieszczenia poszukać czegoś wiecej"

label Serwerownia:
    scene bg serwerownia
    "Przechodzisz do pomieszczenia poszukać czegoś wiecej"

label Zbrojownia:
    scene bg zbrojownia
    "Przechodzisz do pomieszczenia poszukać czegoś wiecej"

label Stołówka:
    if(prad_wlaczony):
        scene bg stolowka
    else:
        scene bg stolowka_no
    "Przechodzisz do pomieszczenia poszukać czegoś wiecej"
