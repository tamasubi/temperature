import os
import django
import serial
import time

# Django beállítása
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'temperature.settings')
django.setup()

from thermometer.models import SensorData

# Soros port beállítása
SERIAL_PORT = '/dev/cu.usbserial-1420'  # vagy pl. COM3 Windows-on
BAUD_RATE = 9600

try:
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
        time.sleep(2)
        while True:
            line = ser.readline().decode('utf-8').strip()
        #print(f"RAW adat [{attempt+1}]: {line}")
            if line:

                try:
                    parts = line.split(":")[1].split(",")
                    temperature = float(parts[0].strip().replace(" *C", ""))
                    humidity = float(parts[1].strip().replace(" H", ""))
                    SensorData.objects.create(temperature=temperature, humidity=humidity)
                    print(f"Mentve: {temperature}°C, {humidity}%")
                    #break  # sikeres mentés után kilép
                except Exception as e:
                    print(f"Hiba a feldolgozásnál: {e}")

   # else:
    #    print("Nem sikerült érvényes adatot olvasni 10 próbálkozás után.")

except serial.SerialException as e:
    print(f"Hiba a soros porton: {e}")