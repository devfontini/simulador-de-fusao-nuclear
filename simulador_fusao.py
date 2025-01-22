import matplotlib.pyplot as plt
import numpy as np

def simulate_fusion(temperature, density, time):
    """
    Simula uma reação de fusão nuclear com base em temperatura, densidade e tempo.
    Retorna a energia liberada e o gráfico do processo.
    """
    # Constantes físicas (valores simplificados)
    k = 1.38e-23  # Constante de Boltzmann (J/K)
    energy_per_reaction = 17.6e6 * 1.6e-13  # Energia por fusão de deutério-trítio (J)

    # Cálculo da taxa de reações
    reaction_rate = density * np.exp(-1e8 / temperature)  # Aproximação simplificada

    # Energia total liberada
    total_energy = reaction_rate * energy_per_reaction * time

    # Geração de dados para o gráfico
    time_steps = np.linspace(0, time, 100)
    energy_steps = reaction_rate * energy_per_reaction * time_steps

    return total_energy, time_steps, energy_steps

def plot_simulation(time_steps, energy_steps, temperature, density):
    """
    Plota o gráfico da energia liberada ao longo do tempo.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(time_steps, energy_steps, label="Energia Liberada", color="red")
    plt.title(f"Simulação de Fusão Nuclear\nTemperatura: {temperature} K | Densidade: {density} partículas/m³")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Energia Liberada (J)")
    plt.legend()
    plt.grid(True)
    plt.savefig("energia_liberada.png")  # Salvar o gráfico como imagem
    plt.show()

if __name__ == "__main__":
    print("=== Simulador de Fusão Nuclear ===")
    
    # Entrada de dados do usuário
    temperature = float(input("Digite a temperatura (em Kelvin): "))
    density = float(input("Digite a densidade (partículas/m³): "))
    time = float(input("Digite o tempo da simulação (em segundos): "))
    
    # Simular e calcular energia
    total_energy, time_steps, energy_steps = simulate_fusion(temperature, density, time)
    
    print(f"\nEnergia total liberada na fusão: {total_energy:.2e} J")

    # Plotar os resultados
    plot_simulation(time_steps, energy_steps, temperature, density)
