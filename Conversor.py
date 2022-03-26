from tkinter import *


def bidecimal():

    def Converte():
        binario2 = binario.get()

        decimal = 0
        i = 0
        contador = 0
        tamanho = len(binario2)
        larg = tamanho

        if binario2[0] == '0':
            tamanho = len(binario2)
            larg = tamanho

            while i < tamanho and larg != 1:
                if binario2[larg - 1] == "1":
                    decimal += 2 ** contador
                elif binario2[larg - 1] == "0":
                    decimal += 0
                else:
                    print('Erro')

                contador += 1
                larg -= 1
                i += 1

            decimal = str(decimal)
            Teste1["text"] = "Esse número binario em decimal é"
            Teste2["text"] = decimal

        elif binario2[0] == '1':
            tamanho = len(binario2)
            larg = tamanho

            while i < tamanho and larg != 1:

                if binario2[larg - 1] == "1":
                    decimal += 2 ** contador
                elif binario2[larg - 1] == "0":
                    decimal += 0
                else:
                    print('Erro')

                contador += 1
                larg -= 1
                i += 1
            decimal = str(-decimal)
            Teste1["text"] = "Esse número binario em decimal é "
            Teste2["text"] = decimal

    Textotipo["text"] = 'Caso o primeiro digito for 0 será considerado positivo'
    Texttipo2["text"] = 'Caso o primeiro digito for 1 será considerado negativo'

    binario = Entry(janela, font="14")
    binario.place(x=55, y=440, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=100, y=490, width=100, height=30)


def decibi():
    def Converte():
        resultado = ""
        decimal = dados.get()
        if decimal == '-0':
            resultado = '10000000'
            Teste1["text"] = "Esse número decimal em binario é "
            Teste2["text"] = resultado
        else:
            decimal = int(decimal)
            if decimal > 0:
                while decimal >= 1:
                    num = decimal % 2
                    if num == 0:
                        resultado = "0" + resultado
                    elif num == 1:
                        resultado = "1" + resultado
                        decimal -= 1
                    decimal /= 2
                tamanho = len(resultado)

                while tamanho < 7:
                    resultado = '0' + resultado
                    tamanho += 1
                resultado = '0' + resultado
                Teste1["text"] = "Esse número decimal em binario é "
                Teste2["text"] = resultado

            elif decimal == 0:
                resultado = '00000000'
                Teste1["text"] = "Esse número decimal em binario é "
                Teste2["text"] = resultado

            else:
                while decimal <= -1:
                    num = decimal % 2

                    if num == 0:
                        resultado = "0" + resultado

                    elif num == 1:
                        resultado = "1" + resultado
                        decimal += 1

                    decimal /= 2
                tamanho = len(resultado)

                while tamanho < 7:
                    resultado = '0' + resultado
                    tamanho += 1
                resultado = '1' + resultado
                Teste1["text"] = "Esse número decimal em binario é"
                Teste2["text"] = resultado

    Textotipo["text"] = 'Informe um número decimal para ser trans- '
    Texttipo2["text"] = 'formado em binario sinal magnitude'

    dados = Entry(janela, font="14")
    dados.place(x=55, y=440, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=100, y=490, width=100, height=30)


def complementodois_Decimal():
    def Converte():
        binario2 = binario.get()
        if binario2[0] == '0':
            decimal = 0
            contador = 0
            i = 0
            tamanho = len(binario2)
            larg = tamanho

            while i < tamanho:
                if binario2[larg - 1] == "1":
                    decimal += 2 ** contador
                elif binario2[larg - 1] == "0":
                    decimal += 0
                else:
                    print('Erro')

                contador += 1
                larg -= 1
                i += 1

            Teste1["text"] = "Esse número binario em decimal é "
            Teste2["text"] = decimal

        elif binario2[0] == '1':
            decimal = 0
            contador = 0
            i = 0
            tamanho = len(binario2)
            larg = tamanho

            while i < tamanho and larg != 1:

                if binario2[larg - 1] == "1":
                    decimal += 2 ** contador
                elif binario2[larg - 1] == "0":
                    decimal += 0
                else:
                    print('Erro')

                contador += 1
                larg -= 1
                i += 1
            decimal = -(2 ** (tamanho - 1)) + decimal

            Teste1["text"] = "Esse número binario em decimal é "
            Teste2["text"] = decimal

    Textotipo["text"] = 'Caso o primeiro digito for 0 será considerado positivo'
    Texttipo2["text"] = 'Caso o primeiro digito for 1 será considerado negativo'

    binario = Entry(janela, font="14")
    binario.place(x=55, y=440, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=100, y=490, width=100, height=30)


