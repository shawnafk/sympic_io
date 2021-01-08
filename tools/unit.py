# we using me and
import numpy as np
# physical constant in SI unit
mu0 = 4*np.pi*1e-7
epsi0 = 8.8542e-12
c = 299792458.
me = 9.10000000000000006e-31
# base units 4


def gen_unit(REAL_DX):
    unit = {}
    # m
    unit['LENGTH'] = REAL_DX
    # H/m
    unit['PERMEABILITY'] = mu0
    # m/s
    unit['VELOCITY'] = c
    # kg
    unit['MASS'] = me
    # derived units
    # s
    unit['TIME'] = unit['LENGTH']/unit['VELOCITY']
    # c
    unit['CHARGE'] = np.sqrt(unit['MASS']*unit['LENGTH']/unit['PERMEABILITY'])
    # A/m**2
    unit['CURRENT_DENSITY'] = unit['CHARGE']/unit['LENGTH']**2/unit['TIME']
    # T
    unit['B'] = unit['MASS']/unit['TIME']/unit['CHARGE']
    # V/m
    unit['E'] = unit['MASS']*unit['VELOCITY']/unit['TIME']/unit['CHARGE']
    # V
    unit['POTENTIAL'] = unit['E']*unit['LENGTH']
    # W/m**3
    unit['POWER_DENSITY'] = unit['MASS']/unit['LENGTH']/unit['TIME']**3
    # J
    unit['ENERGY'] = unit['MASS']*unit['VELOCITY']**2
    # ...
    unit['PERMITTIVITY'] = (unit['TIME']**2*unit['CHARGE']
                            ** 2)/(unit['MASS']*unit['LENGTH']**3)
    # constant
    const = {}
    const['mu0'] = 1.
    const['epsi0'] = 1.
    const['c'] = 1.
    return unit, const


def Ope(n0, U):
    q = 1.6e-19/U[0]['CHARGE']
    n = n0*U[0]['LENGTH']**3
    return q*n**0.5


def Opi(m, z, n0, U):
    q = z*1.6e-19/U[0]['CHARGE']
    n = n0*U[0]['LENGTH']**3
    return (q**2*n/m/1836)**0.5


def Oce(B, U):
    q = 1.6e-19/U[0]['CHARGE']
    b = B/U[0]['B']
    return q*b/1


def Oci(m, z, B, U):
    q = z*1.6e-19/U[0]['CHARGE']
    b = B/U[0]['B']
    return q*b/m/1836

# temp


def Ek2Tev(Ek, v, n, npg, n_ref, m, U):
    n[n == 0] = 1
    # scale is weight of a macro particle to real particle
    scale = U[0]['LENGTH']**3*n_ref/npg
    # first 3 elements storage 1/2*m*v**2, where m is macro particle mass = real me * scale
    # in other word, real summation of energy in this volume
    # v v sq... obtained by sum macro particles particles is not uniform
    # sigma (all macro particle * me * scale * v_mac)
    # so have to devide n_macro to get real ava v that one macro particle represented.
    # a particle (no mater macro or real it is same) averaged v_sq
    Ek_per_pat = Ek/n/scale
    # average velocity aka drift velocity
    v_per_pat = v/n
    # sum_v=0
    # 6th is number density, number of macro particle
    # sum 3 dir
    #temperature in kev
    KbT0 = 2*m*(Ek_per_part-v_per_pat**2)*U[0]['ENERGY'] / 1.6e-19/1000
    return KbT0
