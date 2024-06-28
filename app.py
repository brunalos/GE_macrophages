from pathlib import Path
import pandas as pd
import plotly.express as px
from shiny import App, Inputs, Outputs, Session, render, ui, reactive
from shiny.express import ui, render, input
from shinywidgets import render_plotly

# Set up UI options

ui.page_opts(title="Gene Expression", fillable=True)
ui.page_opts(fillable=True, id="page")


# Read the file
@reactive.calc
def dataframe():
    infile = Path(__file__).parent / "data/GE.csv"
    return pd.read_csv(infile)


