from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass

from alts.core.data_sampler import DataSampler
from alts.core.configuration import Configurable

if TYPE_CHECKING:
    from alts.core.configuration import Configurable
    from typing import Tuple, List

@dataclass
class TwoSampleTest(Configurable):
    
    def test(self, sample1: Tuple[float,...], sample2: Tuple[float,...]) -> Tuple[List[float],List[float]]:
        ...
