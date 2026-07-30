from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.screen import Screen
from textual.containers import Horizontal
from database import con, listar_pastas,deletar_pasta


class PastasScreen(Screen):
    def compose(self) -> ComposeResult:
        pastas = listar_pastas(con)

        with Horizontal():
            for pasta in pastas:
                yield Button(pasta[1], id=f"pasta-{pasta[0]}")
            yield Button("+ Criar pasta", id=f"criar-pasta")
            

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "criar-pasta":
            self.notify(f"Criar nova pasta")
        elif button_id.startswith("pasta-"):
            pasta_id = int(button_id.split("-")[1])   # "pasta-3" → 3
            titulo = event.button.label               # o texto do botão
            self.app.push_screen(OpcoesPastaScreen(pasta_id, str(titulo)))

    def on_screen_resume(self) -> None:
        self.call_after_refresh(self.recompose)


class OpcoesPastaScreen(Screen):
    def __init__(self, pasta_id, titulo):
        super().__init__()          # obrigatório: chama o init da classe base
        self.pasta_id = pasta_id    # guarda pra usar depois
        self.titulo = titulo


    def compose(self) -> ComposeResult:
        yield Static(self.titulo)   # mostra qual pasta é
        with Horizontal():
            yield Button("Editar pasta", id="editar-pasta")
            yield Button("Deletar pasta", id="deletar-pasta")
        with Horizontal():
            yield Button("Estudar", id="estudar")
            yield Button("Adicionar", id="adicionar")
            yield Button("Editar", id="editar")
        yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "voltar":
            self.app.pop_screen()
        elif button_id == "deletar-pasta": 
            deletar_pasta(con, self.pasta_id)
            self.notify(f"Pasta '{self.titulo}' deletada")
            self.app.pop_screen()


class FlashcardsApp(App):
    def on_mount(self) -> None:
        self.push_screen(PastasScreen())


if __name__ == "__main__":
    FlashcardsApp().run()