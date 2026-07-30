<div align="center">

# 🎀 Flashcards da Barbie 🎀

**Um app de flashcards para o terminal, com estética rosa e roxo**

![Status](https://img.shields.io/badge/status-em%20construção-ff69b4)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Windows-ff1493)
![Python](https://img.shields.io/badge/python-3.8+-ff8fcf)
![Textual](https://img.shields.io/badge/feito%20com-Textual-c77dff)

</div>

`✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ `

## ⟡ Sobre o projeto

Um sistema de flashcards feito para rodar no terminal, pensado para o cyberdeck. 🎀

Você organiza seus cartões em **pastas** por assunto, adiciona quantos flashcards quiser (frente e verso), e estuda um por um: vê a frente, revela o verso quando estiver pronta, e avança para o próximo. Quando os cartões acabam, uma telinha de parabéns aparece para comemorar. 💕

Tudo é guardado em um banco de dados local (SQLite), então seus cartões continuam lá entre uma sessão e outra.

`✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ `

## ⟡ O que ele faz

- Cria, edita e apaga **pastas** para agrupar os cartões por matéria
- Cria, edita e apaga **flashcards** (com frente e verso) dentro de cada pasta
- **Modo estudar**: mostra a frente, revela o verso ao clicar, avança para o próximo
- Tela de **parabéns** ao terminar todos os cartões da pasta
- Avisa quando uma pasta não tem cartões para estudar
- Lista de cartões com rolagem, destacados dos botões de ação
- Paleta rosa e roxo, com molduras arredondadas e efeito de profundidade nos botões

`✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ `

## ⟡ Pré-requisitos

- **Python 3.8 ou superior** instalado
- Um terminal (o do sistema, o do VS Code, ou o do cyberdeck)

Para os cantos arredondados e os símbolos aparecerem perfeitos, o ideal é usar uma **[Nerd Font](https://www.nerdfonts.com/)** no terminal (ex.: *JetBrainsMono Nerd Font*). Sem ela, funciona igual — só os cantos ficam mais retos e alguns símbolos podem virar quadradinhos.

`✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ `

## ⟡ Como baixar

Clone o repositório (ou baixe os arquivos `app.py`, `app.tcss` e `database.py` para a mesma pasta):

```bash
git clone https://github.com/MariaRitaRR/flashcards-da-barbie
cd flashcards-da-barbie
```

`✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ `

## ⟡ Como rodar no Windows

Abra o **PowerShell** na pasta do projeto e siga os passos.

**1. Crie um ambiente virtual** (isola as dependências do projeto):

```powershell
python -m venv .venv
```

**2. Permita a ativação de scripts** (só na primeira vez, nesta sessão):

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

**3. Ative o ambiente virtual:**

```powershell
.venv\Scripts\Activate.ps1
```

Você verá `(.venv)` no começo da linha.

**4. Instale o Textual:**

```powershell
pip install textual
```

**5. Rode o app:**

```powershell
python app.py
```

`✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ `

## ⟡ Como rodar no Linux

Abra o **terminal** na pasta do projeto.

**1. Crie um ambiente virtual:**

```bash
python3 -m venv .venv
```

**2. Ative o ambiente virtual:**

```bash
source .venv/bin/activate
```

Você verá `(.venv)` no começo da linha.

**3. Instale o Textual:**

```bash
pip install textual
```

**4. Rode o app:**

```bash
python app.py
```

`✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ `

## ⟡ Como usar

1. Na tela inicial, escolha uma **pasta** ou clique em **+ Criar pasta**
2. Dentro da pasta você pode:
   - **Adicionar** um novo flashcard (frente e verso)
   - Clicar em um **cartão da lista** para editá-lo
   - **Editar** ou **deletar** a pasta inteira
   - **Estudar** todos os cartões da pasta
3. No modo estudar:
   - Leia a **frente** do cartão
   - Clique em **Ver verso** para revelar a resposta
   - Clique em **Next** para o próximo cartão
   - Ao terminar, aparece a tela de **parabéns** 🎉
- Para sair, pressione **Ctrl + Q**

`✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ `

## ⟡ Estrutura do projeto

| Arquivo | O que faz |
|---|---|
| `app.py` | A interface (telas, botões, navegação) |
| `database.py` | O banco de dados e as funções de acesso (criar, listar, editar, apagar) |
| `app.tcss` | O estilo visual (cores, bordas, espaçamentos) |
| `flashcards.db` | O banco SQLite com suas pastas e cartões (criado automaticamente) |

O projeto separa a **lógica de dados** (`database.py`) da **interface** (`app.py`): a interface nunca escreve SQL, só chama as funções do banco. Isso mantém tudo organizado e fácil de testar.

`✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ `

## ⟡ Personalização

| O que mudar | Onde |
|---|---|
| Cores do fundo, cartões e botões | `app.tcss` |
| Tamanho do flashcard | seletor `#frente, #verso` no `app.tcss` |
| Tamanho e estilo dos cartões na lista | seletor `.card-item` no `app.tcss` |
| Efeito de profundidade dos botões | `border: tall` no seletor `Button` |
| Mensagem da tela de parabéns | classe `ParabensScreen` no `app.py` |

`✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ `

## ⟡ Feito com

- [Python](https://www.python.org/)
- [Textual](https://textual.textualize.io/) — framework de interfaces para terminal
- [SQLite](https://www.sqlite.org/) — banco de dados local

`✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ ♡ ˚ ⋆ ✧ ⋆ ˚ `

<div align="center">

`˚ ⋆ ｡ ˚ ♡ feito com carinho para o cyberdeck ♡ ˚ ｡ ⋆ ˚`

</div>