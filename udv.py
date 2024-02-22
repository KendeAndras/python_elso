lname=input('vezetekneved: ')
fname=input('keresztneved: ')

print("szia uram!",lname[0].upper()+lname[1:].lower(),fname[0].upper()+fname[1:].lower(),"vagyol")

mg=lname[0].upper()+fname[0].upper()

print(mg)

age=int(input("korod tesverem?"))

print("esku?",age+15,"? te hazudsz nekem tesverem, tisztan mondjad a szemembe ha velem beszelel")

print("igaz e hogy 18 alatt vagy devla", age<18)

if age>18:
    print("akkor te hazudol nekem testverem odavigyazza magadra")
else:
    print("jo gyerek vagy")

print(((lname+" ")*80)[:80])