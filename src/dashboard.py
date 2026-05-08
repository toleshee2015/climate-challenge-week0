import streamlit as st
        filtered_df = filter_obj.filter_by_year(
            "year",
            selected_year,
        )

        # Custom User Parameters
        st.sidebar.header("Custom Analysis")

        numeric_columns = filtered_df.select_dtypes(include="number").columns

        x_axis = st.sidebar.selectbox(
            "Select X-axis",
            numeric_columns,
        )

        y_axis = st.sidebar.selectbox(
            "Select Y-axis",
            numeric_columns,
        )

        chart_type = st.sidebar.selectbox(
            "Select Chart Type",
            ["Line", "Bar", "Scatter"],
        )

        stats = ClimateStatistics(filtered_df)

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Avg Temperature",
            f"{stats.average_temperature()} °C",
        )

        col2.metric(
            "Max Temperature",
            f"{stats.max_temperature()} °C",
        )

        col3.metric(
            "Min Temperature",
            f"{stats.min_temperature()} °C",
        )

        col4.metric(
            "Temp Range",
            f"{stats.temperature_range()} °C",
        )

        visualizer = ClimateVisualizer(filtered_df)

        if chart_type == "Line":
            fig = visualizer.line_chart(x_axis, y_axis, "Climate Trend")

        elif chart_type == "Bar":
            fig = visualizer.bar_chart(x_axis, y_axis, "Climate Trend")

        else:
            fig = visualizer.scatter_chart(x_axis, y_axis, "Climate Trend")

        st.plotly_chart(fig, use_container_width=True)

        # Display raw data
        with st.expander("View Dataset"):
            st.dataframe(filtered_df)
