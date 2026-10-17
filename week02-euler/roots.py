import numpy as np
import matplotlib.pyplot as plt

def visualizza_radici_nesime(z, n):
    """
    Calcola e visualizza le radici n-esime di un numero complesso z.
    """
    # 1. Calcolo del modulo e dell'argomento principale
    r = np.abs(z)
    theta = np.angle(z)
    
    # 2. Modulo delle radici n-esime
    R = r ** (1 / n)
    
    # 3. Generazione delle n radici tramite la formula esponenziale
    k = np.arange(n)
    argomenti = (theta + 2 * np.pi * k) / n
    radici = R * np.exp(1j * argomenti)
    
    # Stampa dei risultati nella console
    print(f"=== Radici {n}-esime di z = {z} ===")
    for i, w in enumerate(radici):
        print(f"w_{i} = {w.real:.4f} + {w.imag:.4f}i  (Forma polare: R = {R:.4f}, arg = {argomenti[i]:.4f} rad)")
    
    # 4. Creazione del grafico con matplotlib
    plt.figure(figsize=(7, 7))
    
    # Disegno della circonferenza di raggio R
    cerchio = plt.Circle((0, 0), R, color='skyblue', linestyle='--', fill=False, linewidth=1.5, label=f'Circonferenza di raggio R = {R:.2f}')
    plt.gca().add_patch(cerchio)
    
    # Tracciamento del poligono regolare che unisce le radici
    poligono_x = np.append(radici.real, radici.real[0])
    poligono_y = np.append(radici.imag, radici.imag[0])
    plt.plot(poligono_x, poligono_y, color='orange', linestyle='-', linewidth=1, alpha=0.7, label='Poligono regolare')
    
    # Plot dei punti corrispondenti alle radici
    plt.scatter(radici.real, radici.imag, color='red', s=70, zorder=5, label=f'Radici {n}-esime')
    
    # Etichette per ciascuna radice
    for i, w in enumerate(radici):
        plt.annotate(f"  w_{i}", (w.real, w.imag), textcoords="offset points", xytext=(5, 5), ha='left', fontweight='bold', fontsize=11)
        
    # Configurazione degli assi e della griglia
    limite = R * 1.4 if R > 1 else 1.5
    plt.xlim(-limite, limite)
    plt.ylim(-limite, limite)
    plt.axhline(0, color='black', linewidth=1, linestyle='-')
    plt.axvline(0, color='black', linewidth=1, linestyle='-')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Titoli e legenda
    plt.title(f"Visualizzazione Geometrica delle Radici {n}-esime di z = {z}", fontsize=12, fontweight='bold', pad=15)
    plt.xlabel("Parte Reale", fontsize=10)
    plt.ylabel("Parte Immaginaria", fontsize=10)
    plt.legend(loc='upper right')
    
    # Mostra il grafico
    plt.show()

# Esempio pratico: Calcoliamo e visualizziamo le radici cubiche (n = 3) di z = -8
visualizza_radici_nesime(z=-8+0j, n=3)

# Puoi provare anche altri esempi modificando i parametri, ad esempio:
# visualizza_radici_nesime(z=1+1j, n=4)  # Radici quarte di 1 + ils 