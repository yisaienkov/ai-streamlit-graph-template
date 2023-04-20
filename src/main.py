import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network


def simple_func(df): 
    nx_graph = nx.DiGraph()
    nx_graph.add_node("x", size=20)
    nx_graph.add_node("y", size=20)
    nx_graph.add_node("z", size=20)

    for a in "xyz":
        for b in "xyz":
            if df.loc[a, b]:
                nx_graph.add_edge(a, b)

    nt = Network(height="500px", directed=True)
    nt.from_nx(nx_graph)

    nt.show('test.html', notebook=False)

df = pd.DataFrame(np.zeros((3, 3)), columns=["x", "y", "z"], index=["x", "y", "z"])
df = st.sidebar.experimental_data_editor(df)
simple_func(df)

with open("test.html", 'r', encoding='utf-8') as file:
    source_code = file.read() 
    components.html(source_code, height=500)