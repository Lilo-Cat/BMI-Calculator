# Calculator BMI

print("BMI CALCULATOR")
print("--------------")

berat_badan = input("Input your body weight (kg): ") # Input -> Data String
berat_badan = float(berat_badan)
tinggi_badan = input("Input your height (m): ")
tinggi_badan = float(tinggi_badan)

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

print(f"NIlai BMI anda adalah {bmi:.2f} kg/m")
print("Nilai BMI normal adalah 18.5 kg/m^2 - 25 kg/m^2")
print(f"Berat badan ideal anda adalah dalam rentang {berat_badan_ideal['bawah']:.2f} - {berat_badan_ideal['atas']:.2f}")

print("Terima kasih telah menggunakan kalkulator BMi index buatan saya")


