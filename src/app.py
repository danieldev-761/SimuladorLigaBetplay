import time, random


def SimularFPC():

    
    
    equipos= [{"id": 0,"nombre": "Junior FC",}, {"id": 1,"nombre": "América de Cali",}, {"id": 2,"nombre": "Alianza FC",}, {"id": 3,"nombre": "Atlético Nacional",},
              {"id": 4,"nombre": "Boyacá Chico",}, {"id": 5,"nombre": "Bucaramanga",}, {"id": 6,"nombre": "Cúcuta Deportivo",}, {"id": 7,"nombre": "Deportes Tolima",},              
              {"id": 8,"nombre": "Deportivo Cali",}, {"id": 9,"nombre": "Deportivo Pasto",}, {"id": 10,"nombre": "Deportivo Pereira",}, {"id": 11,"nombre": "Fortaleza CEIF",},
              {"id": 12,"nombre": " Independiente Medellín",}, {"id": 13,"nombre": "Independiente Santa Fe",}, {"id": 14,"nombre": "Internacional de Bogotá",}, {"id": 15,"nombre": "Jaguares de Córdoba",},
              {"id": 16,"nombre": "Llaneros FC",}, {"id": 17,"nombre": "Millonarios FC",}, {"id": 18,"nombre": "Once Caldas",}, {"id": 19,"nombre": "Águilas Doradas",}]
    
   
    partidos_junior= []
    partidos_otros= []

    id_equipo_= 0
    id_partido= 0

    partidos_ganados_junior= 0
    partidos_perdidos_junior= 0
    partidos_empatados_junior= 0
    goles_a_favor_junior_total= 0
    goles_en_contra_junior_total= 0



    while True:
        print("""

        |--------------- MENÚ SIMULACIÓN LIGA BETPLAY ---------------|
        | 1. SIMULAR PARTIDOS FPC
        | 2. SALIR
        """)

        opcion= int(input("Ingrese una opción del menú (1, 2): "))

        try:
        
            match opcion:

                case 1:
                    print("""

                    |--------------- SIMULACIÓN DE PARTIDOS FPC ---------------|
                    | REGLAS DE SIMULACIÓN:
                    | 1. Ingresar resultados del Junior FC(PG, PP, GAFPP, GECPP).
                    | 2. Esperar a que se termine de ejecutar la simulación.
                    | 3. Mucha suerte, campeón.
                           
                    """)


                    
                    
                    i= 0
                    for i in range(len(equipos)+1):

                        
    
                         
                        
                        goles_a_favor_junior_pp= int(input("Ingrese goles a favor del partido (Junior FC): "))
                        goles_en_contra_junior_pp= int(input("Ingrese goles en contra del partido (Junior FC): "))
                        
                        



                        if goles_a_favor_junior_pp > goles_en_contra_junior_pp:
                            resultado= "Ganó"
                            partidos_ganados_junior += 1
                            
                        

                        elif goles_a_favor_junior_pp < goles_en_contra_junior_pp:
                            resultado= "Perdió"
                            partidos_perdidos_junior += 1
                            

                        else:
                            resultado= "Empató"
                            partidos_empatados_junior += 1
                            

                        
                        goles_a_favor_junior_total += goles_a_favor_junior_pp
                        goles_en_contra_junior_total += goles_en_contra_junior_pp


                        equipo_juju= {
                            "id": 0,
                            "nombre": "Junior FC",
                            "local": None,
                            "GF": goles_a_favor_junior_total,
                            "GC": goles_en_contra_junior_total,
                            "DG": 0,
                            "resultado": resultado,
                            "PG": partidos_ganados_junior,
                            "PP": partidos_perdidos_junior,
                            "PE": partidos_empatados_junior,
                            "campeón": None

                        }

                        equipo_juju["PG"] += partidos_ganados_junior
                        equipo_juju["PP"] += partidos_perdidos_junior
                        equipo_juju["PE"] += partidos_empatados_junior

                        local= random.choice([True, False])
                        if local:
                            nombre_local= "Junior FC"
                            nombre_visita= equipos[i]["nombre"]
                            junior_local= True
                        else:
                            nombre_local= equipos[i]["nombre"]
                            nombre_visita= "Junior FC"
                            junior_local= False


                        partido_junior= {
                            "id": id_partido,
                            "local": junior_local,
                            "visitante": None,
                            "gol_local_junior": goles_a_favor_junior_pp,
                            "gol_visita_junior": goles_en_contra_junior_pp,
                            "resultado": resultado
                        }

                        partidos_junior.append(partido_junior)
                        
                        equipo_juju["GF"]+= goles_a_favor_junior_total
                        equipo_juju["GC"]+= goles_en_contra_junior_total

                        equipos.append(equipo_juju)
                        
                        

                        

                        print(f"""---------- Partido N°{i} ----------
                              EQUIPO LOCAL | EQUIPO VISITANTE | 
                              {nombre_local}     | {nombre_visita}

                              Goles a Favor Junior FC: {goles_a_favor_junior_pp} | Goles en Contra {nombre_visita}: {goles_en_contra_junior_pp}
                              Resultado Junior FC: {resultado} """)


                        equipo_local= random.choice([True, False])
                        if equipo_local:
                            nombre_local_otro= equipos[i]["nombre"]
                            nombre_visita_otro= equipos[i]["nombre"]
                            
                        else:
                            nombre_local_otro= equipos[i]["nombre"]
                            nombre_visita_otro= equipos[i]["nombre"]
                            


                    
                        
                        gol_local_otro= random.randint(0,5)
                        gol_visita_otro= random.randint(0,5)


                        if gol_local_otro > gol_visita_otro:
                            resultado= "Ganó local"
                            equipos[i]["PG"] += 1

                        elif gol_local_otro < gol_visita_otro:
                            resultado= "Ganó visita"
                            equipos[i]["PP"] += 1

                        else:
                            resultado= "Empate"
                            equipos[i]["PE"] += 1


                        partido_otro = {
                            "id": id_partido,
                            "local": nombre_local_otro,
                            "visitante": nombre_visita_otro,
                            "gol_local_otro": gol_local_otro,
                            "gol_visita_otro": gol_visita_otro,
                            "resultado": resultado
                        }

                        partidos_otros.append(partido_otro)

                        
                        for equipo in len(equipos):

                            equipos_otros= {

                                "GF": 0,
                                "GC": 0,
                                "DG": 0,
                                "resultado": resultado,
                                "PG": 0,
                                "PP": 0,
                                "PE": 0,
                                "campeón": None

                            }

                            equipo[i]["equipos"].append(equipos_otros)

                    
                        i+=1
                        



                case 2:
                    print("Saliendo del programa...")
                    time.sleep(2)
                    break

                case _:
                    print("No existe esa opción. Vuelva a intentarlo")
        
        except ValueError:
            print("{error}: No coincide el tipo de dato.")

SimularFPC()