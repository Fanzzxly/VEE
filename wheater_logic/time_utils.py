import os
import time

def is_expired(path, max_age=1800):
    """
    Cek apakah file sudah expired berdasarkan umur maksimal (dalam detik).
    
    Return True jika file tidak ada atau sudah kadaluarsa.
    """
    if not os.path.exists(path):
        return True
    return (time.time() - os.path.getmtime(path)) > max_age
