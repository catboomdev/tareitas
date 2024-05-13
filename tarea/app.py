import random
from flask import Flask, render_template, request
from flask import Flask

app = Flask(__name__, static_folder='static')


app = Flask(__name__)

# Lista de opciones para las tareas y las cosas que hay que llevar
opciones_tareas = {
    'religion': [
        """El taoísmo y el budismo son dos filosofías y tradiciones religiosas que han ejercido una profunda influencia en la historia y la cultura de Asia. Aunque tienen orígenes diferentes y enfoques distintos, ambos comparten una búsqueda espiritual que busca comprender el significado de la vida y alcanzar la iluminación.

        Taoísmo:
        El taoísmo, también conocido como daoísmo, es una antigua tradición filosófica y religiosa originaria de China. Su nombre proviene del concepto central de "Tao", que se traduce comúnmente como "el Camino" o "la Vía". El taoísmo se atribuye al sabio chino Laozi, quien escribió el texto fundamental del taoísmo, el "Tao Te Ching".

        El taoísmo enseña la importancia de vivir en armonía con el Tao, que representa el orden natural del universo. Se enfoca en la espontaneidad, la simplicidad y el flujo natural de la vida. Los taoístas buscan alcanzar el estado de Wu Wei, que se traduce como "acción sin esfuerzo" o "no hacer", donde uno está en armonía con el Tao y permite que las cosas sucedan de forma natural.

        Además del Tao Te Ching, el taoísmo también se basa en otras escrituras, como el Zhuangzi, que profundiza en temas como el relativo y el absoluto, la naturaleza del cambio y la relatividad de las perspectivas humanas.

        El taoísmo también incluye prácticas como el tai chi, el qi gong y la alquimia interna, que buscan cultivar la energía vital (Qi) y mantener el equilibrio entre el cuerpo y la mente.

        Budismo:
        El budismo es una religión y filosofía basada en las enseñanzas de Siddhartha Gautama, quien más tarde sería conocido como Buda. Surgió en el subcontinente indio alrededor del siglo VI a.C. y se ha extendido por todo el mundo, convirtiéndose en una de las principales religiones del mundo.

        El budismo se centra en las Cuatro Nobles Verdades y el Noble Óctuple Sendero, que proporcionan un marco para comprender la naturaleza del sufrimiento humano y cómo superarlo. Según estas enseñanzas, el sufrimiento (dukkha) es parte integral de la existencia humana, pero puede superarse a través de la comprensión y la práctica adecuadas.

        Una de las características distintivas del budismo es la doctrina de la impermanencia (Anicca), que enseña que todas las cosas están sujetas al cambio y la transitoriedad. Esta comprensión lleva a la noción de vacuidad (Sunyata), que sostiene que no hay una realidad intrínseca o permanente en las cosas.

        El budismo también incluye prácticas de meditación, como la atención plena (mindfulness) y la meditación vipassana, que buscan desarrollar la conciencia y la comprensión profunda de la naturaleza de la mente y la realidad.

        Conclusiones:
        Aunque el taoísmo y el budismo tienen orígenes y enfoques diferentes, comparten algunas similitudes en su búsqueda de la sabiduría y la comprensión espiritual. Ambas tradiciones ofrecen enseñanzas profundas sobre cómo vivir una vida significativa y en armonía con el universo. Explorar estas filosofías puede ofrecer una perspectiva única sobre la naturaleza de la existencia y el propósito de la vida."""
    ],
    'sociales': [
        """ Elige solo 3 
        El potro: Consistía en atar al acusado a una especie de mesa con correas, y luego estirar gradualmente sus extremidades mediante palancas, causando dolor extremo y, en ocasiones, dislocaciones o fracturas.

        La rueda: El acusado era atado a una gran rueda y golpeado con objetos contundentes mientras era girado lentamente, causando fracturas, hemorragias internas y otros daños graves.

        La garrucha: El acusado era suspendido en el aire mediante una polea y luego bajado bruscamente, lo que provocaba dislocaciones de hombros, brazos o piernas.

        La doncella de hierro: Una especie de sarcófago con puntas en su interior. El acusado era encerrado dentro y las puntas perforaban su cuerpo lentamente cuando se cerraba la puerta.

        La pera de la angustia: Un instrumento metálico en forma de pera que se introducía en la boca, el ano o la vagina del acusado y luego se expandía, causando desgarros y lesiones internas.

        El aplastamiento de los dedos: Los dedos del acusado eran colocados entre dos tablas y luego aplastados con fuerza mediante tornillos o prensas.

        La parrilla: El acusado era atado a una parrilla metálica y colocado sobre un fuego, sufriendo quemaduras severas en todo su cuerpo.

        La camisa de fuego: Una prenda de tela empapada en aceite que se colocaba sobre el acusado y luego se prendía fuego, provocando quemaduras graves.

        La ducha fría: El acusado era sometido a un chorro de agua fría durante períodos prolongados, lo que causaba hipotermia y otros problemas de salud.

        La silla de tortura: Una silla con puntas afiladas en el asiento y respaldo, diseñada para causar dolor al acusado cuando se sentaba en ella.

        El tormento de la cuerda: El acusado era suspendido en el aire mediante cuerdas atadas a sus extremidades, causando dislocaciones y dolor extremo.

        La tenaza caliente: Las tenazas se calentaban al rojo vivo y se utilizaban para arrancar trozos de carne del cuerpo del acusado.

        El tormento del agua: Consistía en forzar al acusado a ingerir grandes cantidades de agua, lo que causaba distensión abdominal y asfixia.

        El tormento de la horca: El acusado era colgado de una horca durante períodos prolongados, causando asfixia y lesiones en el cuello.

        El tormento de la estaca: El acusado era empalado en una estaca afilada, causando heridas internas y hemorragias graves.

        La picana eléctrica: Se aplicaban descargas eléctricas al cuerpo del acusado, causando dolor extremo y convulsiones.

        La flagelación: El acusado era azotado con látigos o correas, causando laceraciones en la piel y dolor intenso.

        El tormento de la rata: Se colocaba una rata hambrienta dentro de un recipiente en el abdomen del acusado y se calentaba el recipiente, obligando a la rata a roer su camino hacia afuera.

        La inmersión en agua helada: El acusado era sumergido en agua helada durante períodos prolongados, causando hipotermia y riesgo de ahogamiento.

        La privación del sueño: El acusado era privado de sueño durante días o incluso semanas, lo que causaba alucinaciones, agotamiento físico y deterioro mental.
        No hay dibujos pagina en fase beta UnU"""
    ],
    'ingles': [
        """1:get up  hora 6:00 AM
        2:Leave home hora 7:30 AM
        3:start work hora 8:00 AM
        4:have lunch hora 12:15 PM
        5:get home 3:15 PM
        6:have dinner 6:45 PM
        7:have breakfast 6:15 AM
        8:take the bus to my work 7:10 AM
        9:Have break 10:00 AM
        10:meet my boss 1:15 PM
        11:play tennis 4:00 PM
        12:meet my friends 8:30 PM
        13:have shower 6:30 AM 
        14:finish work 2:30 PM 
        15:start work again 10:30 PM
        16:get my office 7:45 AM
        17:watch the news 6:45 PM 
        18:Go to bed 11:00 PM  """
    ]
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    tarea = request.form['tarea']
    tarea_minusculas = tarea.lower()  # Convertir la entrada a minúsculas para facilitar la comparación
    
    if 'tarea' in tarea_minusculas and 'religion' in tarea_minusculas:
        tarea_elegida = random.choice(opciones_tareas['religion'])
        return tarea_elegida
    elif 'tarea' in tarea_minusculas and 'sociales' in tarea_minusculas:
        tarea_elegida = random.choice(opciones_tareas['sociales'])
        return tarea_elegida
    elif 'tarea' in tarea_minusculas and 'ingles' in tarea_minusculas:
        tarea_elegida = random.choice(opciones_tareas['ingles'])
        return tarea_elegida
    else:
        return "No se reconoce la tarea solicitada."

if __name__ == '__main__':
    app.run(debug=True)

