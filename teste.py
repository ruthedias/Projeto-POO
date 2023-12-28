'''
if __name__=="__main__":
    cidade = Cidade("Pau dos Ferros","Rio Grande do Norte","59999-000")
    local1= Local(cidade,"Escola Estadual Francisco Soares da Costa","ZONA-A","001")
    local2= Local(cidade,"Escola Estadual Fernando de Melo","ZONA-B","002")

    urna1= UrnaEletronica(local1)
    urna2= UrnaEletronica(local2)

    eleitor1= Eleitor("Augusto Rocha","222987383838", local1)
    eleitor2= Eleitor("Ruth Ellen","383293838024", local2)
    eleitor3= Eleitor("Rangel Alvez","029382020839", local1)
    eleitor4= Eleitor("Emilly Garcia","493832838323", local2)
    eleitor5= Eleitor("Lizandro Almeida","889382382398", local1)
    eleitor6= Eleitor("Rogerio Aquino","298338923843", local2)
    eleitor7= Eleitor("Enzo Gabriel","129349240311", local1)
    eleitor8= Eleitor("Gabriella Dantas","393904024932", local2)
    eleitor9= Eleitor("Luiz Guilherme","100399433289", local1)
    eleitor10= Eleitor("Gabriel Sampaio","920208392403", local2)
    eleitor11= Eleitor("Maria das Graças","392820348324", local1)
    eleitor12= Eleitor("Lucas Gabriel","028982298220", local2)
    eleitor13= Eleitor("Ruan Alves","830299239393", local1)
    eleitor14= Eleitor("Marcos Aquino","832829389438", local2)
    eleitor15= Eleitor("Douglas Luiz","394294938239", local1)

    vereador_pt1 = Vereador("Marcos Leonardo", "839999103923", local1, "PT" , "321")
    vereador_pt2 = Vereador("Vanessa Lemos", "224689044002", local2, "PT","111")
    vereador_mdb1 = Vereador("Kaio Santana", "839399203923", local1, "MDB", "123")
    vereador_mdb2 = Vereador("Larissa Emanuela", "293029384002", local2, "MDB","404")

    candidatoPrefeito1 = Prefeito("Joelma", "624097234657", local2, "MDB","13")
    candidatoPrefeito2 = Prefeito("Frederico", "293789157864", local1, "PT","15")


    gerenciador= GerenciadorEleitoral()

    eleitores=[]

    eleitores.append(eleitor1)
    eleitores.append(eleitor2)
    eleitores.append(eleitor3)
    eleitores.append(eleitor4)
    eleitores.append(eleitor5)
    eleitores.append(eleitor6)
    eleitores.append(eleitor7)
    eleitores.append(eleitor8)
    eleitores.append(eleitor9)
    eleitores.append(eleitor10)
    eleitores.append(eleitor11)
    eleitores.append(eleitor12)
    eleitores.append(eleitor13)
    eleitores.append(eleitor14)
    eleitores.append(eleitor15)

    gerenciador.adicionarEleitor(eleitor1)
    gerenciador.adicionarEleitor(eleitor2)
    gerenciador.adicionarEleitor(eleitor3)
    gerenciador.adicionarEleitor(eleitor4)
    gerenciador.adicionarEleitor(eleitor5)
    gerenciador.adicionarEleitor(eleitor6)
    gerenciador.adicionarEleitor(eleitor7)
    gerenciador.adicionarEleitor(eleitor8)
    gerenciador.adicionarEleitor(eleitor9)
    gerenciador.adicionarEleitor(eleitor10)
    gerenciador.adicionarEleitor(eleitor11)
    gerenciador.adicionarEleitor(eleitor12)
    gerenciador.adicionarEleitor(eleitor13)
    gerenciador.adicionarEleitor(eleitor14)
    gerenciador.adicionarEleitor(eleitor15)

    gerenciador.adicionarEleitor(vereador_mdb1)
    gerenciador.adicionarEleitor(vereador_mdb2)
    gerenciador.adicionarEleitor(vereador_pt1)
    gerenciador.adicionarEleitor(vereador_pt2)

    gerenciador.adicionarEleitor(candidatoPrefeito1)
    gerenciador.adicionarEleitor(candidatoPrefeito2)


    gerenciador.adicionarVereador(vereador_pt1)
    gerenciador.adicionarVereador(vereador_pt2)
    gerenciador.adicionarVereador(vereador_mdb1)
    gerenciador.adicionarVereador(vereador_mdb2)

    gerenciador.adicionarPrefeito(candidatoPrefeito1)
    gerenciador.adicionarPrefeito(candidatoPrefeito2)

    gerenciador.adicionarUrnas(urna1)
    gerenciador.adicionarUrnas(urna2)

    gerenciador.adicionandoEleitorCsv()
    gerenciador.adicionandoPrefeitosCsv()
    gerenciador.adicionandoVereadoresCsv()
    gerenciador.adicionarUrnaCsv()
'''