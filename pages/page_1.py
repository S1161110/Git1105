import solara
import leafmap.leafmap as leafmap

@solara.component
def Page():
    m = leafmap.Map(center=(25.033, 121.5654), zoom=12, basemap="CartoDB.DarkMatter")
    url = "https://raw.githubusercontent.com/datasets/taipei-metro/master/data/taipei_metro_lines.geojson"
    m.add_geojson(url, layer_name="台北捷運")
    return m