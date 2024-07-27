# Aktivieren und Deaktivieren der virtuellen Umgebung (venv)

Dieses Repository verwendet Python's eingebaute `venv` Bibliothek, um eine isolierte Umgebung für dieses Projekt zu erstellen. Hier sind die Schritte, um die virtuelle Umgebung zu aktivieren und zu deaktivieren.

## Erstellen der virtuellen Umgebung

Um eine neue virtuelle Umgebung zu erstellen, führen Sie den folgenden Befehl in Ihrem Terminal aus:

```bash
python3 -m venv ./venv
```

Ersetzen Sie `/pfad/zur/venv` durch den Pfad, an dem Sie die virtuelle Umgebung erstellen möchten.

## Aktivieren der virtuellen Umgebung

### macOS

Aktivieren Sie die virtuelle Umgebung mit dem folgenden Befehl:

```bash
source ./venv/bin/activate
```

### Windows

Aktivieren Sie die virtuelle Umgebung mit dem folgenden Befehl:

```bash
./venv/Scripts/activate
```

## Deaktivieren der virtuellen Umgebung

Wenn Sie mit der Arbeit in der virtuellen Umgebung fertig sind, können Sie sie mit dem folgenden Befehl deaktivieren:

```bash
deactivate
```

Bitte beachten Sie, dass Sie die virtuelle Umgebung jedes Mal aktivieren müssen, wenn Sie darin arbeiten möchten.

# Abhängigkeiten und Starten der Anwendung

## Abhängigkeiten setzen

Sollten weitere Pakete verwendet werden, können diese in einer `requirements.txt` Datei gespeichert werden. Dies ist notwendig, damit andere Entwickler mit denselben Paketen und Versionen arbeiten können. Um die aktuell verwendeten Pakete und Versionen zu speichern, führen Sie den folgenden Befehl aus:

```bash
pip freeze > requirements.txt
```

## Abhängigkeiten installieren

Alle notwendigen Pakete können über einen einfachen Befehl installiert werden:

```bash
pip install -r requirements.txt
```

## Anwendung starten

Es gibt viele verschiedene Parameter, die beim Starten im Production Mode relevant sind. Diese können auch in der Dokumentation nachgelesen werden. Im Development Modus kann die App mit dem folgenden Befehl gestartet werden:

```bash
uvicorn src.main:app --reload
```

## API-Visualiserung mit OpenAPI abrufen

Mit localhost:8000/docs abrufen
