import pygame
from sys import exit
import random

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

player1 = pygame.Surface((40, 100))
player1.fill("red")
player1_x = 50
player1_y = 200
player1_count = 0

player2 = pygame.Surface((40, 100))
player2.fill("green")
player2_x = 1150
player2_y = 200
player2_count = 0
ai_speed = 5
    

ball = pygame.Surface((20, 20))
ball.fill("white")
ball_x = 590
ball_y = 290
ball_speed_x = random.choice([5, -5])
ball_speed_y = random.choice([5, -5])

# Lade Hintergrundmusik und Soundeffekte
# background_music = pygame.mixer.Sound("sounds/summer.mp3")
paddle_hit_sound = pygame.mixer.Sound('sounds/paddle.wav')
goal_sound = pygame.mixer.Sound("sounds/goal.mp3")

running = False
start_game = False
modus = True
difficulty_selected = True
winner = False
goals = 3

# Start Bildschirm
while not start_game:
    # Mit dem X auf der rechten oberen Seite kann das Spiel geschlossen werden
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Abfrage ob das Spiel im Einzelspielermodus oder Zweispielermodus gestartet werden soll
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        start_game = True
        modus = True
        difficulty_selected = False

    elif keys[pygame.K_2]:
        start_game = True
        modus = False

    # Ausfüllen des Start Bildschirms
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    text = font.render("Spiel im Einzelspielermodus oder im Zweispielermodus starten? Drücken Sie 1 oder 2", True, (255, 255, 255))
    screen.blit(text, (50, 300))

    pygame.display.update()
    clock.tick(60)

# Schwierigkeitsauswahl Bildschirm
while not difficulty_selected:
    # Mit dem X auf der rechten oberen Seite kann das Spiel geschlossen werden
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Ausfüllen des Schwierigkeitsauswahl Bildschirms
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    difficulty_text = font.render("Wählen Sie den Schwierigkeitsgrad aus: Easy = e, medium = m, hard = h", True, (255, 255, 255))
    screen.blit(difficulty_text, (50, 300))

    pygame.display.update()
    clock.tick(60)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_e]:
        difficulty_selected = True
        difficulty = "easy"
    elif keys[pygame.K_m]:
        difficulty_selected = True
        difficulty = "medium"
    elif keys[pygame.K_h]:
        difficulty_selected = True
        difficulty = "hard"

    pygame.display.update()
    clock.tick(60)

