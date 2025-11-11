import solara


@solara.component
def Page():
    with solara.Column(align="center"):
        markdown = """
        ## 3D Mapping with Leafmap and MapLibre

        #S1161110王筱涵 台北GIS儀表板

        This is a Solara template for a 3D mapping application using Leafmap and MapLibre. Click on the menu above to see the different examples.
        <br>
        """

        solara.Markdown(markdown)