#!/usr/bin/env python
# coding: utf-8

# autogenerated from notebook
# This notebook depends on the following code by the author:
#
#
# - https://github.com/cknoll/yamlpyowl
# - https://github.com/cknoll/semantictools
#
#

from semantictools import core as smt
from yamlpyowl import core as ypo

# for graphviz visualization of networkx graphs
import nxv

fpath = "ocse-prototype-01.owl.yml"
om = ypo.OntologyManager(fpath)

# create an object for quick access to all entities:
n = om.name_mapping_container


q = list(ypo.owl2.Thing.subclasses())
G = smt.generate_taxonomy_graph_from_onto(ypo.owl2.Thing)

G.number_of_nodes() ##:

# http://www.graphviz.org/doc/info/attrs.html#d:nodesep
style = nxv.Style(
    graph={"rankdir": "BT", "nodesep": 0.05},
    node=lambda u, d: {
        "shape": "point",
        "fixedsize": True,
        "width": 0.1,
        "fontsize": 10,
    },
    edge=lambda u, v, d: {"style": "solid", "arrowhead": "none", "color": "#959595ff"},
)


# svg_data = nxv.render(G, style)
svg_data = nxv.render(G, style, format="svg")

svg_fname = "ocse-prototype01-unlabeled.svg"

with open(svg_fname, "wb") as svgfile:
    svgfile.write(svg_data)
