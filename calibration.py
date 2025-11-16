from machine import Pin, PWM
from Traducteur_servo import traduit
import time

# --- Initialisation des servos ---
servo_epaule = PWM(Pin(0))
servo_epaule.freq(50)

servo_coude = PWM(Pin(1))
servo_coude.freq(50)

def move_servo(servo, angle):
    servo.duty_u16(traduit(angle))
    time.sleep(0.05)

# --- Angles de départ ---
angle_epaule = 90
angle_coude = 90

print("=== MODE CALIBRATION ===")
print("Commandes :")
print("  s+ / s- : epaule (+5° / -5°)")
print("  e+ / e- : coude  (+5° / -5°)")
print("  q       : quitter")
print("----------------------------")

move_servo(servo_epaule, angle_epaule)
move_servo(servo_coude, angle_coude)

# --- Boucle de calibration ---
while True:
    cmd = input("Commande : ").strip()

    if cmd == "s+":
        angle_epaule = min(angle_epaule + 5, 180)
        move_servo(servo_epaule, angle_epaule)
        print("Epaule =", angle_epaule)

    elif cmd == "s-":
        angle_epaule = max(angle_epaule - 5, 0)
        move_servo(servo_epaule, angle_epaule)
        print("Epaule =", angle_epaule)

    elif cmd == "e+":
        angle_coude = min(angle_coude + 5, 180)
        move_servo(servo_coude, angle_coude)
        print("Coude =", angle_coude)

    elif cmd == "e-":
        angle_coude = max(angle_coude - 5, 0)
        move_servo(servo_coude, angle_coude)
        print("Coude =", angle_coude)

    elif cmd == "q":
        print("\nCalibration terminée.")
        print("Angles finaux :")
        print("  epaule =", angle_epaule)
        print("  coude  =", angle_coude)
        break

    else:
        print("Commande invalide.")
