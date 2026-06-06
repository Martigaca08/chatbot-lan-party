# Changelog - Equip 5 (Chatbot LAN Party)

## [0.1.0] - 2026-02-10
### Afegit
- Configuració inicial del repositori a GitHub Classroom
- Tots els membres de l'equip units al repositori
- Redacció del README.md amb la justificació de l'entorn de treball
- Vinculació de Google Colab amb el compte de GitHub mitjançant OAuth
- Generació de l'API Key a Google IA Studio
- Configuració de la clau API de forma segura a Google Colab (userdata)

## [1.0.0] - 2026-06-03
### Afegit
- Creat el fitxer `faqs.json` amb les dades estructurades de la LAN Party
- Creat el BackEnd en Flask (`app.py`) integrat amb la lectura dinàmica del JSON
- Afegit control d'excepcions (try-except) per a fitxers no trobats o JSON mal configurats

### Modificat
- Connectat el FrontEnd del xatbot amb l'endpoint de Flask mitjançant peticions POST asíncrones
