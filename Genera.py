import matplotlib.pyplot as plt
import numpy as np
import json
from matplotlib import pyplot


class Genera:

    def __init__(self, jsonDate):
        # jsonDate è il file json da inserire nei parametri
        self.jsonDate = jsonDate

        with open(jsonDate) as file:
            data = json.load(file)
            self.data = data

    def genera_xy_totali(self):
        x = []
        y = []
        totale = 0
        tmpGiorno = self.data[0]['data']
        for item in self.data:              #prendo le date di tutte le regioni
            if item['data'] == tmpGiorno:
                totale += item['totale_casi'] 
            else:
                tmpGiorno = item['data']
                tmpGiorno = tmpGiorno[:-9]
                tmpGiorno = tmpGiorno.lstrip('2020')
                y.append(totale)
                x.append(tmpGiorno)
                totale = 0
        return [x, y]


    def genera_xy_regione(self, codiceRegione): # prendo i dati della regione e le vado a sommare
        x = []
        y = []
            
        for item in self.data:
            if  item['codice_regione'] == codiceRegione:
                casi = item['totale_casi']        
                y.append(casi)
                giorno = item['data']
                giorno = giorno[:-9]
                giorno = giorno.lstrip('2020')
                x.append(giorno)
        return [x, y]

    def genera_xy(self, codiceRegione=None):
        if codiceRegione == None:
            return self.genera_xy_totali()
        else:
            return self.genera_xy_regione(codiceRegione)