def decimal_ComplementoDois():
    def Converte():

        decimal = dados.get()
        decimal = int(decimal)

        if decimal > 0:
            resultado = ""
            while decimal >= 1:
                num = decimal % 2
                if num == 0:
                    resultado = "0" + resultado
                elif num == 1:
                    resultado = "1" + resultado
                    decimal -= 1
                decimal /= 2

            tamanho = len(resultado)
            if tamanho < 8:
                while tamanho < 8:
                    resultado = '0' + resultado
                    tamanho += 1
            elif tamanho > 8:
                resultado = '0' + resultado

            Teste1["text"] = "Esse número decimal em binario é"
            Teste2["text"] = resultado

        elif decimal == 0:
            resultado = '00000000'

            Teste1["text"] = "Esse número decimal em binario é"
            Teste2["text"] = resultado

        else:
            i = 0
            contador = 0
            resultado = ""
            while decimal <= -1:
                num = decimal % 2

                if num == 0:
                    resultado = "0" + resultado

                elif num == 1:
                    resultado = "1" + resultado
                    decimal += 1
                decimal /= 2
            tamanho = len(resultado)

            while tamanho < 8:
                resultado = '0' + resultado
                tamanho += 1

            tamanho = len(resultado)
            nume = list(resultado)

            while i < tamanho:
                if resultado[i] == '1':
                    nume[i] = '0'

                elif resultado[i] == '0':
                    nume[i] = '1'

                i += 1

            resultado = "".join(nume)
            tamanho = len(resultado)
            larg = tamanho
            i = 0

            while i < tamanho:
                if resultado[larg - 1] == "1":
                    decimal += 2 ** contador

                elif resultado[larg - 1] == "0":
                    decimal += 0

                else:
                    print('Erro')

                contador += 1
                larg -= 1
                i += 1
            decimal += 1
            resultado1 = ""
            while decimal >= 1:
                num = decimal % 2
                if num == 0:
                    resultado1 = "0" + resultado1
                elif num == 1:
                    resultado1 = "1" + resultado1
                    decimal -= 1
                decimal /= 2

            Teste1["text"] = "Esse número decimal em binario é"
            Teste2["text"] = resultado1

    Textotipo["text"] = 'Informe um número decimal para ser trans- '
    Texttipo2["text"] = 'formado em binario complemento de dois'

    dados = Entry(janela, font="14")
    dados.place(x=55, y=440, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=100, y=490, width=100, height=30)


def complementoum_Decimal():
    def Converte():
        decimal = 0
        contador = 0
        i = 0
        binario2 = binario.get()
        tamanho = len(binario2)
        larg = tamanho

        if binario2[0] == '0':
            tamanho = len(binario2)
            larg = tamanho

            while i < tamanho:
                if binario2[larg - 1] == "1":
                    decimal += 2 ** contador
                elif binario2[larg - 1] == "0":
                    decimal += 0
                else:
                    print('Erro')

                contador += 1
                larg -= 1
                i += 1

            Teste1["text"] = "Esse número binario em decimal é "
            Teste2["text"] = decimal

        elif binario2[0] == '1':
            tamanho = len(binario2)
            larg = tamanho
            teste = list(binario2)
            while i < tamanho:

                if binario2[i] == "1":
                    teste[i] = "0"

                elif binario2[i] == "0":
                    teste[i] = "1"

                else:
                    print('Erro')

                i += 1

            binario2 = "".join(teste)
            i = 0
            tamanho = len(binario2)
            larg = tamanho

            while i < tamanho:

                if binario2[larg - 1] == "1":
                    decimal += 2 ** contador

                elif binario2[larg - 1] == "0":
                    decimal += 0

                else:
                    print('Erro')

                contador += 1
                larg -= 1
                i += 1

            decimal = str(-decimal)
            Teste1["text"] = "Esse número binario em decimal é "
            Teste2["text"] = decimal

    Textotipo["text"] = 'Caso o primeiro digito for 0 será considerado positivo'
    Texttipo2["text"] = 'Caso o primeiro digito for 1 será considerado negativo'

    binario = Entry(janela, font="14")
    binario.place(x=55, y=440, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=100, y=490, width=100, height=30)


