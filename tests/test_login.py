from login import login

def test_login_sucesso():
    assert login("admin", "1234") == "Login realizado"

def test_login_senha_errada():
    assert login("admin", "errado") == "Credenciais inválidas"

def test_login_campos_vazios():
    assert login("", "") == "Campos obrigatórios"
