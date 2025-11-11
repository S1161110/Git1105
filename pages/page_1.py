import solara
import leafmap.leafmap as leafmap

@solara.component
def Page():
    # 建立地圖，以台北為中心
    m = leafmap.Map(
        center=(25.0330, 121.5654),  # 台北 101 附近
        zoom=12,
        basemap="CartoDB.DarkMatter"  # 暗色底圖
    )

    # 載入台北捷運路網（GeoJSON）
    url = "https://raw.githubusercontent.com/leoluyi/taipei_mrt/refs/heads/master/routes.geojson"
    m.add_geojson(url, layer_name="台北捷運")

    # ✅ 在 Solara 中顯示地圖
    return solara.Display(m)
