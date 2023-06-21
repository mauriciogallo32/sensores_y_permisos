import machine
import utime

#Configura los pines del KY-040
clk_pin = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
dt_pin = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
sw_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

#Variables para almacenar el estado anterior
clk_state = clk_pin.value()
dt_state = dt_pin.value()

#Función para manejar el evento de giro
def handle_rotation(pin):
    global clk_state, dt_state
    clk_state_new = clk_pin.value()
    dt_state_new = dt_pin.value()

    if clk_state != clk_state_new:
        if dt_state != clk_state_new:
            print("Giro en sentido horario")
        else:
            print("Giro en sentido antihorario")

    clk_state = clk_state_new
    dt_state = dt_state_new

#Asigna la función de manejo de eventos al pin CLK
clk_pin.irq(handler=handle_rotation, trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING)

#Bucle principal
while True:
    if sw_pin.value() == 0:
        print("Botón presionado")

    utime.sleep(0.2)