# 📄 1. `login.py` (código)

```python
def login(usuario, senha):
    if not usuario or not senha:
        return "Campos obrigatórios"
    if usuario == "admin" and senha == "1234":
        return "Login realizado"
    return "Credenciais inválidas"
```

---

# 🧪 2. `tests/test_login.py` (teste automatizado)

```python
from login import login

def test_login_sucesso():
    assert login("admin", "1234") == "Login realizado"

def test_login_senha_errada():
    assert login("admin", "errado") == "Credenciais inválidas"

def test_login_campos_vazios():
    assert login("", "") == "Campos obrigatórios"
```

---

# 📦 3. `requirements.txt` (dependências)

```txt
pytest
```

---

# ⚙️ 4. `.github/workflows/quality.yml` (pipeline)

```yaml
name: Quality Pipeline

on:
  push:
    branches:
      - main

jobs:
  testes:
    runs-on: ubuntu-latest

    steps:
      - name: Baixar código
        uses: actions/checkout@v3

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar dependências
        run: pip install -r requirements.txt

      - name: Rodar testes
        run: pytest
```

---

# 📝 5. `aula-17-integracao-continua-qualidade.md` (ENTREGA)

Aqui vai um modelo já no padrão do professor 👇

````md
# 🧪 PBL 12 — Integração Contínua

## 🔹 1. Repositório da Atividade

| Item | Descrição |
|------|----------|
| Nome do repositório | pbl-12-qualidade-ci |
| Link do repositório | https://github.com/SEU-USUARIO/pbl-12-qualidade-ci |

### Estrutura:
pbl-12-qualidade-ci/tests/test_login.py  
pbl-12-qualidade-ci/.github/workflows/quality.yml  
pbl-12-qualidade-ci/requirements.txt  
pbl-12-qualidade-ci/login.py  

---

## 🔹 2. Planejamento da Funcionalidade

| Item | Descrição |
|------|----------|
| Título da Issue | Login de usuário |
| Objetivo | Permitir login válido e bloquear inválido |
| Link da Issue | https://github.com/SEU-USUARIO/pbl-12-qualidade-ci/issues/1 |

---

## 🔹 3. Teste Automatizado

| Item | Descrição |
|------|----------|
| Tipo de teste | Unitário |
| Objetivo | Validar comportamento do login |
| Link | https://github.com/SEU-USUARIO/pbl-12-qualidade-ci/blob/main/tests/test_login.py |

### Código:
```python
# cole aqui o teste
````

---

## 🔹 4. Pipeline

| Item   | Descrição                                                                                                                                                                                |
| ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nome   | Quality Pipeline                                                                                                                                                                         |
| Evento | Push na main                                                                                                                                                                             |
| Link   | [https://github.com/SEU-USUARIO/pbl-12-qualidade-ci/blob/main/.github/workflows/quality.yml](https://github.com/SEU-USUARIO/pbl-12-qualidade-ci/blob/main/.github/workflows/quality.yml) |

---

## 🔹 5. Indicadores

| Indicador         | Valor     |
| ----------------- | --------- |
| Testes executados | 3         |
| Sucesso           | 3         |
| Falha             | 0         |
| Status            | ✅ Sucesso |

---

## 🔹 6. Defeito

| Item       | Descrição                                                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------------------------------------- |
| Título     | Login aceita senha errada                                                                                                  |
| Severidade | Alta                                                                                                                       |
| Link       | [https://github.com/SEU-USUARIO/pbl-12-qualidade-ci/issues/2](https://github.com/SEU-USUARIO/pbl-12-qualidade-ci/issues/2) |

Descrição:
Sistema aceitava senha incorreta.
Identificado via teste automatizado.
Corrigido ajustando validação.

```
Só falar 👍
```
