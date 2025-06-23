import time
import threading

from config import CURRENT_RAW_FILE, FORECAST_RAW_FILE
from wheater_logic.time_utils import is_expired
from wheater_logic.weather_api import fetch_and_save_raw, fetch_and_save_forecast
from wheater_logic.current_parser import parse_and_save_clean
from wheater_logic.forecast_parser import parse_and_save_hourly

def run_all():
    print("🌀 [RUN] Memulai pengecekan dan pembaruan data cuaca...\n")

    if is_expired(CURRENT_RAW_FILE, max_age=1800):
        print("⏳ [CURRENT] Data expired, fetching ulang...")
        fetch_and_save_raw()
        parse_and_save_clean()
    else:
        print("✅ [CURRENT] Data masih valid, skip fetch.")

    if is_expired(FORECAST_RAW_FILE, max_age=1800):
        print("⏳ [FORECAST] Data expired, fetching ulang...")
        fetch_and_save_forecast()
        parse_and_save_hourly()
    else:
        print("✅ [FORECAST] Data masih valid, skip fetch.")

    print("\n✅ [DONE] Semua proses pengecekan selesai.\n")

def run_periodically(interval=1800):
    def loop():
        while True:
            run_all()
            time.sleep(interval)

    thread = threading.Thread(target=loop)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    run_all()

