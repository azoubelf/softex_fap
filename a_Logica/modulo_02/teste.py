

resposta = input("É terrestre? ")


if resposta.lower() == "sim":
    resposta = input("Tem motor? ")
    if resposta.lower() == "sim":
        resposta = input("Tem duas rodas? ")
        if resposta.lower() == "sim":
            print("Moto")
        else:
            resposta = input("Anda sobre trilhos? ")
            if resposta.lower() == "sim":
                print("Trem")
            else:
                resposta = input("Transporta muitas pessoas? ")
                if resposta.lower() == "sim":
                    print("Ônibus")
                else:
                    resposta = input("Cabe apenas uma pessoa? ")
                    if resposta == "sim":
                        print("Trator")
                    else:
                        resposta = input("É usado para carregar cargas pesadas? ")
                        if resposta == "sim":
                            print("Caminhão")
                        else:
                            print("Carro")
            
    else:
        print("Bicicleta")

else:
    resposta = input("É aquático? ")
    if resposta == "sim":
        resposta = input("Se locomove debaixo d'água? ")
        if resposta == "sim":
            print("Submarino")
        else:
            resposta = input("É de grande porte/carrega cargas e passageiros? ")
            if resposta == "sim":
                print("Navio")
            else:
                resposta = input("É de pequeno porte/usado para pesca? ")
                if resposta == "sim":
                    print("Barco")
                else:
                    print("Lancha")
    else:
        resposta = input("Tem uma hélice na parte de cima do veículo? ")
        if resposta == "sim":
            print("Helicóptero")
        else:
            reposta = input("Tem motor?")
            if resposta == "sim":
                print("Avião")
            else:
                resposta = input("É movido a ar quente? ")
                if resposta == "sim":
                    print("Balão")
                else:
                    print("Paraquedas")



































#