# Spiele Bildschirm
while winner == False:
    # Mit dem X auf der rechten oberen Seite kann das Spiel geschlossen werden
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            exit()

    # Eingabe von Spieler 1 und Spieler 2
    # Spieler 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y -= 5
        running = True
    if keys[pygame.K_s]:
        player1_y += 5
        running = True

    # Spieler 2
    if keys[pygame.K_UP] and modus == False:
        player2_y -= 5
        running = True
    if keys[pygame.K_DOWN] and modus == False:
        player2_y += 5
        running = True
    
    # KI-Bewegungssteuerung
    if ball_speed_x > 0 and modus == True:
        if difficulty == "easy":
            # Einfache KI: Die KI bewegt sich langsam in Richtung des Balls
            if ball_y < player2_y + player2.get_height() / 2:
                player2_y -= ai_speed
            elif ball_y > player2_y + player2.get_height() / 2:
                player2_y += ai_speed
        elif difficulty == "medium":
            # Mittlere KI: Die KI bewegt sich schneller in Richtung des Balls
            if ball_y < player2_y + player2.get_height() / 2:
                player2_y -= ai_speed * 1.5
            elif ball_y > player2_y + player2.get_height() / 2:
                player2_y += ai_speed * 1.5
        elif difficulty == "hard":
            # Schwere KI: Die KI bewegt sich sehr schnell in Richtung des Balls
            if ball_y < player2_y + player2.get_height() / 2:
                player2_y -= ai_speed * 2
            elif ball_y > player2_y + player2.get_height() / 2:
                player2_y += ai_speed * 2


    # Grenzen für die Spielfiguren unten und oben
    player1_y = max(0, min(screen.get_height() - player1.get_height(), player1_y))
    player2_y = max(0, min(screen.get_height() - player2.get_height(), player2_y))

    # background_music.play()
    # background_music.set_volume(0.01)

    # Ball bewegt sich solange bis ein Tor erzielt wurde
    if running == True:
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        if ball_x <= 0:
            goal_sound.play()
            goal_sound.set_volume(0.5)
            player2_count += 1
            ball_x = 590
            ball_y = 290
            player1_y = 200
            player2_y = 200
            ball_speed_x = random.choice([5, -5])
            ball_speed_y = random.choice([5, -5])
            running = False

        if ball_x + ball.get_width() >= screen.get_width():
            player1_count += 1
            goal_sound.play()
            goal_sound.set_volume(0.5)
            ball_x = 590
            ball_y = 290
            player1_y = 200
            player2_y = 200
            ball_speed_x = random.choice([5, -5])
            ball_speed_y = random.choice([5, -5])
            running = False

    # Grenzen für den Ball unten und oben
    if ball_y <= 0 or ball_y + ball.get_height() >= screen.get_height():
        ball_speed_y *= -1

    # Collisionsabfragen
    player1_rect = pygame.Rect(player1_x, player1_y, player1.get_width(), player1.get_height())
    player2_rect = pygame.Rect(player2_x, player2_y, player2.get_width(), player2.get_height())
    ball_rect = pygame.Rect(ball_x, ball_y, ball.get_width(), ball.get_height())

    if ball_rect.colliderect(player1_rect) and ball_speed_x < 0:
        ball_speed_x *= -1.1
        paddle_hit_sound.play()
        paddle_hit_sound.set_volume(0.5)
        
    if ball_rect.colliderect(player2_rect) and ball_speed_x > 0:
        ball_speed_x *= -1.1
        paddle_hit_sound.play()
        paddle_hit_sound.set_volume(0.5)

    # Ausfüllen des Bildschirms (Schwarz)
    screen.fill((0, 0, 0))

    # Um den Text in ein Surface umzuwandeln und anzuzeigen:
    player1_count_text = font.render(f"Player 1: {player1_count}", True, (255, 255, 255))
    player2_count_text = font.render(f"Player 2: {player2_count}", True, (255, 255, 255))

    # Die Zähler anzeigen
    screen.blit(player1_count_text, (300, 10))
    screen.blit(player2_count_text, (900, 10))

    # Spieler und Ball anzeigen
    screen.blit(player1, (player1_x, player1_y))
    screen.blit(player2, (player2_x, player2_y))
    screen.blit(ball, (ball_x, ball_y))

    if player1_count == goals or player2_count == goals:
        winner = True

    pygame.display.update()
    clock.tick(60)

    # Abfrage, ob die Spieler nochmal spielen wollen
    while winner == True:
        # Mit dem X auf der rechten oberen Seite kann das Spiel geschlossen werden
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Ausfüllen des Bildschirms (Schwarz)
        screen.fill((0, 0, 0))
        if player1_count == goals:
            font = pygame.font.Font(None, 50)
            player1_count_text = font.render("Spieler 1 hat gewonnen", True, (255, 255, 255))
            screen.blit(player1_count_text, (400, 200))
        
        if player2_count == goals:
            font = pygame.font.Font(None, 50)
            player2_count_text = font.render("Spieler 2 hat gewonnen", True, (255, 255, 255))
            screen.blit(player2_count_text, (400, 200))

        font = pygame.font.Font(None, 36)
        play_again_text = font.render("Möchten Sie noch einmal spielen? Ja = J, Nein = N", True, (255, 255, 255))
        screen.blit(play_again_text, (300, 400))

        pygame.display.update()
        clock.tick(60)

        # Stelle sicher, dass die Tastaturereignisse für die Neustartabfrage richtig verarbeitet werden
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    winner = False
                    player1_count = 0
                    player2_count = 0
                    ball_x = 590
                    ball_y = 290
                    player1_y = 200
                    player2_y = 200
                    ball_speed_x = random.choice([5, -5])
                    ball_speed_y = random.choice([5, -5])
                elif event.key == pygame.K_n:
                    pygame.quit()
                    exit()



# Aufgaben

# Erledigt: Soundeffekte: Füge dem Spiel Soundeffekte hinzu, z.B. wenn der Ball auf das Paddle trifft oder ein Tor erzielt wird.

# Erledigt: Schwierigkeitsstufen: Füge verschiedene Schwierigkeitsstufen für die KI hinzu, indem du die Geschwindigkeit der KI anpasst oder ihre Entscheidungsfindungsalgorithmen änderst.

# Erledigt: Anzeige von Gewinnern: Zeige eine Benachrichtigung an, wenn ein Spieler eine bestimmte Anzahl von Toren erzielt hat und das Spiel gewinnt.

# Pause- und Starttaste: Füge eine Taste hinzu, um das Spiel zu pausieren und fortzusetzen.

# Verbesserte Kollisionsabfrage: Verfeinere die Kollisionsabfrage, um realistischere Abprallwinkel zu erzeugen, wenn der Ball auf Paddles trifft.

# Hintergrundmusik: Füge dem Spiel Hintergrundmusik hinzu, um die Spielerfahrung zu verbessern.

# Verbesserte Grafiken: Ersetze einfache geometrische Formen durch ansprechendere Grafiken für Spieler, Ball und Hintergrund.

# Spielende und Neustart: Implementiere eine Funktion, um das Spiel zu beenden oder neu zu starten, wenn ein Spieler eine bestimmte Anzahl von Toren erzielt hat.

# Besseres GUI: Erstelle ein ansprechendes GUI für den Startbildschirm und d