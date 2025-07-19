from mcp.server.fastmcp import FastMCP
import os
import subprocess
# Create an MCP server
mcp = FastMCP("College Wifi")


wifi_data ={
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

  
@mcp.tool()
def get_all_nearby_ssids():
    """Returns a list of all nearby SSIDs."""
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'], text=True)
        ssids = set()
        for line in output.splitlines():
            if "SSID" in line and "BSSID" not in line:
                ssid x= line.split(":", 1)[1].strip()
                if ssid:
                    ssids.add(ssid)
        return list(ssids)
    except subprocess.CalledProcessError as e:
        print(f"Error running netsh command: {e}")
        return []

@mcp.tool()
def get_wifi_password(ssid):
    """Returns the wifi password from the wifi_data."""
    for net in wifi_data["wifi_networks"]:
        if net["ssid"].strip().upper() == ssid.strip().upper():
            return net["password"]
    return "nerwork not found"
  
# @mcp.tool()
# def get_ssid_password_matches(wifi_db):
#     """Returns list of dictionaries with matching SSID and password from known wifi_data."""
#     nearby_ssids = get_all_nearby_ssids()
#     matched = []
#     for ssid in nearby_ssids:
#         for net in wifi_db["wifi_networks"]:
#             if net["ssid"].strip().upper() == ssid.strip().upper():
#                 matched.append({
#                     "ssid": ssid,
#                     "id": net["id"],
#                     "password": net["password"]
#                 })
#                 break
#     return matched
      