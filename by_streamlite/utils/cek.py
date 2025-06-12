import time
from wheater_utils import get_forecast, get_current_weather

def check_weather_script():
    print("=== Mengecek Cuaca Saat Ini dan Forecast ===")
    
    # Ambil cuaca saat ini
    current = get_current_weather()
    print("\n[Cuaca Saat Ini]")
    print(f"Kota       : {current.get('city', 'Tidak diketahui')}")
    print(f"Info       : {current.get('info', 'Tidak tersedia')}")
    print(f"Icon URL   : {current.get('icon_url', '')}")
    
    fetched_at = current.get('fetched_at', 0)
    if fetched_at:
        print(f"Fetched at : {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(fetched_at))}")
    else:
        print("Fetched at : Tidak tersedia")
    
    # Ambil forecast (cache atau fresh)
    print("\n[Mengambil Data Forecast...]")
    forecast = get_forecast()
    if forecast:
        print("[Forecast Berhasil Diperoleh]")
        print(f"Jumlah Data Per Jam: {len(forecast.get('hourly', []))}")
        print(f"Jumlah Data Harian : {len(forecast.get('daily', []))}")
    else:
        print("[ERROR] Tidak bisa mengambil data forecast")

if __name__ == "__main__":
    check_weather_script()
