#Rumus dari fahrenheit ke celcius (5/9) * (fahrenheit - 32)
#Rumus dari kelvin ke celcius (kelvin - 273)
#Rumus dari reamur ke celcius (5/4) * reamur

print("\n=====>Konverter Suhu<=====")

#Rumus untuk konversi fahrenheit ke celcius
print("\n=====>Konversi fahrenheit<=====")
fahrenheit = float(input("Masukkan nilai fahrenheit : "))
celcius = (5/9) * (fahrenheit - 32)
#Konversi dari fahrenheit ke celcius
print("Nilai dalam bentuk celcius :", celcius)

#Rumus untuk konversi kelvin ke celcius
print("\n=====>Konversi kelvin<=====")
kelvin = float(input("Masukkan nilai kelvin : "))
celcius = kelvin - 273
#Konversi dari kelvin ke celcius
print("Nilai dalam bentuk celcius :", celcius)

#Rumus untuk konversi reamur ke celcius
print("\n=====>Konversi reamur<=====")
reamur = float(input("Masukkan nilai reamur : "))
celcius = (5/4) * reamur
#Konversi dari reamur ke celcius
print("Nilai dalam bentuk celcius :", celcius)