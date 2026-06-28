def login(usuario, senha):
    if not usuario or not senha:
        return "Campos obrigatórios"
    if usuario == "admin" and senha == "1234":
        return "Login realizado"
    return "Credenciais inválidas"
