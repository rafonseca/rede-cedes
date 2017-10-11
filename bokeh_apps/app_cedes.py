from cedes_plots import main_app
whole_layout=main_app.get_whole_layout()

from bokeh.plotting import curdoc
curdoc().add_root(whole_layout)
