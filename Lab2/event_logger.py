from datetime import datetime


def record_event(percepts):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[{time_now}] SENSOR READING")
    print(f"  Temperature: {percepts['temperature']} °C")
    print(f"  Smoke Level: {percepts['smoke_level']}")
    print(f"  Damage Severity: {percepts['damage_severity']}")
    print("-" * 35)
