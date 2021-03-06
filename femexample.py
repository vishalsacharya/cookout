#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example script for running a 1D convection-diffusion problem.
"""
import numpy as np
import cookout.fem.integrators as integrators
import cookout.fem.operators as op
import cookout.fem.mesh as m

# configuration.
mesh = m.Mesh1D(1000, 2)
ops = op.Operators1D(mesh, left_dirichlet_value=0.0, right_dirichlet_value=1.0)
coeffs = {
    'diffusion': 1e-2,
    'convection': 1e-1,
}
ts = np.linspace(0, 10, 1000)
forcing = lambda t, x: 0.0*x + 0.0
constant_load = True
initial = mesh.nodes**2

# do it.
solution = integrators.time_integrate(ops, forcing, coeffs, ts, initial,
                                      constant_load=constant_load)