def decimal_ComplementoUm():
    def Converte():
        i = 0
        decimal = dados.get()
        if decimal == '-0':
            resultado = "11111111"
            Teste1["text"] = "Esse número decimal em binario é"
            Teste2["text"] = resultado
        else:
            decimal = int(decimal)

            if decimal > 0:
                resultado = ""
                while decimal >= 1:
                    num = decimal % 2
                    if num == 0:
                        resultado = "0" + resultado
                    elif num == 1:
                        resultado = "1" + resultado
                        decimal -= 1
                    decimal /= 2
                tamanho = len(resultado)
                while tamanho < 8:
                    resultado = "0" + resultado
                    tamanho += 1

                Teste1["text"] = "Esse número decimal em binario é"
                Teste2["text"] = resultado

            elif decimal == 0:
                resultado = '00000000'
                Teste1["text"] = "Esse número decimal em binario é"
                Teste2["text"] = resultado

            else:
                resultado = ""
                while decimal <= -1:
                    num = decimal % 2

                    if num == 0:
                        resultado = "0" + resultado
                    elif num == 1:
                        resultado = "1" + resultado
                        decimal += 1
                    decimal /= 2
                tamanho = len(resultado)
                while tamanho < 8:
                    resultado = '0' + resultado
                    tamanho += 1
                tamanho = len(resultado)
                nume = list(resultado)
                while i < tamanho:
                    if resultado[i] == '1':
                        nume[i] = '0'
                    elif resultado[i] == '0':
                        nume[i] = '1'
                    i += 1
                resultado = "".join(nume)

                Teste1["text"] = "Esse número decimal em binario é"
                Teste2["text"] = resultado

    Textotipo["text"] = 'Informe um número decimal para ser trans- '
    Texttipo2["text"] = 'formado em binario complemento de dois'

    dados = Entry(janela, font="14")
    dados.place(x=55, y=440, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=100, y=490, width=100, height=30)

# Binarios #
#......................................................................................................................................#


def octal_Decimal():
    def Converte():
        decimal = 0
        contador = 0
        i = 0
        octal2 = octal.get()
        tamanho = len(octal2)
        larg = tamanho

        while i < tamanho:
            if octal2[larg - 1] == '0':
                decimal += 0 * (8 ** contador)

            elif octal2[larg - 1] == '1':
                decimal += 1 * (8 ** contador)

            elif octal2[larg - 1] == '2':
                decimal += 2 * (8 ** contador)

            elif octal2[larg - 1] == '3':
                decimal += 3 * (8 ** contador)

            elif octal2[larg - 1] == '4':
                decimal += 4 * (8 ** contador)

            elif octal2[larg - 1] == '5':
                decimal += 5 * (8 ** contador)

            elif octal2[larg - 1] == '6':
                decimal += 6 * (8 ** contador)

            elif octal2[larg - 1] == '7':
                decimal += 7 * (8 ** contador)

            elif octal2[larg - 1] == '8':
                decimal += 8 * (8 ** contador)

            elif octal2[larg - 1] == '9':
                decimal += 9 * (8 ** contador)

            larg -= 1
            contador += 1
            i += 1

        Teste3["text"] = "Esse número octal em decimal é"
        Teste4["text"] = decimal

    Textotipo3["text"] = 'Informe um número Octal para ser'
    Texttipo4["text"] = 'convertido em decimal'

    octal = Entry(janela, font="14")
    octal.place(x=455, y=370, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=500, y=420, width=100, height=30)


def decimal_Octal():
    def Converte():
        resultado = ""
        decimal = dados.get()
        decimal = int(decimal)

        while decimal >= 1:
            num = int(decimal % 8)
            texto = str(num)

            resultado = texto + resultado
            if num != 0:
                decimal -= num
            decimal /= 8

        Teste3["text"] = "Esse número decimal em octal é"
        Teste4["text"] = resultado

    Textotipo3["text"] = 'Informe um número decimal para'
    Texttipo4["text"] = 'ser transformado em octal'

    dados = Entry(janela, font="14")
    dados.place(x=455, y=370, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=500, y=420, width=100, height=30)

#Octais#
#.......................................................................................................................................#


