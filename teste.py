usuario = "Thiago"
idade = 21
altura = 1, 72
senha = "thiago123"

print("BEM VINDO AO SISTEMA ")
print("ESTAMOS VERIFICANDO SUA IDENTIDADE")
print("VOCÊ FOI IDENTIFICADO COMO: ", usuario)

if senha == "thiago123":
    print("Senha Correta!".upper())

if senha != "thiago123":
    print("Senha incorreta!".upper())
