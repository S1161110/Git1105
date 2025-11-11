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

    metro_url="https://github.com/leoluyi/taipei_mrt/blob/master/routes.geojson"

    m.add_pmtiles(
        building_pmtiles, style=building_style, tooltip=True, fit_bounds=False
    )
    m.add_pmtiles(road_pmtiles, style=road_style, tooltip=True, fit_bounds=False)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()