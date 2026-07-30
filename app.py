from textual.app import App, ComposeResult
from textual.widgets import Button, Static, Input
from textual.screen import Screen
from textual.containers import Horizontal, VerticalScroll, Container
from database import con, listar_pastas,deletar_pasta, criar_pasta, editar_pasta, buscar_pasta, criar_card, editar_card, listar_cards, buscar_card


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
            self.app.push_screen(CriarPastaScreen())
        elif button_id.startswith("pasta-"):
            pasta_id = int(button_id.split("-")[1])   # "pasta-3" → 3
            titulo = event.button.label               # o texto do botão
            self.app.push_screen(OpcoesPastaScreen(pasta_id, str(titulo)))

    def on_screen_resume(self) -> None:
        self.call_after_refresh(self.recompose)

class CriarPastaScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Nome da pasta", id="nome-pasta")
        yield Button("Salvar", id="salvar")
        yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "salvar":
            
            nome= self.query_one("#nome-pasta").value
            if nome.strip():       
                criar_pasta (con, nome)
                self.notify(f"Pasta '{nome}' criada com sucesso!")
                self.app.pop_screen()
            else:
                self.notify("Digite um nome", severity="warning") 

        elif event.button.id == "voltar":
            self.app.pop_screen()

class EditarPastaScreen(Screen):
    def __init__(self, pasta_id, titulo):
        super().__init__()
        self.pasta_id = pasta_id
        self.titulo = titulo

    def compose(self) -> ComposeResult:
        yield Input(value=self.titulo, id="novo-nome-pasta")
        yield Button("Salvar", id="salvar")
        yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "salvar":
            
            nome= self.query_one("#novo-nome-pasta").value
            if nome.strip():       
                editar_pasta(con, self.pasta_id, nome) 
                self.notify(f"Pasta '{nome}' atualizada com sucesso!")
                self.app.pop_screen()
            else:
                self.notify("Digite um nome", severity="warning") 

        elif event.button.id == "voltar":
            self.app.pop_screen()

class AdicionarCardScreen(Screen):
    def __init__(self, pasta_id):
        super().__init__()
        self.pasta_id = pasta_id

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Frente", id="card-frente")
        yield Input(placeholder="Verso", id="card-verso")
        yield Button("Salvar", id="salvar")
        yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "salvar":
            frente = self.query_one("#card-frente").value
            verso = self.query_one("#card-verso").value
            if frente.strip() and verso.strip():
                criar_card(con, frente, verso, self.pasta_id)
                self.notify("Card criado com sucesso!")
                self.app.pop_screen()
            else:
                self.notify("Campo em branco!", severity="warning")
        elif event.button.id == "voltar":
            self.app.pop_screen()

class EditarCardScreen(Screen):
    def __init__(self,card_id, frente, verso):
        super().__init__()
        self.card_id = card_id
        self.frente = frente
        self.verso = verso


    def compose(self) -> ComposeResult:
        yield Input(value=self.frente, id="card_frente")
        yield Input(value=self.verso, id="card_verso")
        yield Button("Salvar", id="salvar")
        yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event: Button.Pressed) -> None:

        if event.button.id == "salvar":
            frente = self.query_one("#card_frente").value
            verso = self.query_one("#card_verso").value
            if frente.strip() and verso.strip():
                editar_card(con, self.card_id, frente, verso)   # id, frente, verso
                self.notify("Card atualizado com sucesso!")
                self.app.pop_screen()
            else:
                self.notify("Campo em branco!", severity="warning")
        elif event.button.id == "voltar":
            self.app.pop_screen()
        
class EstudarScreen(Screen):
    def __init__(self, pasta_id):
        super().__init__()
        self.pasta_id = pasta_id
        self.cards = listar_cards(con, pasta_id)
        self.indice = 0

    def compose(self) -> ComposeResult:
        card_atual = self.cards[self.indice]     # a tupla do card: (id, frente, verso, pasta_id)
        with Container():
            yield Static(card_atual[1], id="frente") # frente = índice 1
            yield Static("", id="verso")             # verso começa vazio (escondido)
            yield Button("Ver verso", id="ver-verso")
            yield Button("Next", id="next")
            yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "ver-verso":
            # mostrar o verso: pega o Static #verso e muda o texto dele
            card_atual = self.cards[self.indice]
            self.query_one("#verso").update(card_atual[2])   # verso = índice 2
        elif event.button.id == "next":
            self.indice += 1                     # avança
            if self.indice >= len(self.cards):   # passou do último?
                self.app.switch_screen(ParabensScreen())
            else:
                self.call_after_refresh(self.recompose)                # redesenha com o próximo card
        elif event.button.id == "voltar":
            self.app.pop_screen()

class ParabensScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Static ("✧ ⋆ ˚ ♡ ˚ ⋆ ✧ Parabens ✧ ⋆ ˚ ♡ ˚ ⋆ ✧")
        yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "voltar":
            self.app.pop_screen()
        
class OpcoesPastaScreen(Screen):
    def __init__(self, pasta_id, titulo):
        super().__init__()          # obrigatório: chama o init da classe base
        self.pasta_id = pasta_id    # guarda pra usar depois
        self.titulo = titulo

    def compose(self) -> ComposeResult:

        cards=listar_cards(con,self.pasta_id)
        yield Static(self.titulo)   # mostra qual pasta é
        with Horizontal():
            yield Button("Editar pasta", id="editar-pasta")
            yield Button("Deletar pasta", id="deletar-pasta")

        with VerticalScroll():
            for card in cards:
                yield Button(card[1], id=f"card-{card[0]}", classes="card-item")
            
        with Horizontal():
            yield Button("Estudar", id="estudar")
            yield Button("Adicionar", id="adicionar")
        yield Button("← Voltar", id="voltar")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "voltar":
            self.app.pop_screen() 
        elif button_id == "deletar-pasta": 
            deletar_pasta(con, self.pasta_id)
            self.notify(f"Pasta '{self.titulo}' deletada")
            self.app.pop_screen()
        elif button_id == "editar-pasta":
            self.app.push_screen(EditarPastaScreen(self.pasta_id, str(self.titulo)))
        elif button_id == "adicionar":
            self.app.push_screen(AdicionarCardScreen(self.pasta_id))
        elif button_id.startswith("card-"):
            card_id = int(button_id.split("-")[1])    
            frente, verso = buscar_card(con, card_id)             
            self.app.push_screen(EditarCardScreen(card_id, frente, verso))
        elif button_id == "estudar":
            cards = listar_cards(con, self.pasta_id)
            if not cards:
                self.notify("Nenhum card para estudar!", severity="error")
            else:
                self.app.push_screen(EstudarScreen(self.pasta_id))


    def on_screen_resume(self) -> None:
        self.titulo = buscar_pasta(con, self.pasta_id)
        self.call_after_refresh(self.recompose)


class FlashcardsApp(App):
    CSS_PATH = "app.tcss"
    def on_mount(self) -> None:
        self.push_screen(PastasScreen())


if __name__ == "__main__":
    FlashcardsApp().run()