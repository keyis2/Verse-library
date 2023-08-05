'''
This file integrates high-level functions of 2D & 3D plotter 
'''

from __future__ import annotations
import copy
import numpy as np
import plotly.graph_objects as go
from typing import List, Tuple, Union
from plotly.graph_objs.scatter import Marker
from verse.analysis.analysis_tree import AnalysisTree, AnalysisTreeNode, AnalysisTreeNodeType
from verse.map.lane_map import LaneMap

import plotter2D, plotter3D_new

def plotTree2d(    
    root: Union[AnalysisTree, AnalysisTreeNode],
    map=None,
    fig=go.Figure(),
    x_dim: int = 1,
    y_dim: int = 2,
    print_dim_list=None,
    color_array=None,
    map_type="lines",
    scale_type="trace",
    label_mode="None",
    sample_rate=1,
    combine_rect=None,
    anime=False,
    time_step=None,
    speed_rate=1,
    anime_mode="normal",
    full_trace=False,):
    if root.type == AnalysisTreeNodeType.SIM_TRACE:
        if anime:
            plotter2D.simulation_anime(root, map, fig, x_dim, y_dim, print_dim_list, color_array, map_type, scale_type, label_mode, sample_rate, time_step, speed_rate, anime_mode, full_trace,)
        else:
            plotter2D.simulation_tree(root, map, fig, x_dim, y_dim, print_dim_list, color_array, map_type, scale_type, label_mode, sample_rate)
    elif root.type == AnalysisTreeNodeType.REACH_TUBE:
        if anime:
            plotter2D.reachtube_anime(root, map, fig, x_dim, y_dim, print_dim_list, color_array, map_type, scale_type, label_mode, sample_rate, time_step, speed_rate, combine_rect)
        else:
            plotter2D.reachtube_tree(root, map, fig, x_dim, y_dim, print_dim_list, color_array, map_type, scale_type, label_mode, sample_rate, combine_rect)
    else:
        raise ValueError(f"Invalid node type")
def plotTree3d(    
    root: Union[AnalysisTree, AnalysisTreeNode],
    map=None,
    fig=go.Figure(),
    x_dim: int = 1,
    y_dim: int = 2,
    z_dim: int = 3,
    print_dim_list=None,
    color_array=None,
    map_type="outline",
    sample_rate=1,
    xrange=[],
    yrange=[],
    zrange=[],
    combine_rect=None,):
    if root.type == AnalysisTreeNodeType.SIM_TRACE:
        plotter3D_new.simulation_tree_3d(root, map, fig, x_dim, y_dim, z_dim, print_dim_list, color_array, map_type, sample_rate, xrange, yrange, zrange)
    elif root.type == AnalysisTreeNodeType.REACH_TUBE:   
        plotter3D_new.reachtube_tree_3d(root, map, fig, x_dim, y_dim, z_dim, print_dim_list, color_array, map_type, sample_rate, xrange, yrange, zrange, combine_rect)
    else:
        raise ValueError(f"Invalid node type") 