from pathlib import Path
from typing import List

class TodoManager:
    def __init__(self, storage_path: Path):
        """
        Inizializza il manager con il percorso del file di salvataggio.
        Dovrebbe caricare i task esistenti all'avvio.
        """
        self.storage_path = storage_path
        self.tasks: List[str] = []
        # Qui dovresti chiamare il caricamento iniziale

    def _load(self) -> List[str]:
        """
        Metodo privato per caricare i task dal file JSON.
        Gestisce i casi di file mancante o corrotto.
        """
        pass

    def _save(self) -> bool:
        """
        Metodo privato per salvare lo stato attuale dei task su disco.
        """
        pass

    def add_task(self, task: str) -> bool:
        """
        Aggiunge un nuovo task e salva le modifiche.
        """
        pass

    def remove_task(self, index: int) -> bool:
        """
        Rimuove un task in base alla sua posizione (indice).
        Ritorna True se l'operazione ha successo.
        """
        pass

    def get_tasks(self) -> List[str]:
        """
        Ritorna la lista attuale dei task.
        """
        pass
