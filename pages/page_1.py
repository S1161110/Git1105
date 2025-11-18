import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="dark-matter",
        projection="globe",
        height="750px",
        center=[121.56, 25.03],  # 台北
        zoom=12,
        sidebar_visible=True,
    )

    stations_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/stations.geojson"
    road_url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/master/routes.geojson"

    # 捷運站點 (Point)
    m.add_geojson(
        data=stations_url,
        name="stations",
        layer_type="circle",
        paint={
            "circle-color": "#ff0000",
            "circle-radius": 5,
        },
    )

    # 捷運路線 (LineString)
    m.add_geojson(
        data=road_url,
        name="roads",
        layer_type="line",
        paint={
            "line-color": "#ffffff",
            "line-width": 2,
        },
    )

    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
