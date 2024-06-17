import pandas as pd
import numpy as np

import os
#Auflisten aller Dateien im aktuellen Verzeichnis (Optional) zur Überprüfung ob CSV-File im selben Path ist
files = os.listdir('.')
print(files)
''''
# CSV-Datei einlesen, hier die CSV-Datei zum überarbeiten geben 'xxx.csv'
df = pd.read_csv('Sample_list.csv', sep=';')

# Leere Zellen und 'X'-Zeichen bereinigen aus der Excel-Datei und durch NaN ersetzen "Not a Number" äquivalent zu Null
df.replace('X', np.nan, inplace=True)

# Leere Zellen in spezifischen Spalten auffüllen,
# die Funktion Forward Fill übernimmt den Eintrag des letzten Feldes für die kommende Reihe
df[['ID', 'First Name', 'Last Name']] = df[['ID', 'First Name', 'Last Name']].ffill()

# Datum in das deutsche Format dd.mm.yyyy umwandeln
df['Date of birth'] = pd.to_datetime(df['Date of birth'], errors='coerce', dayfirst=True).dt.strftime('%d.%m.%Y')

def find_people_by_id(df, search_id):
    result = df[df['ID'] == search_id]
    return result

# Suche nach der spezifischen ID
search_id = '50Bb061cB30B461'

result_df = find_people_by_id(df, search_id)
print(result_df)

# Bereinigte Daten in eine neue CSV-Datei speichern, mit "sep = ';'" für die Einteilung in richtige Columns
result_df.to_csv('cleaned_data_Sample_list.csv', index=False, sep=';')