import json
import urllib.request
import pandas as pd
from setify import utils


def _get_server():
    # return 'http://207.148.28.62:5000'
    return 'http://127.0.0.1:5000'


def country_birth_rate():
    fpath = utils.load_data(_get_server() + "/country_birth_rate", 'country_birth_rate.h5')
    return pd.read_hdf(fpath)


def country_death_rate():
    fpath = utils.load_data(_get_server() + "/country_death_rate", 'country_death_rate.h5')
    return pd.read_hdf(fpath)

def iris():
    fpath = utils.load_data(_get_server() + "/iris", 'iris.h5')
    return pd.read_hdf(fpath)

def country_name_code():
    fpath = utils.load_data(_get_server() + "/country_name_code", 'country_name_code.h5')
    return pd.read_hdf(fpath)

def logic_gate_not():
    fpath = utils.load_data(_get_server() + "/logic_gate_not", 'logic_gate_not.h5')
    return pd.read_hdf(fpath)


def logic_gate_and():
    fpath = utils.load_data(_get_server() + "/logic_gate_and", 'logic_gate_and.h5')
    return pd.read_hdf(fpath)


def logic_gate_nand():
    fpath = utils.load_data(_get_server() + "/logic_gate_nand", 'logic_gate_nand.h5')
    return pd.read_hdf(fpath)


def logic_gate_or():
    fpath = utils.load_data(_get_server() + "/logic_gate_or", 'logic_gate_or.h5')
    return pd.read_hdf(fpath)


def logic_gate_nor():
    fpath = utils.load_data(_get_server() + "/logic_gate_nor", 'logic_gate_nor.h5')
    return pd.read_hdf(fpath)


def logic_gate_xor():
    fpath = utils.load_data(_get_server() + "/logic_gate_xor", 'logic_gate_xor.h5')
    return pd.read_hdf(fpath)


def logic_gate_xnor():
    fpath = utils.load_data(_get_server() + "/logic_gate_xnor", 'logic_gate_xnor.h5')
    return pd.read_hdf(fpath)


def temperatures_daily_min():
    fpath = utils.load_data(_get_server() + "/temperatures_daily_min", 'temperatures_daily_min.h5')
    return pd.read_hdf(fpath)


def shampoo_sales():
    fpath = utils.load_data(_get_server() + "/shampoo_sales", 'shampoo_sales.h5')
    return pd.read_hdf(fpath)


def monthly_sunspot():
    fpath = utils.load_data(_get_server() + "/monthly_sunspot", 'monthly_sunspot.h5')
    return pd.read_hdf(fpath)


def daily_female_births():
    fpath = utils.load_data(_get_server() + "/daily_female_births", 'daily_female_births.h5')
    return pd.read_hdf(fpath)


def occupancy_detection():
    fpath = utils.load_data(_get_server() + "/occupancy_detection", 'occupancy_detection.h5')
    return pd.read_hdf(fpath)

