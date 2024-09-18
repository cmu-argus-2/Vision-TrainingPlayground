from poliastro.czml.extract_czml import CZMLExtractor

from poliastro.examples import molniya

start_epoch = molniya.epoch
end_epoch = molniya.epoch + molniya.period
N = 80

extractor = CZMLExtractor(start_epoch, end_epoch, N)

extractor.add_orbit(
    molniya,
    id_name="MolniyaOrbit",
    path_width=2,
    label_text="Molniya",
    label_fill_color=[125, 80, 120, 255],
    groundtrack_show=True,
    groundtrack_lead_time=20,
    groundtrack_trail_time=20,
)

# extractor = CZMLExtractor(start_epoch, end_epoch, N, scene3D=False)
# html_info = extractor.packets
# print(html_info)
# import pdb; pdb.set_trace()

packets = extractor.packets  # This gets the CZML packets
print(packets)

czml_filename = "molniya_orbit.czml"

doc = czml.CZML()
for packet in packets:
    doc.packets.append(packet)
doc.write(czml_filename)