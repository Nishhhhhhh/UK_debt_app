# ==========================================
# IMPORT LIBRARIES
# ==========================================

import networkx as nx
import matplotlib.pyplot as plt


# ==========================================
# CREATE NETWORK
# ==========================================

def create_network():

    G = nx.DiGraph()

    # Nodes

    G.add_node("Government")

    G.add_node("Banks")

    G.add_node("Investors")

    G.add_node("Households")

    # Connections

    G.add_edge("Government","Banks")

    G.add_edge("Government","Investors")

    G.add_edge("Government","Households")

    G.add_edge("Banks","Investors")

    G.add_edge("Investors","Households")

    G.add_edge("Households","Government")

    plt.figure(figsize=(8,6))

    pos = nx.spring_layout(

        G,

        seed=42

    )

    nx.draw(

        G,

        pos,

        with_labels=True,

        node_size=3500,

        node_color="skyblue",

        edge_color="black",

        font_size=12,

        arrows=True

    )

    plt.title(

        "UK Debt Economic Network"

    )

    plt.savefig(

        "static/charts/network.png"

    )

    plt.close()

    return G