def hexa_Decimal():
    def Converte():
        decimal = 0
        i = 0
        contador = 0
        hexa = hexadecimal.get()
        tamanho = len(hexa)
        larg = tamanho

        while i < tamanho:
            if hexa[larg - 1] == '0':
                decimal += 0 * (16 ** contador)

            elif hexa[larg - 1] == '1':
                decimal += 1 * (16 ** contador)

            elif hexa[larg - 1] == '2':
                decimal += 2 * (16 ** contador)

            elif hexa[larg - 1] == '3':
                decimal += 3 * (16 ** contador)

            elif hexa[larg - 1] == '4':
                decimal += 4 * (16 ** contador)

            elif hexa[larg - 1] == '5':
                decimal += 5 * (16 ** contador)

            elif hexa[larg - 1] == '6':
                decimal += 6 * (16 ** contador)

            elif hexa[larg - 1] == '7':
                decimal += 7 * (16 ** contador)

            elif hexa[larg - 1] == '8':
                decimal += 8 * (16 ** contador)

            elif hexa[larg - 1] == '9':
                decimal += 9 * (16 ** contador)

            elif hexa[larg - 1] == 'A':
                decimal += 10 * (16 ** contador)

            elif hexa[larg - 1] == 'B':
                decimal += 11 * (16 ** contador)

            elif hexa[larg - 1] == 'C':
                decimal += 12 * (16 ** contador)

            elif hexa[larg - 1] == 'D':
                decimal += 13 * (16 ** contador)

            elif hexa[larg - 1] == 'E':
                decimal += 14 * (16 ** contador)

            elif hexa[larg - 1] == 'F':
                decimal += 15 * (16 ** contador)

            larg -= 1
            contador += 1
            i += 1

        Teste5["text"] = "Esse número hexadecimal em decimal é"
        Teste6["text"] = decimal

    Textotipo5["text"] = 'Informe um número Hexadecimal para ser'
    Texttipo6["text"] = 'convertido em decimal'

    hexadecimal = Entry(janela, font="14")
    hexadecimal.place(x=855, y=370, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=900, y=420, width=100, height=30)


def decimal_Hexa():
    def Converte():
        decimal = dados.get()
        decimal = int(decimal)
        resultado = ""
        while decimal >= 1:
            num = int(decimal % 16)
            texto = str(num)

            if num == 15:
                resultado = 'F' + resultado
            elif num == 14:
                resultado = 'E' + resultado
            elif num == 13:
                resultado = 'D' + resultado
            elif num == 12:
                resultado = 'C' + resultado
            elif num == 11:
                resultado = 'B' + resultado
            elif num == 10:
                resultado = 'A' + resultado
            else:
                resultado = texto + resultado

            if num != 0:
                decimal -= num

            decimal /= 16

        Teste5["text"] = "Esse número decimal em hexadecimal é"
        Teste6["text"] = resultado

    Textotipo5["text"] = 'Informe um número decimal para'
    Texttipo6["text"] = 'ser transformado em hexadecimal'

    dados = Entry(janela, font="14")
    dados.place(x=855, y=370, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=900, y=420, width=100, height=30)

#Hexadecimais#
#......................................................................................................................................#


def octal_Binario():
    def Converte():
        i = 0
        contador = 0
        resultado = ""
        octa = dados.get()
        tamanho = len(octa)
        larg = tamanho

        while i < tamanho:
            if octa[larg - 1] == '0':
                resultado = '000' + resultado

            elif octa[larg - 1] == '1':
                resultado = '001' + resultado

            elif octa[larg - 1] == '2':
                resultado = '010' + resultado

            elif octa[larg - 1] == '3':
                resultado = '011' + resultado

            elif octa[larg - 1] == '4':
                resultado = '100' + resultado

            elif octa[larg - 1] == '5':
                resultado = '101' + resultado

            elif octa[larg - 1] == '6':
                resultado = '110' + resultado

            elif octa[larg - 1] == '7':
                resultado = '111' + resultado

            larg -= 1
            contador += 1
            i += 1

        print(resultado)
        Teste7["text"] = "Esse número octal"
        Teste8["text"] = "em binario é"
        Teste9["text"] = resultado

    Textotipo7["text"] = 'Informe um número octal para'
    Texttipo8["text"] = 'ser transformado em binario'

    dados = Entry(janela, font="14")
    dados.place(x=1255, y=400, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=1300, y=450, width=100, height=30)


