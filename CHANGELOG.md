# Changelog - Equip 5 (Chatbot LAN Party)

## [1.1.0] - 2026-06-03
### Afegit
- Creat el fitxer `faqs.json` amb les dades estructurades de la LAN Party (preguntes sobre xarxa, cables, perifèrics i seguretat).
- Creat el BackEnd en Flask (`app.py`) integrat amb la lectura dinàmica de l'array JSON.
- Afegit control d'excepcions (try-except) per a fitxers no trobats o JSON mal configurats.

### Modificat
- Connectat el FrontEnd del xatbot amb l'endpoint de Flask mitjançant peticions POST asíncronas.
