# 🧪 PBL 12 — Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## 👨‍💻 Integrantes
- Gabriel Sbruzzi

---

## 📦 1. Repositório da Atividade

Repositório no GitHub contendo:
- Código da funcionalidade
- Testes automatizados
- Pipeline de CI configurado

Link: https://github.com/seu-usuario/seu-repositorio

---

## 📝 2. Planejamento da Funcionalidade

### Funcionalidade escolhida:
Validação de login de usuário

### Regras:
- Deve permitir login com usuário e senha válidos
- Deve bloquear login com senha incorreta
- Deve impedir login com campos vazios

---

## 🤖 3. Teste Automatizado

Exemplo utilizando JavaScript + Jest:

```javascript
function login(usuario, senha) {
    if (!usuario || !senha) return "Campos obrigatórios";
    if (usuario === "admin" && senha === "1234") return "Login realizado";
    return "Credenciais inválidas";
}

test("Login com sucesso", () => {
    expect(login("admin", "1234")).toBe("Login realizado");
});

test("Senha incorreta", () => {
    expect(login("admin", "errado")).toBe("Credenciais inválidas");
});

test("Campos vazios", () => {
    expect(login("", "")).toBe("Campos obrigatórios");
});