def binario_Octal():
    def Converte():
        dados2 = dados.get()
        tamanho = len(dados2)
        i = 1
        c = 0

        largura = tamanho % 3
        ture = largura
        vale = tamanho - ture
        testar = vale / 3

        resposta = ""

        if tamanho == 1:
            if dados2 == '0':
                resposta = "0"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == '1':
                resposta = "1"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

        elif tamanho == 2:
            if dados2 == '00':
                resposta = "0"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == '01':
                resposta = "1"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == "10":
                resposta = "2"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == "11":
                resposta = "3"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

        elif testar >= 1:

            resposta1 = ""
            if ture == 1:
                binario = dados2[0]

                if binario == '0':
                    resposta1 = "0"

                elif binario == '1':
                    resposta1 = "1"

            elif ture == 2:
                binario = dados2[0] + dados2[1]

                if binario == '00':
                    resposta1 = "0"

                elif binario == '01':
                    resposta1 = "1"

                elif binario == "10":
                    resposta1 = "2"

                elif binario == "11":
                    resposta1 = "3"

            while i <= testar:
                teste1 = tamanho - (3 + c)
                teste2 = tamanho - (2 + c)
                teste3 = tamanho - (1 + c)
                binario = ""

                binario = dados2[teste1] + dados2[teste2] + dados2[teste3]

                if binario == '000':
                    resposta = "0" + resposta
                elif binario == '001':
                    resposta = "1" + resposta
                elif binario == '010':
                    resposta = "2" + resposta
                elif binario == '011':
                    resposta = "3" + resposta
                elif binario == '100':
                    resposta = "4" + resposta
                elif binario == '101':
                    resposta = "5" + resposta
                elif binario == '110':
                    resposta = "6" + resposta
                elif binario == '111':
                    resposta = "7" + resposta

                i += 1
                c += 3

            resposta = resposta1 + resposta
            print(resposta)
            Teste7["text"] = "Esse número binario"
            Teste8["text"] = "em octal é"
            Teste9["text"] = resposta

    Textotipo7["text"] = 'Informe um número binario para'
    Texttipo8["text"] = 'ser transformado em octal'

    dados = Entry(janela, font="14")
    dados.place(x=1255, y=400, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=1300, y=450, width=100, height=30)
# Binario/Octal #
#....................................................................................................................................#


def binario_Hexa():
    def Converte():
        dados2 = dados.get()
        tamanho = len(dados2)
        i = 1
        c = 0

        largura = tamanho % 4
        ture = largura
        vale = tamanho - ture
        testar = vale / 4

        resposta = ""
        resposta1 = ""
        binario = ""

        if tamanho == 1:
            if dados2 == '0':
                resposta = "0"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == '1':
                resposta = "1"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

        elif tamanho == 2:
            if dados2 == '00':
                resposta = "0"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == '01':
                resposta = "1"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == "10":
                resposta = "2"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == "11":
                resposta = "3"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta
        elif tamanho == 3:
            if dados2 == '000':
                resposta = "0"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == '001':
                resposta = "1"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == "010":
                resposta = "2"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == "011":
                resposta = "3"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta
            elif dados2 == "100":
                resposta = "4"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == "101":
                resposta = "5"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == "110":
                resposta = "6"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

            elif dados2 == "111":
                resposta = "7"

                Teste7["text"] = "Esse número binario em octal é"
                Teste8["text"] = resposta

        elif testar >= 1:
            binario = ""
            resposta1 = ""
            if ture == 1:
                binario = dados2[0]

                if binario == '0':
                    resposta1 = "0"

                elif binario == '1':
                    resposta1 = "1"

            elif ture == 2:
                binario = ""
                binario = dados2[0] + dados2[1]

                if binario == '00':
                    resposta1 = "0"

                elif binario == '01':
                    resposta1 = "1"

                elif binario == "10":
                    resposta1 = "2"

                elif binario == "11":
                    resposta1 = "3"

            elif ture == 3:
                binario = dados2[0] + dados2[1] + dados2[2]

                if binario == '000':
                    resposta1 = "0"

                elif binario == '001':
                    resposta1 = "1"

                elif binario == "010":
                    resposta1 = "2"

                elif binario == "011":
                    resposta1 = "3"

                elif binario == "100":
                    resposta1 = "4"

                elif binario == "101":
                    resposta1 = "5"

                elif binario == "101":
                    resposta1 = "6"

                elif binario == "111":
                    resposta1 = "7"

            while i <= testar:
                teste1 = tamanho - (4 + c)
                teste2 = tamanho - (3 + c)
                teste3 = tamanho - (2 + c)
                teste4 = tamanho - (1 + c)
                binario = ""

                binario = dados2[teste1] + dados2[teste2] + \
                    dados2[teste3] + dados2[teste4]

                if binario == '0000':
                    resposta = "0" + resposta
                elif binario == '0001':
                    resposta = "1" + resposta
                elif binario == '0010':
                    resposta = "2" + resposta
                elif binario == '0011':
                    resposta = "3" + resposta
                elif binario == '0100':
                    resposta = "4" + resposta
                elif binario == '0101':
                    resposta = "5" + resposta
                elif binario == '0110':
                    resposta = "6" + resposta
                elif binario == '0111':
                    resposta = "7" + resposta
                elif binario == '1000':
                    resposta = "8" + resposta
                elif binario == '1001':
                    resposta = "9" + resposta
                elif binario == '1010':
                    resposta = "A" + resposta
                elif binario == '1011':
                    resposta = "B" + resposta
                elif binario == '1100':
                    resposta = "C" + resposta
                elif binario == '1101':
                    resposta = "D" + resposta
                elif binario == '1110':
                    resposta = "E" + resposta
                elif binario == '1111':
                    resposta = "F" + resposta

                i += 1
                c += 4

            resposta = resposta1 + resposta

            Teste7["text"] = "Esse número binario"
            Teste8["text"] = "em hexadecimal é"
            Teste9["text"] = resposta

    Textotipo7["text"] = 'Informe um número binario para'
    Texttipo8["text"] = 'ser transformado em hexadecimal'

    dados = Entry(janela, font="14")
    dados.place(x=1255, y=400, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=1300, y=450, width=100, height=30)


