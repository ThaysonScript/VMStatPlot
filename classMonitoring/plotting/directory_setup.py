from pathlib import Path

class DirectorySetup:
    def __init__(self, *dirs):
        self.dirs = dirs

    def check_and_create_dirs(self):
        for directory in self.dirs:
            if not directory.exists():
                directory.mkdir()
                print(f"{directory} criado com sucesso.")
            else:
                print(f"Verificação de diretório {directory} feita.")