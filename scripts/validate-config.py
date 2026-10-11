#!/usr/bin/env python3
"""Validate the Config Server Git backend, demo profiles, decryption, and health."""

import json
from urllib.error import URLError
from urllib.request import urlopen

BASE_URL = "http://localhost:8888"
PROFILES = {
    "dev": {
        "salud.monto-copago-base": "50.00",
        "salud.descuento-eps": "0.80",
        "salud.api-key-aseguradora": "demo-api-key-dev-grupo5",
        "spring.datasource.password": "demo-db-password-dev-grupo5",
    },
    "prod": {
        "salud.monto-copago-base": "100.00",
        "salud.descuento-eps": "0.70",
        "salud.api-key-aseguradora": "demo-api-key-prod-grupo5",
        "spring.datasource.password": "demo-db-password-prod-grupo5",
    },
}


def get_json(path):
    with urlopen(f"{BASE_URL}{path}", timeout=15) as response:
        return json.load(response)


def merged_source(payload):
    source = {}
    for property_source in reversed(payload.get("propertySources", [])):
        source.update(property_source.get("source", {}))
    return source


def main():
    for profile, expected in PROFILES.items():
        payload = get_json(f"/cita-service/{profile}")
        source = merged_source(payload)
        for key, value in expected.items():
            if source.get(key) != value:
                raise SystemExit(
                    f"FAIL {profile}: {key} is missing, incorrect, or not decrypted"
                )
        print(f"PASS {profile}: GitHub properties loaded; demo secrets decrypted.")

    health = get_json("/actuator/health")
    if health.get("status") != "UP":
        raise SystemExit("FAIL Actuator health is not UP")
    print("PASS health: Config Server is UP.")


if __name__ == "__main__":
    try:
        main()
    except (URLError, TimeoutError, json.JSONDecodeError) as error:
        raise SystemExit(f"FAIL: could not validate Config Server: {error}")
