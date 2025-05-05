import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo
G = nx.Graph()
#Se agregran los nodos con sus respectivas coordenadas (sacadas de google maps)
nodos_posiciones = {
    "Area gimnasio": (19.05391, -98.287331),
    "Moe Williams": (19.054415, -98.2867),
    "Hostal/Residencia": (19.055219, -98.2889),
    "Pista de atletismo": (19.055576, -98.287743),
    "Cancha de Futbol 7": (19.055415, -98.286614),
    "Templo del dolor": (19.054514, -98.285687),
    "Canchas Bourbaki": (19.057129, -98.286692),
    "Edificio de Salud": (19.053956, -98.285604),
    "Canchas al lado de Salud": (19.053619, -98.286247),
    "Colegio Ray Lindley": (19.053816, -98.284795),
    "Lago": (19.053938, -98.284697),
    "Ciencias Sociales": (19.053129, -98.283569),
    "Centro Estudiantil": (19.053693, -98.283704),
    "Colegio Cain Murray": (19.05446, -98.283812),
    "Biblioteca": (19.054122, -98.283318),
    "Playita": (19.053591, -98.283235),
    "Auditorio Udlap": (19.053539, -98.282772),
    "Colegio Jose Gaos": (19.05181, -98.28514),
    "Jardin de la meditacion": (19.05194, -98.28293),
    "Hacienda/rectoria": (19.05305, -98.28216),
    "Ciencias e Ingenierias": (19.053662, -98.28225),
    "Agora": (19.053081, -98.281148),
    "Edificio de HU": (19.05284, -98.28078),
    "Colegio Ignacio Bernal": (19.05176, -98.28012),
    "Cancha de Futbol Rapido": (19.05545, -98.28019), 
    "RH": (19.05637, -98.28225),
    "Planta Fisica": (19.05645, -98.28328),
    "Servicios Escolares": (19.05502, -98.2823),
    "Banderas": (19.0539, -98.28293)
}

# Convertir coordenadas GPS a un sistema de coordenadas plano para mejor visualización
def convert_coords(coords):
    lat, lon = coords
    x = (lon + 98.29) * 10000  
    y = (lat - 19.05) * 10000
    return (x, y)

posiciones_ajustadas = {nodo: convert_coords(coords) for nodo, coords in nodos_posiciones.items()}

# Agregar nodos al grafo
G.add_nodes_from(nodos_posiciones.keys())

