from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass

from scipy.stats import kruskal #type: ignore

from alts.core.data_sampler import DataSampler
from alts.core.configuration import Configurable

if TYPE_CHECKING:
    from alts.core.configuration import Configurable
    from typing import Tuple, List

@dataclass
class MultiSampleTest(Configurable):


    def test(self, samples: Tuple[float,...]) -> Tuple[List[float],List[float]]:
        raise NotImplementedError
