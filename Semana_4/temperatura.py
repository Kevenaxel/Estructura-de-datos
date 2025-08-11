# La siguiente lista contiene las temperatura maximas registradas en tu ciudad durante una semana:

Temperatura = [30, 32, 29, 35, 31, 33, 35]
total = sum(Temperatura)

promedio = sum(Temperatura)/len(Temperatura)
print("EL promedio semanal es:", promedio)

#Imprimir el dia mas caluroso

max_temp = max(Temperatura)
dia_caluroso = Temperatura.index(max_temp) + 1
print("Dia mas caluroso:", dia_caluroso, "con", max_temp, "C")