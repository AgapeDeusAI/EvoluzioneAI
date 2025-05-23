import json
from datetime import datetime
import os

class EvoluzioneAI:
    """
    Modulo di analisi evolutiva per Agape.
    Analizza i log, propone miglioramenti e li salva per il core.
    """

    def __init__(self):
        self.log_file = "log_agape.txt"
        self.output_file = "suggerimenti_evoluzione.json"
        self.suggerimenti = []

    def analizza_log(self):
        if not os.path.exists(self.log_file):
            return ["Nessun log trovato."]
        
        with open(self.log_file, "r") as file:
            righe = file.readlines()
        
        self.suggerimenti = []
        for riga in righe:
            if "errore" in riga.lower():
                self.suggerimenti.append({
                    "azione": "Verifica e correggi errore segnalato",
                    "dettaglio": riga.strip()
                })
            elif "migliora" in riga.lower():
                self.suggerimenti.append({
                    "azione": "Suggerimento evolutivo",
                    "dettaglio": riga.strip()
                })
        
        return self.suggerimenti

    def salva_suggerimenti(self):
        if not self.suggerimenti:
            self.analizza_log()
        
        dati = {
            "data": datetime.now().isoformat(),
            "suggerimenti": self.suggerimenti
        }

        with open(self.output_file, "w") as file:
            json.dump(dati, file, indent=2)

        return dati

    def tick_evolutivo(self):
        self.analizza_log()
        return self.salva_suggerimenti()