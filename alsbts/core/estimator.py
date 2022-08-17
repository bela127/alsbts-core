from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass

from alts.core.experiment_module import ExperimentModule

if TYPE_CHECKING:
    from typing_extensions import Self #type: ignore
    from alts.core.data_sampler import DataSampler
    from alts.core.query.query_sampler import QuerySampler


@dataclass
class Estimator(ExperimentModule):

    def estimate(self):
        raise NotImplementedError()
        

    def __call__(self, exp_modules = None, **kwargs) -> Self:
        obj = super().__call__(exp_modules, **kwargs)
        return obj
