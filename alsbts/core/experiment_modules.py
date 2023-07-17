from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass

from alts.core.experiment_modules import InitQueryExperimentModules
from alts.core.configuration import init
from alsbts.modules.query.query_sampler import StreamQuerySampler


if TYPE_CHECKING:
    from alsbts.core.estimator import Estimator
    from alts.core.data.queried_data_pool import QueriedDataPool
    from alts.core.oracle.oracle import Oracle
    from alts.core.configuration import Required
    from typing_extensions import Self
    from alts.core.query.query_sampler import QuerySampler



@dataclass
class StreamExperiment(InitQueryExperimentModules):
    estimator: Estimator = init()

    initial_query_sampler: QuerySampler = init(default_factory=StreamQuerySampler)

    def __post_init__(self):
        super().__post_init__()
        self.estimator = self.estimator(exp_modules = self)
