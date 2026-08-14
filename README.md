# NEXA Desktop — aplikasi Windows (.exe) bertenaga Gemini

Aplikasi desktop mandiri: buka NEXA.exe, jendela aplikasi langsung muncul —
tanpa browser. File .exe dibangun otomatis oleh GitHub Actions,
jadi kamu tidak perlu menginstal Python atau alat apa pun di komputer.

## Cara pakai
1. Buat repository baru di GitHub (Public).
2. Unggah SEMUA isi folder ini ke repository, termasuk folder `.github`
   (strukturnya harus tetap sama).
3. Buka tab **Actions** -> workflow **Build EXE** jalan otomatis (± 3-5 menit).
   Kalau tidak jalan, klik "Build EXE" -> "Run workflow".
4. Buka hasil run yang hijau -> bagian **Artifacts** -> unduh **NEXA-windows**.
5. Ekstrak zip -> jalankan `NEXA.exe`. Selesai.

Catatan:
- Butuh Windows 10/11 (memakai mesin Edge WebView2 yang sudah bawaan Windows).
- Saat pertama dijalankan, Windows SmartScreen mungkin memberi peringatan
  karena exe belum ditandatangani -> klik "More info" -> "Run anyway".
- Aplikasi butuh internet hanya untuk bicara ke server Gemini (Google).

## Mengubah isi aplikasi
Semua tampilan & fitur ada di satu file: `index.html`.
Edit file itu, push ke GitHub, dan .exe baru dibangun otomatis.
