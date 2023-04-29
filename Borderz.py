import struct
import json

data = []
l = 0

with open("borders.geojson", "r", encoding="utf-8") as f:
    geojson = json.loads(f.read())

    for feature in geojson["features"]:
        line = struct.pack("h", len(feature["geometry"]["coordinates"]))

        for coordinate in feature["geometry"]["coordinates"]:
            line += struct.pack("ff", coordinate[0], coordinate[1])

        data.append(line)

with open("Python/Earth/Alps/Mesh/Borders.bin", "wb") as f:
    f.write(b"".join(data))