import subprocess

wifi_data = {
    "wifi_networks": [
        {
            "id": 1,
            "ssid": "CIT-Campus",
            "password": "CIT@#&2104"
        },
        {
            "id": 2,
            "ssid": "CITAR",
            "password": "CITAR@123."
        },
        {
            "id": 3,
            "ssid": "pothigai hostel",
            "password": "Pothigai@$C%I$T"
        },
        {
            "id": 4,
            "ssid": "BOYS HOSTEL",
            "password": "citchennai@24"
        }
    ]
}

def get_all_nearby_ssids():
    """Returns a list of all nearby SSIDs."""
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'], text=True)
        ssids = set()
        for line in output.splitlines():
            if "SSID" in line and "BSSID" not in line:
                ssid = line.split(":", 1)[1].strip()
                if ssid:
                    ssids.add(ssid)
        return list(ssids)
    except subprocess.CalledProcessError as e:
        print(f"Error running netsh command: {e}")
        return []

def get_ssid_password_matches(wifi_db):
    """Returns list of dictionaries with matching SSID and password from known wifi_db."""
    nearby_ssids = get_all_nearby_ssids()
    matched = []
    for ssid in nearby_ssids:
        for net in wifi_db["wifi_networks"]:
            if net["ssid"].strip().upper() == ssid.strip().upper():
                matched.append({
                    "ssid": ssid,
                    "id": net["id"],
                    "password": net["password"]
                })
                break
    return matched

if __name__ == "__main__":
    # Show all SSIDs
    print("Nearby SSIDs:")
    for ssid in get_all_nearby_ssids():
        print(f"- {ssid}")

    print("\nMatching SSIDs with Passwords:")
    matches = get_ssid_password_matches(wifi_data)
    for net in matches:
        print(f'- {net["ssid"]} (ID: {net["id"]}, Password: {net["password"]})')
