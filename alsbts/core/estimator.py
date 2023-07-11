from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass

from alts.core.experiment_module import ExperimentModule
from alts.core.subscriber import ExperimentSubscriber, ResultSubscriber

if TYPE_CHECKING:
    from nptyping import  NDArray, Number, Shape

@dataclass
class Estimator(ExperimentSubscriber, ResultSubscriber):

    def __post_init__(self):
        super().__post_init__()

    def estimate(self, times, queries, vars) -> NDArray[Shape["query_nr, ... result_dim"], Number]:
        raise NotImplementedError()

    def query(self, queries):
        raise NotImplementedError()

    def train(self) -> None:
        pass

    def result_update(self):
        super().result_update()
        self.train()
        

    def experiment_update(self):
        super().experiment_update()
        times = self.exp_modules.data_pools.stream.last_queries
        vars = self.exp_modules.data_pools.stream.last_results
        queries = self.exp_modules.oracles.process.last
        self.estimate(times, queries, vars)
        