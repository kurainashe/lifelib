import sys
import os.path
import pickle
import pathlib

import pytest

from lifelib.projects.solvency2 import solvency2
from tests.data.generate_testdata_solvency2 import generate_data

if '' not in sys.path:
    sys.path.insert(0, '')

datadir = pathlib.Path(__file__).parents[1].joinpath('data')
testdata = str(datadir.joinpath('data_solvency2'))


def test_nestedlife():
    model = solvency2.build()
    data = generate_data(model)

    with open(testdata, 'rb') as file:
        data_saved = pickle.load(file)

    assert data == data_saved


