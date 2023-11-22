def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        if heures == 0:
            if minutes == 1:
                return f"{minutes} minute"
            else:
                return f"{minutes} minutes"
        elif heures == 1:
            if minutes_restantes == 0:
                return f"{heures} heure"
            elif minutes_restantes == 1:
                return f"{heures} heure et {minutes_restantes} minute"
            else:
                return f"{heures} heure et {minutes_restantes} minutes"
        else:
            if minutes_restantes == 0:
                return f"{heures} heures"
            elif minutes_restantes == 1:
                return f"{heures} heures et {minutes_restantes} minute"
            else:
                return f"{heures} heures et {minutes_restantes} minutes"

print(time_to_text(75))
