# ---------------------- 1. KOD PYTHON (KLASY) ----------------------
init python:
    # Definicja samego przedmiotu (statystyki + wygląd)
    class Item:
        def __init__(self, name, idle_img, hover_img):
            self.name = name
            self.idle_img = idle_img   # Obrazek normalny
            self.hover_img = hover_img # Obrazek po najechaniu myszką

    # Pomocnicza klasa dla przedmiotu leżącego w plecaku (Przedmiot + Pozycja)
    class InventorySlot:
        def __init__(self, item, x, y):
            self.item = item
            self.x = x
            self.y = y

    # Zarządzanie ekwipunkiem
    class Inventory:
        def __init__(self):
            self.slots = [] # Lista przedmiotów wraz z ich pozycjami

        # Metoda dodawania wymaga teraz podania pozycji X i Y
        def add(self, item, x, y):
            new_slot = InventorySlot(item, x, y)
            self.slots.append(new_slot)
            renpy.notify(f"Znaleziono: {item.name}")

        def remove(self, slot):
            if slot in self.slots:
                self.slots.remove(slot)

# ---------------------- 2. EKRAN PLECAKA (SCREEN) ----------------------
# To musi być POZA blokiem init python!

screen plecak_screen():
    modal True # Blokuje klikanie w grę pod spodem
    zorder 100 # Wyświetla się nad wszystkim innym
    frame:
        align (0.5, 0.5)
        xsize 1920  # <--- Tu ustawiasz szerokość swojego obrazka tła
        ysize 1080  # <--- Tu ustawiasz wysokość swojego obrazka tła
        
        background "plecak.png"

        textbutton "Zamknij":
            align (0.98, 0.02)
            action Hide("plecak_screen")

        # --- WYŚWIETLANIE PRZEDMIOTÓW ---
        # Iterujemy przez listę slotów z Twojej klasy Inventory
        for slot in plecak.slots:
            imagebutton:
                idle slot.item.idle_img
                hover slot.item.hover_img
                
                # Używamy X i Y z Twojej klasy InventorySlot
                pos (slot.x, slot.y)
                
                # Co się dzieje po kliknięciu? Na razie wyświetlmy nazwę
                action Notify("To jest: " + slot.item.name)
                
                # Dymek z nazwą po najechaniu myszką
                tooltip slot.item.name

    # Obsługa tooltipa (wyświetlanie nazwy po najechaniu)
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            align (0.5, 0.1)
            size 40
            color "#fff"
            outlines [(2, "#000", 0, 0)]

# ---------------------- 3. ZMIENNE GRY (DEFINICJE) ----------------------
# Tworzymy instancję plecaka
default plecak = Inventory()

# Definiujemy przedmioty
# Pamiętaj, żeby nazwy plików (np. "lom.png") istniały w folderze images!
define przedmiot_lom = Item("Łom", "lom.png", "lom.png") 
define przedmiot_mapa = Item("Mapa", "mapa.png", "mapa.png")
define przedmiot_karta = Item("Karta", "karta.png", "karta.png")

#----------------------------- IKONA PLECAK ------------------------------------
screen plecak_ikona():
    zorder 90 # Warstwa poniżej otwartego plecaka (żeby plecak przykrył ikonę jak się otworzy)
    
    imagebutton:
        # Grafiki ikony (musisz je mieć w folderze images)
        idle "ikona_plecaka.png" 
        hover "ikona_plecaka_hover.png" # Opcjonalne: inna grafika jak najedziesz myszką
        focus_mask True
        # Akcja po kliknięciu
        action Show("plecak_screen")