def hexa_binario():
    def Converte():
        i = 0
        contador = 0
        resultado = ""
        hexa = dados.get()
        tamanho = len(hexa)
        larg = tamanho

        while i < tamanho:
            if hexa[larg - 1] == '0':
                resultado = '0000' + resultado

            elif hexa[larg - 1] == '1':
                resultado = '0001' + resultado

            elif hexa[larg - 1] == '2':
                resultado = '0010' + resultado

            elif hexa[larg - 1] == '3':
                resultado = '0011' + resultado

            elif hexa[larg - 1] == '4':
                resultado = '0100' + resultado

            elif hexa[larg - 1] == '5':
                resultado = '0101' + resultado

            elif hexa[larg - 1] == '6':
                resultado = '0110' + resultado

            elif hexa[larg - 1] == '7':
                resultado = '0111' + resultado

            elif hexa[larg - 1] == '8':
                resultado = '1000' + resultado

            elif hexa[larg - 1] == '9':
                resultado = '1001' + resultado

            elif hexa[larg - 1] == 'A':
                resultado = '1010' + resultado

            elif hexa[larg - 1] == 'B':
                resultado = '1011' + resultado

            elif hexa[larg - 1] == 'C':
                resultado = '1100' + resultado

            elif hexa[larg - 1] == 'D':
                resultado = '1101' + resultado

            elif hexa[larg - 1] == 'E':
                resultado = '1110' + resultado

            elif hexa[larg - 1] == 'F':
                resultado = '1111' + resultado

            larg -= 1
            contador += 1
            i += 1

        print(resultado)
        Teste7["text"] = "Esse número hexadecimal"
        Teste8["text"] = "em binario é"
        Teste9["text"] = resultado

    Textotipo7["text"] = 'Informe um número hexadecimal para'
    Texttipo8["text"] = 'ser transformado em binario'

    dados = Entry(janela, font="14")
    dados.place(x=1255, y=400, width=200, height=35)

    converter = Button(janela, text="Converter",
                       command=lambda: Converte(), font="14")
    converter.place(x=1300, y=450, width=100, height=30)
# Binario/Hexadecimal#
#......................................................................................................................................#


