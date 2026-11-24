# CS2 Major OBS Overlay

## Schnellstart (nur GitHub Pages)
1. Öffentliches GitHub-Repository erstellen, `index.html` ins Hauptverzeichnis hochladen.
2. Settings → Pages → Deploy from a branch → main / (root) → Save.
3. Veröffentlichte URL im normalen Browser öffnen, zunächst mit `?demo=1`, anschließend ohne Demo. In OBS als Browserquelle mit 1080 × 260 px verwenden.

Die direkte API ist eine undokumentierte BO3.gg-Schnittstelle. Die CORS-Freigabe für GitHub Pages und das genaue aktuelle Antwortschema konnten nicht live verifiziert werden. Demo-Daten sind ausdrücklich fiktiv. Im Fehlerfall `?debug=1` verwenden und die Browser-Konsole prüfen. Fehlende Rundenscores werden nicht erfunden; stattdessen werden, sofern verfügbar, Map-Siege angezeigt. Prüfe vor der Nutzung die Bedingungen des Datenanbieters.

## URL-Optionen
- `?demo=1` – fiktive Daten zum Layouttest
- `?debug=1` – API-Antwort / Fehler anzeigen, nur zum Testen
- `?layout=vertical` – Matches untereinander (OBS ca. 550 × 470)
- `?upcoming=0` – ausschließlich laufende Matches
- `?refresh=30` – Abfrageintervall in Sekunden (mindestens 15)
- `?event=PGL%20Major%20Singapore%202026` – Turnierfilter (Teilstring)
- `?hideEmpty=1` – leeres Matchfeld ausblenden
- `?source=github` – optionaler JSON-Cache, siehe unten

Parameter mit `&` kombinieren.

## Optional: GitHub Actions, falls direkter Abruf an CORS scheitert
Dies ist kein echter Live-Rundenticker. GitHub Actions läuft frühestens etwa alle fünf Minuten, GitHub Pages kann zusätzlich verzögert sein. Der Job kann ebenfalls scheitern, falls BO3.gg den Zugriff blockiert.

1. Zusätzlich `fetch_matches.py` und `.github/workflows/matches.yml` hochladen (Ordnerstruktur beibehalten).
2. Settings → Actions → General → Workflow permissions: Read and write permissions (sofern erforderlich). Unter Actions den Workflow `BO3 match cache (optional)` manuell starten.
3. Nach erfolgreichem Lauf enthält das Repository `matches.json`. Prüfe, ob diese Datei unter deiner Pages-URL verfügbar ist.
4. Falls Pages nach dem Bot-Commit nicht neu deployt (GITHUB_TOKEN-Commits lösen dies nicht zuverlässig aus), nutze den alternativen Abruf der Cache-Datei aus dem GitHub-Repository oder einen eigenen Pages-Deploy-Workflow. Diese Version enthält einen Abruf über raw.githubusercontent.com, wenn die Seite auf github.io liegt; alternativ lässt sich `cache=...` setzen.
5. In OBS die URL `?source=github` verwenden. Den Workflow nach dem Major deaktivieren. Die Cron-Termine wiederholen sich jährlich.

Quelle: https://github.com/tommhe14/CS2API (Endpunkte) und https://bo3.gg/ (Daten). Kein offizielles PGL-Produkt.
