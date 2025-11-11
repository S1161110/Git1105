import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="CartoDB.DarkMatter",
        projection="mercator",
        height="750px",
        center=[25.0330, 121.5654],
        zoom=12,
        sidebar_visible=True,
    )

    metro_url="https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/routes.geojson"
    m.add_geojson(metro_url)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()