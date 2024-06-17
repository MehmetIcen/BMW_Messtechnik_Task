import pandas as pd
import numpy as np

#Auflisten aller Dateien im aktuellen Verzeichnis (Optional) zur Überprüfung ob CSV-File im selben Project ist zur Verarbeitung

'''import os
files = os.listdir('.')
print(files)'''

# CSV-Datei einlesen, hier die CSV-Datei zum überarbeiten geben 'xxx.csv' oder den Pfad zur CSV-Datei
df = pd.read_csv('Sample_list.csv', sep=';')

# Leere Zellen und 'X'-Zeichen bereinigen aus der Excel-Datei und durch NaN ersetzen "Not a Number" äquivalent zu Null
df.replace('X', np.nan, inplace=True)

# Leere Zellen in spezifischen Spalten auffüllen, die Funktion Forward Fill übernimmt den Eintrag des letzten Feldes für die kommende Zelle
df[['ID']] = df[['ID']].ffill()
#Provisorische Lösung, Überarbeitung notwendig - ffill() limitiert auf maximal 1, damit Inhalt der CSV-Datei äquivalent zur xlsx-Datei ist
df[['Last Name']] = df [['Last Name']].ffill(limit = 1)

# Datum in das deutsche Format dd.mm.yyyy umwandeln
df['Date of birth'] = pd.to_datetime(df['Date of birth'], errors='coerce', dayfirst=True).dt.strftime('%d.%m.%Y')

#Funktion zur Suche nach spezifischer Personen-ID
def find_people_by_id(df, search_id):
    result = df[df['ID'] == search_id]
    return result

search_id = '5d2feAfbdCAA6B5'

result_df = find_people_by_id(df, search_id)
print(result_df)

# Bereinigte Daten in eine neue CSV-Datei speichern, mit "sep = ';'" für die Einteilung der Spalten und Reihen
result_df.to_csv('cleaned_data_Sample_list.csv', index=False, sep=';')
