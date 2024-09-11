# This file generated by Quarto; do not edit by hand.
# shiny_mode: core

from __future__ import annotations

from pathlib import Path
from shiny import App, Inputs, Outputs, Session, ui




def server(input: Inputs, output: Outputs, session: Session) -> None:
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    from shiny import render, reactive, ui
    from shinywidgets import render_widget, render_plotly

    data = px.data.gapminder().query("country == 'New Zealand'")

    # ========================================================================

    ui.input_select("value", "Value", choices=['lifeExp', 'pop', 'gdpPercap'], selected="pop")

    # ========================================================================

    @render_plotly
    def display_trend():
        value = input.value()
        fig = px.bar(data, x='year', y=value, title=f"New Zealand {value} by year")
        return fig

    # ========================================================================



    return None


_static_assets = ["index_files","index_files\\libs\\quarto-html\\tippy.css","index_files\\libs\\quarto-html\\quarto-syntax-highlighting.css","index_files\\libs\\bootstrap\\bootstrap-icons.css","index_files\\libs\\bootstrap\\bootstrap.min.css","index_files\\libs\\quarto-dashboard\\datatables.min.css","index_files\\libs\\clipboard\\clipboard.min.js","index_files\\libs\\quarto-html\\quarto.js","index_files\\libs\\quarto-html\\popper.min.js","index_files\\libs\\quarto-html\\tippy.umd.min.js","index_files\\libs\\quarto-html\\anchor.min.js","index_files\\libs\\bootstrap\\bootstrap.min.js","index_files\\libs\\quarto-dashboard\\quarto-dashboard.js","index_files\\libs\\quarto-dashboard\\stickythead.js","index_files\\libs\\quarto-dashboard\\datatables.min.js","index_files\\libs\\quarto-dashboard\\pdfmake.min.js","index_files\\libs\\quarto-dashboard\\vfs_fonts.js","index_files\\libs\\quarto-dashboard\\web-components.js","index_files\\libs\\quarto-dashboard\\components.js"]
_static_assets = {"/" + sa: Path(__file__).parent / sa for sa in _static_assets}

app = App(
    Path(__file__).parent / "index.html",
    server,
    static_assets=_static_assets,
)
