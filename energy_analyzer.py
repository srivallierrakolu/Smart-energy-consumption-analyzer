import matplotlib.pyplot as plt

print("======================================")
print("   SMART ENERGY CONSUMPTION ANALYZER")
print("======================================")

appliances = []
energy_values = []

n = int(input("\nEnter number of appliances: "))

total_energy = 0

for i in range(n):
    print(f"\nAppliance {i + 1}")

    name = input("Enter appliance name: ")
    power = float(input("Enter power rating (Watts): "))
    hours = float(input("Enter usage per day (hours): "))
    days = int(input("Enter number of days: "))

    # Energy consumption in kWh
    energy = (power * hours * days) / 1000

    appliances.append(name)
    energy_values.append(energy)

    total_energy += energy

    print(f"Energy consumed by {name}: {energy:.2f} kWh")

print("\n======================================")
print(f"Total Energy Consumption: {total_energy:.2f} kWh")
print("======================================")

# Display graph
plt.figure(figsize=(8, 5))
plt.bar(appliances, energy_values)

plt.xlabel("Appliances")
plt.ylabel("Energy Consumption (kWh)")
plt.title("Energy Consumption of Appliances")

plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
