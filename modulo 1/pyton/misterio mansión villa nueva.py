import time

def mostrar_texto_lento(texto, velocidad=0.03):
    """Muestra el texto letra por letra para dar efecto de escritura"""
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(velocidad)
    print()

def introduccion():
    mostrar_texto_lento("\nBienvenido a la  Mansion villa nueva")
    mostrar_texto_lento("Estas a punto de embarcarte en una aventura de decisiones cruciales.")
    mostrar_texto_lento("Tus elecciones determinaran tu destino.\n")
    time.sleep(1)
    mostrar_texto_lento("Es una fria noche de septiembre. Has recibido una carta misteriosa invitandote a la Mansian villa nueva.")
    mostrar_texto_lento("La carta menciona un tesoro escondido y un secreto familiar.")
    
    decision = input("\n¿Que decides hacer? (1) Ir a la mansion (2) Ignorar la carta: ")
    if decision == "1":
        llegada_mansion()
    else:
        final_ignorar()

def llegada_mansion():
    mostrar_texto_lento("\nDecides ir a la mansion. Despues de un largo viaje, llegas al imponente edificio.")
    mostrar_texto_lento("La puerta principal esta entreabierta. Dentro solo se ve oscuridad...")
    mostrar_texto_lento("Escuchas un ruido que viene del jardin a tu izquierda.")
    
    decision = input("\n¿Que haces? (1) Entrar por la puerta principal (2) Investigar el jardin: ")
    if decision == "1":
        entrada_principal()
    else:
        investigar_jardin()

def entrada_principal():
    mostrar_texto_lento("\nAl entrar, la puerta se cierra de golpe detras de ti. Estas atrapado.")
    mostrar_texto_lento("Frente a ti hay dos puertas: una roja a la izquierda y una azul a la derecha.")
    
    decision = input("\n¿Que puerta eliges? (1) Puerta roja (2) Puerta azul: ")
    if decision == "1":
        puerta_roja()
    else:
        puerta_azul()

def investigar_jardin():
    mostrar_texto_lento("\nEn el jardin encuentras un cofre antiguo bajo un arbol.")
    mostrar_texto_lento("El cofre tiene un candado con un extraño simbolo.")
    
    decision = input("\n¿Que haces? (1) Intentar abrirlo (2) Volver a la entrada principal: ")
    if decision == "1":
        intentar_abrir_cofre()
    else:
        entrada_principal()

def puerta_roja():
    mostrar_texto_lento("\nAl abrir la puerta roja, te encuentras en una biblioteca llena de libros antiguos.")
    mostrar_texto_lento("En el centro hay un libro que brilla con una luz tenue.")
    
    decision = input("\n¿Que haces? (1) Examinar el libro (2) Salir de la biblioteca: ")
    if decision == "1":
        examinar_libro()
    else:
        entrada_principal()

def puerta_azul():
    mostrar_texto_lento("\nLa puerta azul te lleva a un salon con un espejo grande.")
    mostrar_texto_lento("Tu reflejo hace movimientos que tu no haces...")
    
    decision = input("\n¿Qué haces? (1) Acercarte al espejo (2) Romper el espejo: ")
    if decision == "1":
        acercarse_espejo()
    else:
        romper_espejo()

def examinar_libro():
    mostrar_texto_lento("\nAl abrir el libro, encuentras un mapa del sótano de la mansión.")
    mostrar_texto_lento("El mapa muestra la ubicación del tesoro familiar.")
    
    decision = input("\n¿Qué haces? (1) Ir al sótano (2) Seguir buscando en la biblioteca: ")
    if decision == "1":
        ir_sotano()
    else:
        mostrar_texto_lento("\nPasas horas buscando pero no encuentras nada más. Pierdes tu oportunidad.")
        final_sin_tesoro()

def acercarse_espejo():
    mostrar_texto_lento("\nTu reflejo te extiende la mano. Sientes una extraña energía.")
    mostrar_texto_lento("Te das cuenta de que es un portal a otra dimensión.")
    
    decision = input("\n¿Qué haces? (1) Entrar al espejo (2) Alejarte: ")
    if decision == "1":
        entrar_espejo()
    else:
        mostrar_texto_lento("\nDecides no arriesgarte y sales corriendo de la mansión.")
        final_huida()

def romper_espejo():
    mostrar_texto_lento("\nAl romper el espejo, liberas un espíritu que estaba atrapado.")
    mostrar_texto_lento("El espíritu agradecido te revela la ubicación del tesoro.")
    
    decision = input("\n¿Qué haces? (1) Buscar el tesoro (2) Huir de la mansión: ")
    if decision == "1":
        buscar_tesoro()
    else:
        final_huida()

# Funciones de finales
def final_ignorar():
    mostrar_texto_lento("\nDecides ignorar la carta. La vida sigue como siempre.")
    mostrar_texto_lento("Pero a veces te preguntas qué habrías encontrado en la mansión...")
    reiniciar()

def final_sin_tesoro():
    mostrar_texto_lento("\nNo logras encontrar el tesoro. La mansión te atrapa para siempre.")
    reiniciar()

def final_huida():
    mostrar_texto_lento("\nHuyes de la mansión. Nunca sabrás qué secretos escondía.")
    reiniciar()

def buscar_tesoro():
    mostrar_texto_lento("\nSiguiendo las pistas del espíritu, encuentras el tesoro familiar.")
    mostrar_texto_lento("Eres rico, pero ahora debes lidiar con la maldición que lo acompaña...")
    reiniciar()

def entrar_espejo():
    mostrar_texto_lento("\nAl cruzar el espejo, descubres un mundo paralelo.")
    mostrar_texto_lento("Aquí tomaste decisiones diferentes. ¿Cuál es la realidad verdadera?")
    reiniciar()

def ir_sotano():
    mostrar_texto_lento("\nEn el sótano encuentras no un tesoro de oro, sino los diarios de tu familia.")
    mostrar_texto_lento("Descubres la verdad sobre tus antepasados y tu propio destino.")
    reiniciar()

def intentar_abrir_cofre():
    mostrar_texto_lento("\nEl cofre contiene una llave y una nota: 'Esta llave abre tu futuro'.")
    mostrar_texto_lento("Pero al tomarla, la mansión comienza a derrumbarse.")
    
    decision = input("\n¿Qué haces? (1) Usar la llave en la puerta principal (2) Correr al jardín: ")
    if decision == "1":
        usar_llave()
    else:
        correr_jardin()

def usar_llave():
    mostrar_texto_lento("\nLa llave abre no la puerta, sino un pasadizo secreto.")
    mostrar_texto_lento("Siguiéndolo, encuentras la verdad sobre la mansión y tu linaje.")
    reiniciar()

def correr_jardin():
    mostrar_texto_lento("\nLogras escapar justo cuando la mansión colapsa.")
    mostrar_texto_lento("La llave desaparece de tu mano. El misterio permanece...")
    reiniciar()

def reiniciar():
    decision = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
    if decision == "s":
        introduccion()
    else:
        mostrar_texto_lento("\nGracias por jugar 'El Misterio de la Mansión villa nueva.")

# Iniciar el juego
if __name__ == "__main__":
    introduccion()
    
    #nota para quien sea espero disfruten la historia fruto de 2 ia y un monton de correciones y videos de youtube nose si la regla del tiempo de texto funcione correctamente pero almenos el codigo funciona hora 02:32 am
    
    #posdata: ultima correcion y areglo de un bug en el final del tesoro q hacia q se corrompa todo a la vrg espero q ya funcione hora 12:58 am del dia de entrega 