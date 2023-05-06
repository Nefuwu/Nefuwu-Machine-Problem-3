import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import math

st.set_page_config(page_title="Lagrange Interpolation", page_icon=":roller_coaster:")

def lagrange(x: list, y: list, p: float) -> float:

    # counts the length of the x
    n = len(x)

    # initializes value for the answer
    answer = 0.0000

    # Solving for the values of L(n)
    for i in range(n):
        basis_i = y[i]
        for j in range(n):
            # prevents division by zero when i = j
            if i != j:
                # term = term * following operations
                basis_i *= (p - x[j]) / (x[i] - x[j])          
        answer += basis_i
    return answer

tab1, tab2 = st.tabs(["Pre-defined", "User defined"])
with tab1:
    st.title("Lagrange Interpolation Calculator")
    st.write("---")

    # header and link for stocks
    st.write("<h2 style='text-align: center;'> SMI Corp. Stocks</h2>", unsafe_allow_html= True)
    st.markdown("<p style='text-align: center; font-size: 16px;'><a href='https://www.marketwatch.com/investing/stock/sm/charts?countrycode=ph&mod=mw_quote_advanced'>SMI Corp. Stocks</a>", unsafe_allow_html=True)
    

    # input data points
    x_input = st.text_input("Enter x-coordinates (comma-separated):", value = "1,2,3,6,7,8,9,10,13,14,15,16,17,20,21", disabled=True) 
    y_input = st.text_input("Enter y-coordinates (comma-separated):", value = "889.000,890.500,896.000,886.000,880.000,889.000,871.000,875.000,875.000,860.000,874.000,874.000,897.000,883.500,900.000", disabled=True)

    # input value to interpolate at
    p_input = st.text_input("Enter x-value to interpolate at:", value = 0)

    # convert inputs to lists of floats
    x = []
    y = []
    p = None

    # tries to execute the following codes unless(except) it detects an error
    try:
        x = [float(i) for i in x_input.split(",")]
        y = [float(i) for i in y_input.split(",")]
        p = float(p_input)
    except ValueError:
        st.error("Please enter a valid value.")

    # calculate and display the interpolated value at P(x)
    if st.button("Calculate") and p is not None:
        answer = lagrange(x, y, p)
        st.write("---")
        # add the interpolated point to the input data
        x.append(p)
        y.append(answer)
        # display the interpolated value
        st.markdown(f"<br>The interpolated value at P({p}) is <span style='color:green'>{answer}</span>", unsafe_allow_html=True)
   
    st.write("<h5 style='text-align: center;'> Month of March</h5>", unsafe_allow_html= True)
    # create a pandas DataFrame from the input data
    data = pd.DataFrame({
        'x': x,
        'y': y
    })

    # Define y-axis range
    y_range = (data['y'].min() - 0.1, data['y'].max() + 0.1)

    # create a chart
    chart = alt.Chart(data).mark_line().encode(
     # To specify the range of values to display on the x and y axis
        x=alt.X('x', scale=alt.Scale(domain=(x[0], x[-1]))),
        y=alt.Y('y', scale=alt.Scale(domain=y_range))
    )

    # Add points
    points = chart.mark_circle(size=100, color='red').encode(
        x='x',
        y='y'
    )

    # Combine chart and points
    chart = (chart + points)

    # display the chart
    st.altair_chart(chart, use_container_width=True)

with tab2:
    st.title("Lagrange Interpolation Calculator")
    st.write("---")

    # input data points (no fractions, only decimals)
    x_input = st.text_input("Enter x-coordinates (comma-separated): ", value = 0) 
    y_input = st.text_input("Enter y-coordinates (comma-separated): ", value = 0)

    # input value to interpolate at
    p_input = st.text_input("Enter x-value to interpolate at: ", value = 0)

    # convert inputs to lists of floats
    x = []
    y = []
    p = None

    # tries to execute the following codes unless(except) it detects an error
    try:
        x = [float(i) for i in x_input.split(",")]
        y = [float(i) for i in y_input.split(",")]
        p = float(p_input)
    except ValueError:
        st.error("Please enter a valid value.")

    # calculate and display the interpolated value at P(x)
    if st.button("Calculate ") and p is not None:
        answer = lagrange(x, y, p)
        st.write("---")
        # add the interpolated point to the input data
        x.append(p)
        y.append(answer)
        # display the interpolated value
        st.markdown(f"<br>The interpolated value at P({p}) is <span style='color:green'>{answer}</span>", unsafe_allow_html=True)
        
    # create a pandas DataFrame from the input data
    data = pd.DataFrame({'x': x, 'y': y})

    # create a chart
    chart = alt.Chart(data).mark_line().encode(
        x='x',
        y='y'
    )

    # Add points
    points = chart.mark_circle(size=100, color='red').encode(
        x='x',
        y='y'
    )

    # Combine chart and points
    chart = (chart + points)

    # display the chart
    st.altair_chart(chart, use_container_width=True)
