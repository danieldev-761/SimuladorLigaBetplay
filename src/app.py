import time, random


def SimularFPC():

    
    
    equipos= [{"id": 0,"nombre": "Junior FC", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 1,"nombre": "América de Cali", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 2,"nombre": "Alianza FC", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 3,"nombre": "Atlético Nacional", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0},
              {"id": 4,"nombre": "Boyacá Chico", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 5,"nombre": "Bucaramanga", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 6,"nombre": "Cúcuta Deportivo", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 7,"nombre": "Deportes Tolima", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0},              
              {"id": 8,"nombre": "Deportivo Cali", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 9,"nombre": "Deportivo Pasto", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 10,"nombre": "Deportivo Pereira", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 11,"nombre": "Fortaleza CEIF", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0},
              {"id": 12,"nombre": " Independiente Medellín", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 13,"nombre": "Independiente Santa Fe", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 14,"nombre": "Internacional de Bogotá", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 15,"nombre": "Jaguares de Córdoba", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0},
              {"id": 16,"nombre": "Llaneros FC", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 17,"nombre": "Millonarios FC", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 18,"nombre": "Once Caldas", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}, {"id": 19,"nombre": "Águilas Doradas", "PG": 0, "PP": 0, "PE": 0, "GF": 0, "GC": 0, "DG": 0}]
    
   
    partidos_junior= []
    partidos_otros= []

 
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


                    
                    
                    i= 1
                    for i in range(len(equipos)):

                        
    
                         
                        
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
                            nombre_visita= equipos[i+1]["nombre"]
                            junior_local= True
                        else:
                            nombre_local= equipos[i+1]["nombre"]
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

                            idx_local = random.randint(0, len(equipos)-1)
                            idx_visita = random.randint(0, len(equipos)-1)

                            while idx_visita == idx_local:
                                idx_visita = random.randint(0, len(equipos)-1)

                            nombre_local_otro= equipos[idx_local]["nombre"]
                            nombre_visita_otro= equipos[idx_visita]["nombre"]
                            
                        else:
                            idx_visita = random.randint(0, len(equipos)-1)
                            idx_local = random.randint(0, len(equipos)-1)


                            while idx_local == idx_visita:
                                idx_local = random.randint(0, len(equipos)-1)

                            nombre_local_otro= equipos[idx_local]["nombre"]
                            nombre_visita_otro= equipos[idx_visita]["nombre"]
                            


                    
                        
                        gol_local_otro= random.randint(0,5)
                        gol_visita_otro= random.randint(0,5)


                        if gol_local_otro > gol_visita_otro:
                            resultado= "Ganó local"
                            equipos[idx_local]["PG"] += 1
                            equipos[idx_visita]["PP"] += 1

                        elif gol_local_otro < gol_visita_otro:
                            resultado= "Ganó visita"
                            equipos[idx_visita]["PG"] += 1
                            equipos[idx_local]["PP"] += 1

                        else:
                            resultado= "Empate"
                            equipos[idx_local]["PE"] += 1
                            equipos[idx_visita]["PE"] += 1


                        partido_otro = {
                            "id": id_partido,
                            "local": nombre_local_otro,
                            "visitante": nombre_visita_otro,
                            "gol_local_otro": gol_local_otro,
                            "gol_visita_otro": gol_visita_otro,
                            "resultado": resultado
                        }

                        partidos_otros.append(partido_otro)



                    
                        i+=1



                        
                    print("Simulación de partidos finalizada. Mostrando tabla de clasificación...")
                    time.sleep(2)

                    equipos_ordenados= sorted(equipos, key=lambda x: (x["PG"], x["DG"]), reverse=True)

                    print("|----------------- TABLA DE CLASIFICACIÓN -----------------|")
                    print("| EQUIPO | PJ | PG | PP | PE | GF | GC | DG | PUNTOS |")
                    for equipo in equipos_ordenados:
                        puntos= equipo["PG"]*3 + equipo["PE"]
                        print(f"| {equipo['nombre']} | {equipo['PJ']} | {equipo['PG']} | {equipo['PP']} | {equipo['PE']} | {equipo['GF']} | {equipo['GC']} | {equipo['DG']} | {puntos} |")



                case 2:
                    print("Saliendo del programa...")
                    time.sleep(2)
                    break

                case _:
                    print("No existe esa opción. Vuelva a intentarlo")
        
        except ValueError:
            print("{error}: No coincide el tipo de dato.")

SimularFPC()



    