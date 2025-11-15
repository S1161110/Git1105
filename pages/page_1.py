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

    # 加入捷運站點（Point）
    m.add_geojson(
        stations_url,
        name="stations",
        layer_type="circle",
        paint={
            "circle-color": "#ff0000",
            "circle-radius": 5,
        },
        zoom_to_data=True,
    )

    # 加入捷運路線（LineString）
    m.add_geojson(
        road_url,
        name="roads",
        layer_type="line",
        paint={
            "line-color": "#ffffff",
            "line-width": 2,
        },
        zoom_to_data=False,
    )

    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