# Aristas con pesos (distancias (sacadas de google maps))
aristas_validas = [
("Moe Williams", "Area gimnasio", 111.86),
    ("Pista de atletismo", "Moe Williams", 119.75),
    ("Pista de atletismo", "Hostal/Residencia", 58.55),
    ("Cancha de Futbol 7", "Moe Williams", 128.47),
    ("Cancha de Futbol 7", "Pista de atletismo", 45.91),
    ("Templo del dolor", "Moe Williams", 99.9),
    ("Canchas Bourbaki", "Cancha de Futbol 7", 172.28),
    ("Edificio de Salud", "Templo del dolor", 38.6),
    ("Canchas al lado de Salud", "Templo del dolor", 30.34),
    ("Canchas al lado de Salud", "Edificio de Salud", 24.71),
    ("Colegio Ray Lindley", "Edificio de Salud", 107.47),
    ("Lago", "Templo del dolor", 114.18),
    ("Lago", "Edificio de Salud", 99.59),
    ("Lago", "Colegio Ray Lindley", 15),
    ("Ciencias Sociales", "Colegio Ray Lindley", 127.75),
    ("Centro Estudiantil", "Colegio Ray Lindley", 137.61),
    ("Centro Estudiantil", "Lago", 16.85),
    ("Centro Estudiantil", "Ciencias Sociales", 77.92),
    ("Colegio Cain Murray", "Lago", 75.85),
    ("Centro Estudiantil", "Colegio Cain Murray", 147.51),
    ("Centro Estudiantil", "Biblioteca", 89.68),
    ("Colegio Cain Murray", "Biblioteca", 83.39),
    ("Playita", "Ciencias Sociales", 30.89),
    ("Centro Estudiantil", "Playita", 34.91),
    ("Biblioteca", "Playita", 24.56),
    ("Ciencias Sociales", "Auditorio Udlap", 132.25),
    ("Playita", "Auditorio Udlap", 42.12),
    ("Colegio Jose Gaos", "Colegio Ray Lindley", 267.98),
    ("Colegio Jose Gaos", "Ciencias Sociales", 239.44),
    ("Ciencias Sociales", "Jardin de la meditacion", 164.45),
    ("Hacienda/rectoria", "Ciencias Sociales", 174.17),
    ("Colegio Cain Murray", "Planta Fisica", 261.22),
    ("Colegio Cain Murray", "Servicios Escolares", 237.27),   
    ("Biblioteca", "Servicios Escolares", 196.81),  
    ("Biblioteca", "Banderas", 37.63), 
    ("Playita", "Banderas", 43.12),
    ("Auditorio Udlap", "Hacienda/rectoria", 90.56),
    ("Jardin de la meditacion", "Hacienda/rectoria", 124.31),
    ("Auditorio Udlap", "Ciencias e Ingenierias", 80.1), 
    ("Hacienda/rectoria", "Ciencias e Ingenierias", 70.25),
    ("Hacienda/rectoria", "Agora", 160.84),
    ("Ciencias e Ingenierias", "Agora", 132.74),
    ("Edificio de HU", "Agora", 38.26),
    ("Hacienda/rectoria", "Colegio Ignacio Bernal", 258.96),
    ("Ciencias e Ingenierias", "Cancha de Futbol Rapido", 358.08),
    ("Agora", "Cancha de Futbol Rapido", 368),
    ("Servicios Escolares", "Ciencias e Ingenierias", 149.06),
    ("Banderas", "Ciencias e Ingenierias", 78.71),
    ("Canchas Bourbaki", "Planta Fisica", 413.34),    
    ("Edificio de HU", "Colegio Ignacio Bernal", 164.68),
    ("Colegio Ignacio Bernal", "Cancha de Futbol Rapido", 449.47),
    ("RH", "Cancha de Futbol Rapido", 241.62),
    ("Planta Fisica", "RH", 111.11),
    ("Servicios Escolares", "RH", 186.9),
    ("Servicios Escolares", "Planta Fisica", 229.4),
    ("Banderas", "Servicios Escolares", 146.09)
]
# Agregar aristas al grafo
G.add_weighted_edges_from(aristas_validas)

# Configurar el tamaño de la figura
plt.figure(figsize=(15, 12))

# Dibujar el grafo con las posiciones ajustadas
nx.draw(G, 
        pos=posiciones_ajustadas,
        with_labels=True,
        node_size=1000,
        node_color='lightblue',
        font_size=12,
        font_weight='bold',
        edge_color='gray',
        width=1.5)

# Dibujar etiquetas de peso en las aristas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, 
                            pos=posiciones_ajustadas,
                            edge_labels=edge_labels,
                            font_size=7,
                            label_pos=0.5)

# Agregar título y ajustar layout
plt.title("Mapa de la UDLAP con coordenadas GPS", size=15)
plt.tight_layout()

# Mostrar el mapa
plt.show()

def visualizar_subgrafo_dijkstra(grafo, origen, destino, posiciones):
    try:
        # Calcular ruta más corta
        longitud, camino = nx.single_source_dijkstra(grafo, origen, destino)
        
        # Crear subgrafo con solo los nodos y aristas del camino
        aristas_camino = list(zip(camino[:-1], camino[1:]))
        subgrafo = grafo.edge_subgraph(aristas_camino).copy()
        
        # Configurar visualización
        plt.figure(figsize=(14, 10))
        
        # Dibujar el grafo completo (fondo)
        nx.draw_networkx_nodes(grafo, posiciones, node_size=1000, node_color='lightgray', alpha=0.3)
        nx.draw_networkx_edges(grafo, posiciones, edge_color='lightgray', width=1, alpha=0.2)
        nx.draw_networkx_labels(grafo, posiciones, font_size=12, alpha=0.5)
        
        # Dibujar el subgrafo de Dijkstra (resaltado)
        nx.draw_networkx_nodes(subgrafo, posiciones, node_size=1000, node_color='lightsteelblue')
        nx.draw_networkx_edges(subgrafo, posiciones, edge_color='#ff7f0e', width=3, alpha=0.8)
        nx.draw_networkx_labels(subgrafo, posiciones, font_size=12)
        
        # Dibujar etiquetas de peso solo para el camino
        edge_labels = {(u, v): grafo.edges[u, v]['weight'] for u, v in subgrafo.edges()}
        nx.draw_networkx_edge_labels(subgrafo, posiciones, edge_labels=edge_labels, font_size=8)
        
        # Resaltar nodos de inicio y fin
        nx.draw_networkx_nodes(grafo, posiciones, nodelist=[origen], node_size=1000, node_color='plum')
        nx.draw_networkx_nodes(grafo, posiciones, nodelist=[destino], node_size=1000, node_color='palegreen')
        
        plt.title(f"Ruta más corta: {origen} → {destino}\nDistancia total: {longitud:.2f} metros", pad=20)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        
    except nx.NetworkXNoPath:
        print(f"\nNo existe camino entre {origen} y {destino}")
    except Exception as e:
        print(f"\nError al visualizar: {str(e)}")

