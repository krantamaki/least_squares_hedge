"""@package least_squares_hedge.PathIndependentLeastSquaresHedge
@author Kasper Rantamäki
TODO
"""
from typing import Callable, List, Literal, Tuple, Optional
import numpy as np
import pandas as pd

from quantform.pylib.equity.derivative import Option
from quantform.pylib.equity.portfolio import GenericUnivariateStrategy
from quantform.pylib import QfDate


class PathIndependentLeastSquaresHedge:
  """Class for encapsulating the functionality for the (path-independent) least squares hedge"""

  def __init__(self, payoff_func: Callable[[float], float], options: List[Option], 
               solver: Literal['quantform', 'numpy', 'scipy'] = 'scipy') -> None:
    """
    TODO
    """
    assert len(set([option.maturity_date for option in options])) == 1, "All of the options must share the same maturity date!"
    assert len(set([option.underlying for option in options])) == 1, "All of the options must share the same underlying!"
    assert sum([int(option.market_price is not None) for option in options]) == len(options), "The options must have a set market price!"
    assert solver in ['quantform', 'numpy', 'scipy'], f"Invalid solver specified! ({solver} not in ['quantform', 'numpy', 'scipy'])"

    self.__options = options
    self.__options.sort()

    self.__maturity_date = options[0].maturity_date
    self.__payoff = payoff_func
    self.__solver = solver

    self.__strategy = None


  def __call__(self, underlying_value: float, report_date: QfDate) -> float:
    """
    Prices the hedge
    """
    assert self.__strategy is not None, "The hedge needs to be solved before it can be priced!"

    return self.__strategy(underlying_value, report_date)

  
  def solve(self, value_range: Tuple[float, float], n_points: int) -> None:
    """
    Solves for the optimal hedge
    """
    pass 


  @property
  def strategy(self) -> Optional[GenericUnivariateStrategy]:
    """
    Returns a strategy object
    """
    return self.__strategy
  