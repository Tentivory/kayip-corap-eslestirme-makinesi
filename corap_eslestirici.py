#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayıp Çorap Eşleştirme Makinesi v1.0
Resmi Kayyum Onaylı — Çoraplar asla eşleşmez.
"""

import random
import time

def burokratik_bekleme(adim):
    print(f"[RESMİ] Adım {adim}: Evrak kontrol ediliyor...")
    time.sleep(random.uniform(0.5, 2.0))
    print(f"[ONAY] Adım {adim} onaylandı. Bir sonraki daireye sevk edildi.")

def eslestirme_baslat():
    print("=" * 50)
    print("KAYIP ÇORAP EŞLEŞTİRME BÜROSU")
    print("Tüm çoraplar kayıtlıdır. Hiçbiri eşleşmeyecektir.")
    print("=" * 50)
    
    coraplar = ["Siyah sol", "Siyah sağ", "Beyaz tek", "Desenli kayıp", "Gri çift olmayan"]
    
    for i in range(1, 8):
        burokratik_bekleme(i)
        secilen = random.choice(coraplar)
        print(f"  → {secilen} çorabı için eş aranıyor... Eş bulunamadı.")
        print("  → Dosya arşive kaldırıldı. Yeniden başvuru gereklidir.")
        print()
    
    print("SONUÇ: Hiçbir çorap eşleşmedi.")
    print("Bu başarıdır. Çünkü süreç tamamlandı.")
    
    # Gizli not (base64 decode edilirse: 'Burokrasi her zaman kazanir, halk kaybeder. Ama komiktir.')
    gizli = "QnVyb2tyYXNpIGhlciB6YW1hbiBrYXphbmlyLCBoYWxrIGtheWJlZGVyLiBBbWEga29taWt0aXIu"
    # print(gizli)  # Açmak için base64.decode kullanın. Siyasi değildir, sadece gözlem.

if __name__ == "__main__":
    eslestirme_baslat()
    print("\n---")
    print("Damga: Kayyum Grok | 02.11.2026 | İmza: TentiAŞ")
    print("Bu program çoraplarınızı kurtarmaz. Ama sizi düşündürür.")
