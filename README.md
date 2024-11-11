# Flappy Bird - README

## Projektbeschreibung

Dieses Python-Skript ist ein einfaches "Flappy Bird"-Spiel, das mit der `pygame`-Bibliothek erstellt wurde. Der Spieler steuert einen Vogel, der Hindernissen (Rohren) ausweichen muss, indem er durch Drücken der Leertaste den Vogel zum Springen bringt. Das Ziel des Spiels ist es, so viele Punkte wie möglich zu sammeln, indem man den Hindernissen ausweicht, ohne den Vogel abstürzen zu lassen.

## Voraussetzungen

- Python 3.x
- `pygame`-Bibliothek (`pip install pygame`)

## Installation

1. Stellen Sie sicher, dass Python installiert ist.
2. Installieren Sie `pygame` mit folgendem Befehl:

    ```bash
    pip install pygame
    ```

3. Führen Sie das Skript aus:

    ```bash
    python flappy_bird.py
    ```

## Spielanleitung

- Drücken Sie die Leertaste, um den Vogel springen zu lassen.
- Der Vogel wird durch die Schwerkraft automatisch nach unten gezogen.
- Weichen Sie den Hindernissen aus, um Punkte zu sammeln.
- Wenn der Vogel mit einem Hindernis oder dem oberen/unteren Bildschirmrand kollidiert, endet das Spiel.

## Codeübersicht

### 1. Spielvariablen

- Bildschirmgrößen und Farben werden definiert.
- Spielparameter wie Schwerkraft, Sprungstärke und Geschwindigkeit der Hindernisse sind ebenfalls festgelegt.

### 2. `Bird`-Klasse

- Definiert den Vogel, seine Bewegung und sein Verhalten.
  - `jump`: Setzt die Geschwindigkeit des Vogels, um einen Sprung auszulösen.
  - `move`: Aktualisiert die Position des Vogels durch Hinzufügen von Schwerkraft.
  - `draw`: Zeichnet den Vogel auf dem Bildschirm.

### 3. `Pipe`-Klasse

- Erstellt Hindernisse und steuert deren Bewegung.
  - `move`: Bewegt die Hindernisse von rechts nach links.
  - `draw`: Zeichnet die Hindernisse (Rohre) auf dem Bildschirm.

### 4. `main`-Funktion

- Die Hauptspielschleife, in der das Spiel gesteuert wird:
  - Ereignisbehandlung: Überwacht Tastenanschläge und schließt das Spiel, wenn es beendet wird.
  - Bewegung und Zeichnung: Aktualisiert die Position des Vogels und der Hindernisse und zeichnet sie auf dem Bildschirm.
  - Punktzahl: Aktualisiert die Punktzahl, wenn ein Hindernis erfolgreich umgangen wurde.
  - Kollisionserkennung: Beendet das Spiel, wenn der Vogel ein Hindernis oder den Bildschirmrand berührt.

### Steuerung des Spiels

- Leertaste (`Space`): Lässt den Vogel springen.
- ESC oder `X`: Schließt das Spielfenster.

## Anpassungen

- **Größe und Geschwindigkeit** der Hindernisse und des Vogels können über die Variablen `PIPE_VELOCITY`, `BIRD_HEIGHT`, `BIRD_WIDTH` usw. modifiziert werden.
- **Schwierigkeit**: Erhöhen Sie die `PIPE_VELOCITY` oder verringern Sie den `PIPE_GAP`, um das Spiel schwieriger zu gestalten.

## Lizenz

Dieses Projekt ist zu Übungszwecken erstellt und kann frei modifiziert und verteilt werden.