def menu_principal():
    while True:
        print("\n" + "="*50)
        print(" SISTEMA DE RUTAS - MENÚ PRINCIPAL ".center(50, "="))
        print("="*50)
        print("1. Consultar ruta más corta (texto)")
        print("2. Visualizar ruta en el mapa")
        print("0. Salir")
        print("="*50)
        
        try:
            opcion = int(input("\n► Seleccione una opción: "))
            
            if opcion == 0:
                break
            elif opcion == 1:
                menu_consulta_texto()
            elif opcion == 2:
                menu_visualizacion()
            else:
                print("\n¡Opción inválida! Por favor seleccione 0, 1 o 2")
                
        except ValueError:
            print("\n¡Error! Ingrese un número válido")

def menu_consulta_texto():
    nodos_ordenados = list(nodos_posiciones.keys())
    
    while True:
        print("\n" + "="*50)
        print(" CONSULTA DE RUTA (TEXTO) ".center(50, "="))
        print("="*50)
        
        for i, nodo in enumerate(nodos_ordenados, 1):
            print(f"{i:2d}. {nodo.ljust(25)}", end="")
            if i % 2 == 0 or i == len(nodos_ordenados):
                print()
        
        print("\n 0. Volver al menú principal")
        print("="*50)
        
        try:
            origen_num = int(input("\n► Seleccione el NÚMERO del nodo de ORIGEN (0 para volver): "))
            if origen_num == 0:
                break
            origen = nodos_ordenados[origen_num-1]
            
            destino_num = int(input("► Seleccione el NÚMERO del nodo de DESTINO: "))
            destino = nodos_ordenados[destino_num-1]
            
            print("\n" + " RESULTADO ".center(50, "-"))
            distancia, ruta = nx.single_source_dijkstra(G, origen, target=destino)
            print(f"● Ruta más corta desde: {origen}")
            print(f"● Hasta: {destino}")
            print(f"● Distancia total: {distancia:.2f} metros")
            print("● Camino completo:")
            print("  " + " → ".join(ruta))
            print("-"*50)
            
            continuar = input("\n¿Desea visualizar esta ruta en el mapa? (s/n): ").lower()
            if continuar == 's':
                visualizar_subgrafo_dijkstra(G, origen, destino, posiciones_ajustadas)
                
        except (ValueError, IndexError):
            print("\n¡ERROR! Por favor ingrese números válidos del menú.")
        except nx.NetworkXNoPath:
            print(f"\nNo existe camino entre los nodos seleccionados")

def menu_visualizacion():
    nodos_ordenados = list(nodos_posiciones.keys())
    
    while True:
        print("\n" + "="*50)
        print(" VISUALIZACIÓN DE RUTA EN MAPA ".center(50, "="))
        print("="*50)
        
        for i, nodo in enumerate(nodos_ordenados, 1):
            print(f"{i:2d}. {nodo.ljust(25)}", end="")
            if i % 2 == 0 or i == len(nodos_ordenados):
                print()
        
        print("\n 0. Volver al menú principal")
        print("="*50)
        
        try:
            origen_num = int(input("\n► Seleccione el NÚMERO del nodo de ORIGEN (0 para volver): "))
            if origen_num == 0:
                break
            origen = nodos_ordenados[origen_num-1]
            
            destino_num = int(input("► Seleccione el NÚMERO del nodo de DESTINO: "))
            destino = nodos_ordenados[destino_num-1]
            
            visualizar_subgrafo_dijkstra(G, origen, destino, posiciones_ajustadas)
            
        except (ValueError, IndexError):
            print("\n¡ERROR! Por favor ingrese números válidos del menú.")

# Iniciar el sistema
print("\n" + " BIENVENIDO AL SISTEMA DE RUTAS UDLAP ".center(50, "="))
menu_principal()
