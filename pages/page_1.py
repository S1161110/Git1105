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
    stations_style = {
        "layers": [
            {
                "id": "stations",
                "source": "stations",
                "type": "circle",
                "paint": {
                    "line-color": "#ff0000",
                    "line-width": 5,
                },
            },
        ]
    }
    road_style = {
        "layers": [
            {
                "id": "roads",
                "source": "roads",
                "type": "line",
                "paint": {
                    "line-color": "#ffffff",
                    "line-width": 2,
                },
            },
        ]
    }
    m.add_geojson(stations_style, style=stations_style, tooltip=True, fit_bounds=False)
    m.add_geojson(road_style, style=road_style, tooltip=True, fit_bounds=False)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()