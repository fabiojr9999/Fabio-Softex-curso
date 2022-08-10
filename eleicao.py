c1 = 0
c2 = 0
c3 = 0
b = 0
print("numero dos canditados 1º(889) 2º(847) 3º(515) Branco(0)")
while True:
    try:
        voto = int(input("digite o numero do candidato: "))
        if voto == 889:
                    c1 += 1
                    c = int(input("deseja continua? digite sim=(1) ou não=(2): "))
                    if c == 2:
                        print(f"A contegem de voto ficou assim \n canditado 1 teve {c1} votos \n candidato 2 teve {c2} votos \n candidato 3 teve {c3} votos \n branco teve {b} votos")
                        c1 > c2 and c1 > c3 or c1 >= b or c1 <= b
                        print("o primeiro candidato venceu!")
                        break
                    continue
        elif voto == 847:
                    c2 += 1
                    c = int(input("deseja continua? digite sim=(1) ou não=(2): "))
                    if c == 2:
                        print(f"A contegem de voto ficou assim \n canditado 1 teve {c1} votos \n candidato 2 teve {c2} votos \n candidato 3 teve {c3} votos \n branco teve {b} votos")
                        c2 > c1 and c2 > c3 
                        print("o segundo candidato venceu!")
                        break
                    continue
        elif voto == 515:
                    c3 += 1
                    c = int(input("deseja continua? digite sim=(1) ou não=(2): "))
                    if c == 2:
                        print(f"A contegem de voto ficou assim \n canditado 1 teve {c1} votos \n candidato 2 teve {c2} votos \n candidato 3 teve {c3} votos \n branco teve {b} votos")
                        c3 > c2 and c3 > c1 
                        print("o terceiro candidato venceu!")
                        break
                    continue
        elif voto == 0:
                    b += 1
                    c = int(input("deseja continua? digite sim=(1) ou não=(2): "))
                    if c == 2:
                        print(f"A Apuração dos votos ficou assim \n canditado 1 teve {c1} votos \n candidato 2 teve {c2} votos \n candidato 3 teve {c3} votos \n branco teve {b} votos")
                        if b > c1 and c1 > c2 and c1 > c3:
                            print("o primeiro candidado venceu!")
                        elif b > c1 and c2 > c1 and c2 >c3:
                            print("o segundo candidato venceu!")
                        elif b > c3 and c3 > c1 and c3 > c2:
                            print("o terceiro candidato venceu!")
                        break
                    continue
        else:
            print('erro')
    except:
        print("erro")
        c = int(input("deseja continua? digite sim=(1) ou não=(2): "))
        if c == 2:
            break
        continue