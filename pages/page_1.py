import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="dark-matter",
        projection="globe",
        height="750px",
        center=[25.03, 121.56],
        zoom=12,
        sidebar_visible=True,
    )

    stations_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/stations.geojson"
    road_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/routes.geojson"

    # 加站點（circle）
    m.add_geojson(
        stations_url,
        layer_name="stations",
        style={
            "circle-color": "#ff0000",
            "circle-radius": 5,
        },
        tooltip_property="NAME",
        fit_bounds=True
    )

    # 加路線（線）
    m.add_geojson(
        road_url,
        layer_name="roads",
        style={
            "line-color": "#ffffff",
            "line-width": 2,
        },
        fit_bounds=False
    )

    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
