import string

import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from pyvis.network import Network


def simple_func(df): 
    nx_graph = nx.DiGraph()
    for x in df.columns:
        nx_graph.add_node(x, size=20)
    
    for a in df.index:
        for b in df.columns:
            if df.loc[a, b]:
                nx_graph.add_edge(a, b)

    nt = Network(height="500px", directed=True)
    nt.from_nx(nx_graph)

    nt.show('test.html', notebook=False)

n_nodes = st.sidebar.number_input("N nodes", min_value=1, value=3, max_value=10)
node_names = list(string.ascii_lowercase[:n_nodes])

df = pd.DataFrame(np.zeros((n_nodes, n_nodes)), columns=node_names, index=node_names)
df = st.sidebar.experimental_data_editor(df)

nodes = []
for a in df.index:
    for b in df.columns:
        if df.loc[a, b]:
            nodes.append((a, b))

st.sidebar.text_area("Edge view:", nodes)

simple_func(df)

with open("test.html", 'r', encoding='utf-8') as file:
    source_code = file.read() 
    components.html(source_code, height=500)