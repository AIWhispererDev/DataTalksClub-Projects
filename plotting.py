import plotly.graph_objects as go
import streamlit as st

def generate_plot(data):
    try:
        wordcloud = analysis.generate_wordcloud(data['processed_titles'])
        st.image(wordcloud.to_array(), use_column_width=True)
    except Exception as e:
        st.write("An error occurred while generating the word cloud.")
    #################################
        # Plot Top 10 Most Frequent Project Titles
        ################################

        try:
            # Initialize Plotly figure for the horizontal bar chart
            fig = go.Figure()

            # Add Bar chart
            fig.add_trace(
                go.Bar(
                    x=top_titles,
                    y=top_titles.index,
                    orientation='h',
                    marker=dict(color='#B53158', line=dict(color='black', width=1)),
                    hoverinfo='y+x',
                )
            )
            fig.update_layout(
                title='Top 10 Most Frequent Project Titles',
                xaxis_title='Frequency',
                yaxis_title='Project Titles',
                yaxis=dict(autorange="reversed"),
            )
            # Show Plotly figure
            st.plotly_chart(fig)
        except Exception as e:
            st.write(
                "An error occurred while plotting the most frequent project titles."
            )

        #################################
        # Plot Top 10 Most Frequent Words in Project Titles
        ################################
        try:
            # Initialize Plotly figure for the bar chart
            fig = go.Figure()

            # Add Bar chart
            fig.add_trace(
                go.Bar(
                    x=top_words.index,
                    y=top_words,
                    marker=dict(color='#B53158', line=dict(color='black', width=1)),
                    hoverinfo='x+y',
                )
            )
            fig.update_layout(
                title='Top 10 Most Frequent Words in Project Titles',
                xaxis_title='Words',
                xaxis=dict(tickangle=-45),
                yaxis_title='Frequency',
            )
            # Show Plotly figure
            st.plotly_chart(fig)
        except Exception as e:
            st.write("An error occurred while plotting the most frequent words.")

        #################################
        # Plot Deployment Type Distribution
        ################################
        try:
            # Initialize Plotly figure for the horizontal bar chart
            fig = go.Figure()

            # Add Horizontal Bar chart
            fig.add_trace(
                go.Bar(
                    x=deployment_types,
                    y=deployment_types.index,
                    orientation='h',  # Horizontal orientation
                    marker=dict(color='#B53158', line=dict(color='black', width=1)),
                    hoverinfo='x+y',
                )
            )
            fig.update_layout(
                title='Deployment Type Distribution',
                xaxis_title='Frequency',
                yaxis_title='Deployment Type',
                yaxis=dict(autorange="reversed"),  # Reverse the y-axis
            )
            # Show Plotly figure
            st.plotly_chart(fig)
        except Exception as e:
            st.write(
                "An error occurred while plotting the deployment type distribution."
            )

        #################################
        # Plot Cloud Provider Distribution
        ################################

        try:
            # Initialize Plotly figure for the bar chart
            fig = go.Figure()

            # Add Bar chart
            fig.add_trace(
                go.Bar(
                    x=cloud_provider_counts.index,
                    y=cloud_provider_counts,
                    marker=dict(color='#B53158', line=dict(color='black', width=1)),
                    hoverinfo='y+x',
                )
            )
            fig.update_layout(
                title='Cloud Provider Distribution',
                xaxis_title='Cloud Provider',
                yaxis_title='Frequency',
            )
            # Show Plotly figure
            st.plotly_chart(fig)
        except Exception as e:
            st.write(
                "An error occurred while plotting the cloud provider distribution."
            )

        ###################################################
        # Pie chart
        ###################################################

        # Initialize Plotly figure
        fig = go.Figure()
        # Add Pie chart
        fig.add_trace(
            go.Pie(
                labels=course_counts.index,
                values=course_counts,
                hole=0.8,
                rotation=90,
                marker=dict(colors=palette_colors),
                textinfo='label+percent',
                hoverinfo='label+value',
                insidetextorientation='radial',
            )
        )
        fig.update_layout(title='Distribution of Projects Across Different Courses')
        # Show Plotly figure
        st.plotly_chart(fig)

        #############################
        # Stacked bar chart Projects by Year and Course
        ######################

        # Pivot the data to get counts for each 'Year' and 'Course' combination
        year_course_counts = (
            data.groupby(['Year', 'Course']).size().reset_index(name='Counts')
        )
        pivot_year_course = year_course_counts.pivot(
            index='Year', columns='Course', values='Counts'
        ).fillna(0)

        # Initialize Plotly figure
        fig = go.Figure()
        edge_color = 'black'
        gap_height = 0.2
        # Initialize the bottom_value to zero
        bottom_value = np.zeros(len(pivot_year_course))
        annotations = []

        # Plotting the stacked bar chart
        for idx, course in enumerate(course_order):
            hover_text = [
                f"{course}: {count}" for count in pivot_year_course[course].tolist()
            ]
            fig.add_trace(
                go.Bar(
                    x=pivot_year_course.index,
                    y=pivot_year_course[course],
                    base=bottom_value,
                    name=course,
                    hovertext=hover_text,
                    hoverinfo="text+x",
                    marker=dict(
                        color=palette_colors[idx], line=dict(color=edge_color, width=1)
                    ),
                )
            )
            bottom_value = [
                sum(x) for x in zip(bottom_value, pivot_year_course[course].tolist())
            ]
            bottom_value = [x + gap_height for x in bottom_value]

        # Add annotations for the sum count
        for i, x_val in enumerate(pivot_year_course.index):
            annotations.append(
                dict(
                    x=x_val,
                    y=bottom_value[i],
                    xanchor='center',
                    yanchor='bottom',
                    xshift=0,
                    yshift=4,
                    text=str(int(bottom_value[i])),
                    showarrow=False,
                    font=dict(size=14),
                )
            )

        # Update layout
        fig.update_layout(
            barmode='stack',
            title='Projects by Year and Course',
            xaxis_title='Year',
            yaxis_title='Counts',
            annotations=annotations,
            xaxis=dict(
                tickvals=pivot_year_course.index,
                ticktext=[str(year) for year in pivot_year_course.index],
            ),
        )

        # Show Plotly figure in Streamlit
        st.plotly_chart(fig)

        #######################
        # Stacked bar chart Distribution in Different Clouds by Course
        ##################

        # Pivot the data to get counts for each 'Cloud' and 'Course' combination
        cloud_course_counts = (
            data.groupby(['Cloud', 'Course']).size().reset_index(name='Counts')
        )
        pivot_cloud_course = cloud_course_counts.pivot(
            index='Cloud', columns='Course', values='Counts'
        ).fillna(0)

        # Initialize Plotly figure
        fig = go.Figure()
        edge_color = 'black'
        gap_height = 0.2
        bottom_value = np.zeros(len(pivot_cloud_course))
        annotations = []
        # Plotting the stacked bar chart
        for idx, course in enumerate(course_order):
            hover_text = [
                f"{course}: {count}" for count in pivot_cloud_course[course].tolist()
            ]
            fig.add_trace(
                go.Bar(
                    x=pivot_cloud_course.index,
                    y=pivot_cloud_course[course],
                    base=bottom_value,
                    name=course,
                    hovertext=hover_text,
                    hoverinfo="text+x",
                    marker=dict(
                        color=palette_colors[idx], line=dict(color=edge_color, width=1)
                    ),
                )
            )
            bottom_value = [
                sum(x) for x in zip(bottom_value, pivot_cloud_course[course].tolist())
            ]
            bottom_value = [x + gap_height for x in bottom_value]

        # Add annotations
        for i, x_val in enumerate(pivot_cloud_course.index):
            annotations.append(
                dict(
                    x=x_val,
                    y=bottom_value[i],
                    xanchor='center',
                    yanchor='bottom',
                    xshift=0,
                    yshift=4,
                    text=str(int(bottom_value[i])),
                    showarrow=False,
                    font=dict(size=14),
                )
            )
        fig.update_layout(
            barmode='stack',
            title='Distribution in Different Clouds by Course',
            xaxis_title='Cloud',
            yaxis_title='Counts',
            annotations=annotations,
        )

        # Show Plotly figure
        st.plotly_chart(fig)

        ##########################
        # Stacked bar chart Distribution in Different Deployment Types by Course
        ###############################

        # Pivot the data to get counts for each 'Deployment Type' and 'Course' combination
        deployment_course_counts = (
            data.groupby(['Deployment Type', 'Course'])
            .size()
            .reset_index(name='Counts')
        )
        pivot_deployment_course = deployment_course_counts.pivot(
            index='Deployment Type', columns='Course', values='Counts'
        ).fillna(0)

        # Initialize Plotly figure
        fig = go.Figure()
        edge_color = 'black'
        gap_height = 0.2
        bottom_value = np.zeros(len(pivot_deployment_course))
        annotations = []

        # Plotting the stacked bar chart
        for idx, course in enumerate(course_order):
            hover_text = [
                f"{course}: {count}"
                for count in pivot_deployment_course[course].tolist()
            ]
            fig.add_trace(
                go.Bar(
                    x=pivot_deployment_course.index,
                    y=pivot_deployment_course[course],
                    base=bottom_value,
                    name=course,
                    hovertext=hover_text,
                    hoverinfo="text+x",
                    marker=dict(
                        color=palette_colors[idx], line=dict(color=edge_color, width=1)
                    ),
                )
            )
            bottom_value = [
                sum(x)
                for x in zip(bottom_value, pivot_deployment_course[course].tolist())
            ]
            bottom_value = [x + gap_height for x in bottom_value]

        # Add annotations
        for i, x_val in enumerate(pivot_deployment_course.index):
            annotations.append(
                dict(
                    x=x_val,
                    y=bottom_value[i],
                    xanchor='center',
                    yanchor='bottom',
                    xshift=0,
                    yshift=4,
                    text=str(int(bottom_value[i])),
                    showarrow=False,
                    font=dict(size=14),
                )
            )
        fig.update_layout(
            barmode='stack',
            title='Deployment Types by Course',
            xaxis_title='Deployment Type',
            yaxis_title='Counts',
            annotations=annotations,
        )

        # Show Plotly figure
        st.plotly_chart(fig)

        #############################