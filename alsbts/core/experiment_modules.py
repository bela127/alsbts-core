from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass

from alts.core.experiment_modules import ExperimentModules

if TYPE_CHECKING:
    from alsbts.core.estimator import Estimator
    from alts.core.data.queried_data_pool import QueriedDataPool
    from alts.core.data.data_pool import DataPool

    from typing_extensions import Self #type: ignore


@dataclass
class StreamExperiment(ExperimentModules):
    estimator: Estimator

    def __call__(self, queried_data_pool: QueriedDataPool = None, oracle_data_pool: DataPool = None, **kwargs) -> Self:
        obj = super().__call__(queried_data_pool, oracle_data_pool, **kwargs)
        obj.estimator = obj.estimator(obj)
        return obj
