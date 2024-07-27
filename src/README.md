# Arbeitsweise der App

## App Klasse
Die `App.py` Datei enthält die Definition der `App` Klasse, die eine FastAPI Anwendung repräsentiert. Die Initialisierung der Komponenten erfolgt in der `__init__` Methode und den entsprechenden Hilfsmethoden.

1. **Initialisierung der App**: Bei der Initialisierung der `App` Klasse werden der Name der Anwendung, die Controller, Services, Repositories und Entities als Parameter übergeben. Ein FastAPI Objekt wird erstellt und das Logging wird konfiguriert.

2. **Initialisierung der Controller**: Die Methode `_init_controller` initialisiert alle Controller, die in der App registriert sind. Jeder Controller in der Liste wird instanziiert und mit der App als Parameter initialisiert.

3. **Initialisierung der Repositories**: Die Methode `_init_repositories` initialisiert alle Repositories, die in der App registriert sind. Jedes Repository in der Liste wird instanziiert und mit der App als Parameter initialisiert.

4. **Initialisierung der Services**: Die Methode `_init_services` initialisiert alle Services, die in der App registriert sind. Jeder Service in der Liste wird instanziiert und mit der App als Parameter initialisiert.

Zusätzlich bietet die `App` Klasse Methoden zum Abrufen von initialisierten Repository- und Service-Objekten. Die Methoden `get_repository` und `get_service` geben ein initialisiertes Repository bzw. Service Objekt zurück, wenn es in der App registriert ist. Andernfalls geben sie `None` zurück.

Diese werden verwendet, um die initialisierten Objekte an die Controller und Services weiterzugeben.
