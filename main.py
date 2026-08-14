# PGBrain Desktop - aplikasi Windows dengan otak Gemini
# Menggunakan pywebview (mesin Edge WebView2 bawaan Windows 10/11)
import os, sys
import webview

def resource_path(name):
    # Saat dikemas PyInstaller, file ikut di folder sementara _MEIPASS
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)

if __name__ == "__main__":
    html_file = resource_path("index.html")
    webview.create_window(
        "PGBrain — Multi AI",
        html_file,
        width=1000,
        height=720,
        min_size=(420, 560),
        background_color="#0b1220",
    )
    webview.start()