def Escolha():
    def Escolhas2(i):
        def mudar():
            Escolha1["background"] = "#77DD77"
            Escolha2["background"] = "#fff"

        def mudar2():
            Escolha1["background"] = "#fff"
            Escolha2["background"] = "#77DD77"

        if i == 1:
            teste = decibi
            teste2 = bidecimal
            magnitude["background"] = "#77DD77"
            complementodedois["background"] = "#fff"
            complementodeum["background"] = "#fff"

        elif i == 2:
            teste = decimal_ComplementoDois
            teste2 = complementodois_Decimal
            magnitude["background"] = "#fff"
            complementodedois["background"] = "#77DD77"
            complementodeum["background"] = "#fff"

        elif i == 3:
            teste = decimal_ComplementoUm
            teste2 = complementoum_Decimal
            magnitude["background"] = "#fff"
            complementodedois["background"] = "#fff"
            complementodeum["background"] = "#77DD77"

        Escolha1 = Button(janela, text="Decimal/Binario", font="12",
                          command=lambda: [teste(), mudar()], background="#fff")
        Escolha1.place(x=10, y=350, width=150, height=20)
        Escolha2 = Button(janela, text="Binario/Decimal", font="12",
                          command=lambda: [teste2(), mudar2()], background="#fff")
        Escolha2.place(x=160, y=350, width=150, height=20)

    binario["background"] = "#77DD77"
    magnitude = Button(janela, text="Sinal M", font="12",
                       command=lambda: Escolhas2(1), background="#fff")
    magnitude.place(x=10, y=290, width=150, height=20)

    complementodedois = Button(janela, text="Compl de 2", font="12",
                               command=lambda: Escolhas2(2), background="#fff")
    complementodedois.place(x=160, y=290, width=160, height=20)

    complementodeum = Button(janela, text="Comple de 1", font="12",
                             command=lambda: Escolhas2(3), background="#fff")
    complementodeum.place(x=80, y=315, width=150, height=20)


def EscolhasOctal():
    def mudar():
        Escolha1["background"] = "#77DD77"
        Escolha2["background"] = "#fff"

    def mudar2():
        Escolha1["background"] = "#fff"
        Escolha2["background"] = "#77DD77"

    octal["background"] = "#77DD77"
    teste = decimal_Octal
    teste2 = octal_Decimal

    Escolha1 = Button(janela, text="Dec/Oct", font="12",
                      command=lambda: [teste(), mudar()], background="#fff")
    Escolha1.place(x=410, y=290, width=150, height=20)
    Escolha2 = Button(janela, text="Oct/Dec", font="12",
                      command=lambda: [teste2(), mudar2()], background="#fff")
    Escolha2.place(x=560, y=290, width=150, height=20)


def EscolhasHexadecimal():
    def mudar():
        Escolha1["background"] = "#77DD77"
        Escolha2["background"] = "#fff"

    def mudar2():
        Escolha1["background"] = "#fff"
        Escolha2["background"] = "#77DD77"

    hexadecimal["background"] = "#77DD77"
    teste = decimal_Hexa
    teste2 = hexa_Decimal

    Escolha1 = Button(janela, text="Dec/Hexa", font="12",
                      command=lambda: [teste(), mudar()], background="#fff")
    Escolha1.place(x=795, y=290, width=180, height=20)
    Escolha2 = Button(janela, text="Hexa/Dec", font="12",
                      command=lambda: [teste2(), mudar2()], background="#fff")
    Escolha2.place(x=965, y=290, width=180, height=20)


def Transforme():
    def mudar():
        Escolha1["background"] = "#77DD77"
        Escolha2["background"] = "#fff"
        Escolha3["background"] = "#fff"
        Escolha4["background"] = "#fff"

    def mudar2():
        Escolha1["background"] = "#fff"
        Escolha2["background"] = "#77DD77"
        Escolha3["background"] = "#fff"
        Escolha4["background"] = "#fff"

    def mudar3():
        Escolha1["background"] = "#fff"
        Escolha2["background"] = "#fff"
        Escolha3["background"] = "#77DD77"
        Escolha4["background"] = "#fff"

    def mudar4():
        Escolha1["background"] = "#fff"
        Escolha2["background"] = "#fff"
        Escolha3["background"] = "#fff"
        Escolha4["background"] = "#77DD77"

    binaOctal["background"] = "#77DD77"
    teste = binario_Octal
    teste2 = octal_Binario
    teste3 = binario_Hexa
    teste4 = hexa_binario

    Escolha1 = Button(janela, text="Bin/Oct", font="12",
                      command=lambda: [teste(), mudar()], background="#fff")
    Escolha1.place(x=1210, y=290, width=150, height=20)
    Escolha2 = Button(janela, text="Oct/Bin", font="12",
                      command=lambda: [teste2(), mudar2()], background="#fff")
    Escolha2.place(x=1360, y=290, width=150, height=20)

    Escolha3 = Button(janela, text="Bin/Hexa", font="12",
                      command=lambda: [teste3(), mudar3()], background="#fff")
    Escolha3.place(x=1200, y=315, width=160, height=20)
    Escolha4 = Button(janela, text="Hexa/Bin", font="12",
                      command=lambda: [teste4(), mudar4()], background="#fff")
    Escolha4.place(x=1360, y=315, width=160, height=20)


