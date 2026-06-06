# 🤖 Chatbot LAN Party - Equip 5

Aquest és el projecte de programació d'un xatbot assistent integrat en un Portfoli Digital, dissenyat específicament per respondre de manera automatitzada a les preguntes freqüents (FAQs) dels usuaris que assisteixen a una **LAN Party**.

El projecte s'ha desenvolupat com a part del mòdul de programació del cicle **SMX (Sistemes Microinformàtics i Xarxes)** de l'Institut Castellbisbal.

---

## 🏗️ Arquitectura del Projecte (Model de 3 Capes)

L'aplicació segueix una arquitectura distribuïda dividida en tres capes independents per garantir un codi modular i escalable:

1. **FrontEnd (Interfície d'Usuari):** Un giny (widget) de xat integrat a la pàgina web del Portfoli de WordPress, programat en **HTML, CSS i JavaScript**. S'encarrega de recollir l'entrada de l'usuari i mostrar la resposta de manera asíncrona mitjançant l'API `fetch()`.
2. **BackEnd (Lògica de Control):** Un servidor web programat en **Python** utilitzant el microframework **Flask**. Gestiona les peticions HTTP de tipus `POST` a l'endpoint `/api/chat`, processa el text i cerca coincidències.
3. **Capa de Persistència de Dades (JSON):** Un fitxer de dades estructurades anomenat `faqs.json` que emmagatzema les preguntes i respostes de la LAN Party amb un format de llista d'objectes (ID, pregunta, resposta). Actua com a base de dades local.

---

## 🌐 Connexió i Canalització (ngrok)

Com que el servidor de Flask s'executa localment a la màquina de desenvolupament (`localhost:5000`), s'utilitza **ngrok** per obrir un túnel HTTP segur cap a Internet. Això genera una URL pública (`https://...`) que permet al JavaScript del FrontEnd comunicar-se directament amb el nostre codi de Python sense restriccions de tallafocs o de xarxa.

---

## 📁 Estructura del Repositori

* `Chatbot.py` / `app.py`: Codi principal del BackEnd en Flask amb la lògica de control i la gestió d'errors (`try-except`).
* `faqs.json`: Base de dades local amb la informació de suport de la LAN Party.
* `CHANGELOG.md`: Registre oficial de versions, millores i canvis realitzats per l'equip.
* `README.md`: Documentació principal del projecte (aquest fitxer).

---

## 🛠️ Requisits i Execució

Per fer funcionar el BackEnd localment, cal instal·lar Python i les dependències del projecte:

```bash
pip install flask flask-cors
