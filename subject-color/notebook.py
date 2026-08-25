import marimo

__generated_with = "0.24.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import plotly.express as px
    from plotly.subplots import make_subplots

    return make_subplots, mo, pd, px


@app.cell
def _(pd):
    df = pd.read_csv('schoolsubjects.csv', index_col=0)
    df.index.name = 'Initial'
    df
    return (df,)


@app.cell
def _(px):
    def notebook_vis(subject, source_df):
        subject = str.lower(subject)
        subject_counts = source_df[str(subject).capitalize()].value_counts()
        color_map = {
            "red": "#ED2F39",
            "blue": "#0487D7",
            "green": "#5BB515",
            "yellow": "#DACF00",
            "purple": "#5B45B0",
            "orange": "#D47D3B",
            "black": "#3B423D",
            "white": "#E4E4E4",
        }
        fig = px.treemap(
            subject_counts,
            path=[subject_counts.index],
            values=subject_counts.values,
            color=subject_counts.index,
            custom_data=[subject_counts.index.str.capitalize()],
            color_discrete_map=color_map,
            width=425,
            height=550,
        )
        fig.update_traces(
            tiling=dict(pad=0),
            marker=dict(line=dict(width=0)),
            pathbar=dict(visible=False),
            maxdepth=1,
            textinfo='none',
            hovertemplate=(
                "<b>%{customdata[0]}</b><br>"
                "Votes: %{value}<br>"
                "Share: %{percentParent:.1%}"
                "<extra></extra>"
            ),
        )
        fig.add_annotation(
            text=str(subject).capitalize(),
            showarrow=False,
            font=dict(family='Ink Free', size=50, color='black'),
        )
        return fig


    return (notebook_vis,)


@app.cell
def _(df, make_subplots, mo, notebook_vis):
    subjects = ['math', 'english', 'science', 'history']

    def prettify_notebooks(df):
        figs = [notebook_vis(subject, df) for subject in subjects]
        spacing = 0.025
        subplot_width = (1 - spacing * (len(figs) - 1)) / len(figs)

        fig = make_subplots(
            rows=1,
            cols=len(figs),
            specs=[[{'type': 'domain'}] * len(figs)],
            horizontal_spacing=spacing,
        )

        for position, (subject, plot) in enumerate(zip(subjects, figs), start=1):
            fig.add_trace(plot.data[0], row=1, col=position)
            left_edge = (position-1) * (subplot_width + spacing)
            center = subplot_width / 2 + left_edge

            fig.add_annotation(
                text=subject.capitalize(),
                y=.9,
                x=center,
                xref='paper',
                yref='paper',
                yanchor='top',
                xanchor='center',
                align='center',
                showarrow=False,
                font=dict(family='Ink Free', size=30, color='black', weight='bold'),
            )

            oval_width = 0.018
            oval_height = 0.03
            oval_x = left_edge + .002

            for oval_number in range(46):
                oval_center_y = .04 + oval_number * 0.0195

                fig.add_shape(
                    type="circle",
                    x0=oval_x,
                    x1=oval_x + oval_width,
                    y0=oval_center_y - oval_height / 2,
                    y1=oval_center_y + oval_height / 2,
                    xref="paper",
                    yref="paper",
                    line=dict(color="#333333", width=1),
                )

        fig.update_layout(
            width=1000,
            height=400,
            paper_bgcolor='white',
            plot_bgcolor='white',
            margin=dict(t=40, l=20, r=20, b=10),
            showlegend=False,
            title='Main Tank Subject Colors'
        )
        return fig
    
    # fig.write_html('MT School Subject Colors.html')

    interactive_fig = mo.ui.plotly(prettify_notebooks(df))
    interactive_fig
    return interactive_fig, prettify_notebooks, subjects


@app.cell
def _(interactive_fig, subjects):
    selection = interactive_fig.value
    if selection:
        clicked = selection[0]
        subject_name = subjects[clicked['curveNumber']].capitalize()
        color= clicked['label']
    else:
        subject_name = None
        color = None

    subject_name, color
    return color, subject_name


@app.cell
def _(color, df, subject_name):
    if subject_name and color:
        filtered_df = df[df[subject_name] == color]
    else:
        filtered_df = df

    filtered_df
    return (filtered_df,)


@app.cell
def _(filtered_df, prettify_notebooks):
    prettify_notebooks(filtered_df)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
