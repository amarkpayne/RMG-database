#!/usr/bin/env python
# encoding: utf-8

name = "c-C5H5_CH3_Sharma_TST"
shortDesc = u"CCSD(T)//B3LYP/6-31g+(d') and MP4SDQ//B3LYP/CBSB4"
longDesc = u"""
Kinetics from:
Computed Rate Coefficients and Product Yields for c-C5H5+CH3->Products
S. Sharma and W. H. Green*
Department of Chemical Engineering, Massachusetts Institute of Technology, Cambridge, MA 02139
Received: January 22, 2009; Revised Manuscript Received: June 1, 2009
J. Phys. Chem. A 2009, 113, 8871-8882
"""
entry(
    index = 1,
    label = "c-C5H5 + CH3 <=> C5H5CH3-5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.38482e-08, 'cm^3/(molecule*s)'),
        n = -0.7,
        Ea = (-0.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "R2 + H <=> C5H5CH3-5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.582e-10, 'cm^3/(molecule*s)'),
        n = -0.1,
        Ea = (0.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "R2 + H <=> C5H5CH3-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7982e-11, 'cm^3/(molecule*s)'),
        n = 0.3,
        Ea = (0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "R1 + H <=> C5H5CH3-1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.74338e-12, 'cm^3/(molecule*s)'),
        n = 0.6,
        Ea = (-0.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "R2 + H <=> C5H5CH3-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.50356e-10, 'cm^3/(molecule*s)'),
        n = 0.1,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "R3 + H <=> C5H5CH3-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6921e-12, 'cm^3/(molecule*s)'),
        n = 0.5,
        Ea = (-0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 7,
    label = "R4 + H <=> C5H5CH3-5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.48677e-12, 'cm^3/(molecule*s)'),
        n = 0.6,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

