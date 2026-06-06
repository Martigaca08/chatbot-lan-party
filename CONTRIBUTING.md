# Guia de Contribució - Chatbot LAN Party (Equip 5)

Gràcies per contribuir al projecte! Aquesta guia explica com treballem en equip i com fer canvis al repositori de manera ordenada.

## Estructura del repositori

```
chatbot-lan-party/
├── Xat_bot_LAN_Party.ipynb   # Notebook principal (backend Flask + Gemini)
├── Chatbot.py                # Versió en script Python del chatbot
├── foqs.json                 # Preguntes freqüents estructurades
├── README.md                 # Documentació principal del projecte
├── CHANGELOG.md              # Registre de canvis i versions
└── CONTRIBUTING.md           # Aquesta guia
```

## Com fer canvis al repositori

### 1. Mai editar directament a `main`
Tots els canvis importants s'han de fer des d'una branca separada.

### 2. Crear una branca nova
```bash
git checkout -b nom-de-la-branca
```
Exemple: `git checkout -b millora-respostes-bot`

### 3. Fer els canvis i un commit explicatiu
```bash
git add .
git commit -m "Descripció clara del que has fet"
```
Exemple: `git commit -m "Afegits comentaris al codi del backend Flask"`

### 4. Pujar la branca i fer un Pull Request
```bash
git push origin nom-de-la-branca
```
Després, a GitHub → "Compare & pull request" → descriu els canvis.

## Convencions de commits

Usa un prefix clar al missatge del commit:

| Prefix | Quan usar-lo |
|--------|-------------|
| `feat:` | Nova funcionalitat |
| `fix:` | Correcció d'un error |
| `docs:` | Canvis a documentació (README, CHANGELOG...) |
| `refactor:` | Millora del codi sense canviar la funcionalitat |
| `style:` | Canvis de format o estil |

Exemples:
- `docs: actualitzat README amb instruccions d'instal·lació`
- `feat: afegida resposta sobre el menjar a la LAN Party`
- `fix: corregit error de CORS al servidor Flask`

## Actualitzar el CHANGELOG

Cada vegada que fas un canvi important, afegeix-lo al `CHANGELOG.md` amb la data i una descripció breu sota la versió corresponent.

## Ús de la IA (Google Gemini)

Hem usat la IA com a copilot de programació. Els prompts utilitzats i el procés d'iteració estan documentats al Portfoli Digital del projecte.

**Important**: Mai pujar claus API reals al repositori. Usar sempre placeholders com `"LA_TEVA_CLAU_AQUI"` al codi i guardar les claus reals com a Secrets a Google Colab.

## Membres de l'equip

- Martigaca08
- [Membre 2]
- [Membre 3]
