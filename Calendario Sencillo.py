# Calendario sencillo
import calendar

yy = 2022 # Este es el año
mm = 8 # Este es el mes

# Mostrar el calendario ---> print(calendar.month(yy, mm))

# Obtener una lista de días en el mes
cal = calendar.monthcalendar(yy, mm)

# Día a resaltar
day = 15

# Mostrar el calendario y el dia que se quiere resaltar
for i in cal:
    for j in i:
        if j == 0:
            print("   ", end="")
        elif j == day:
            print("[%2d]" % j, end="")
        else:
            print(" %2d " % j, end="")
    print("")
