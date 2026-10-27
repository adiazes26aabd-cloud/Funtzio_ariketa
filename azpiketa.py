def azpikate_luzeena(testua):

    luzera = len(testua)
    luzeena = 0
    ikusitako_karaktereak = set()  
    ezkerra = 0  

    for eskuina in range(luzera):  
        
        while testua[eskuina] in ikusitako_karaktereak:
            ikusitako_karaktereak.remove(testua[ezkerra])
            ezkerra += 1

     
        ikusitako_karaktereak.add(testua[eskuina])

      
        luzeena = max(luzeena, eskuina - ezkerra + 1)

    return luzeena


testua = "abcabcbbasdfgbergwefevhsjbgf"
print(azpikate_luzeena(testua))  