# Botôes de escolha #
#......................................................................................................................................#

janela = Tk()
janela.title('Conversor')
janela.state('zoomed')
janela.geometry('1600x800')
janela.call('wm', 'iconphoto', janela._w, PhotoImage(
    file='Logo.ico'))

img = PhotoImage(file="Logo.png")
Label(janela, image=img).place(x=70, y=20)
Label(janela, text="Conversor Binario", font="14",).place(
    x=30, y=220, width=250, height=40)


Label(janela, text="Conversor Octal", font="14",).place(
    x=430, y=220, width=250, height=40)
Label(janela, image=img).place(x=470, y=20)

Label(janela, text="Conversor Hexadecimal", font="14",).place(
    x=830, y=220, width=250, height=40)
Label(janela, image=img).place(x=870, y=20)

Label(janela, text="Transformador", font="14",).place(
    x=1230, y=220, width=250, height=40)
Label(janela, image=img).place(x=1270, y=20)

binario = Button(janela, text="Binario", font="12",
                 command=lambda: Escolha(), background="#fff")
binario.place(x=75, y=260, width=150, height=20)


octal = Button(janela, text="Octal", font="12",
               command=lambda: EscolhasOctal(), background="#fff")
octal.place(x=475, y=260, width=150, height=20)

hexadecimal = Button(janela, text="Hexadecimal", font="12",
                     command=lambda: EscolhasHexadecimal(), background="#fff")
hexadecimal.place(x=875, y=260, width=150, height=20)

binaOctal = Button(janela, text="Opções", font="12",
                   command=lambda: Transforme(), background="#fff")
binaOctal.place(x=1275, y=260, width=150, height=20)

Textotipo = Label(janela, text='', anchor=W, font="12")
Texttipo2 = Label(janela, text='', anchor=W, font="12")
Textotipo3 = Label(janela, text='', anchor=W, font="12")
Texttipo4 = Label(janela, text='', anchor=W, font="12")
Textotipo5 = Label(janela, text='', anchor=W, font="12")
Texttipo6 = Label(janela, text='', anchor=W, font="12")
Textotipo7 = Label(janela, text='', anchor=W, font="12")
Texttipo8 = Label(janela, text='', anchor=W, font="12")

Textotipo.place(x=0, y=380, width=420, height=20)
Texttipo2.place(x=0, y=400, width=400, height=20)
Textotipo3.place(x=410, y=320, width=400, height=20)
Texttipo4.place(x=410, y=340, width=400, height=20)
Textotipo5.place(x=810, y=320, width=400, height=20)
Texttipo6.place(x=810, y=340, width=400, height=20)
Textotipo7.place(x=1210, y=350, width=400, height=20)
Texttipo8.place(x=1210, y=370, width=400, height=20)

Teste1 = Label(text="", font="12", anchor=W)
Teste1.place(x=10, y=520, width=400, height=20, )

Teste2 = Label(text="", font="12", anchor=W)
Teste2.place(x=10, y=550, width=400, height=20, )

Teste3 = Label(text="", font="12", anchor=W)
Teste3.place(x=410, y=470, width=400, height=20, )

Teste4 = Label(text="", font="12", anchor=W)
Teste4.place(x=410, y=500, width=400, height=20, )

Teste5 = Label(text="", font="12", anchor=W)
Teste5.place(x=810, y=470, width=400, height=20, )

Teste6 = Label(text="", font="12", anchor=W)
Teste6.place(x=810, y=500, width=400, height=20, )

Teste7 = Label(text="", font="12", anchor=W)
Teste7.place(x=1210, y=490, width=400, height=20, )

Teste8 = Label(text="", font="12", anchor=W)
Teste8.place(x=1210, y=520, width=400, height=20, )

Teste9 = Label(text="", font="12", anchor=W)
Teste9.place(x=1210, y=550, width=400, height=20, )
janela.mainloop()

#Principal#
#.......................................................................................................................................#
