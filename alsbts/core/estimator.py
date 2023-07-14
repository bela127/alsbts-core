from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass

from alts.core.experiment_module import ExperimentModule
from alts.core.subscriber import ExpModSubscriber, ResultDataSubscriber

if TYPE_CHECKING:
    from nptyping import  NDArray, Number, Shape
    from alts.core.subscribable import Subscribable

@dataclass
class Estimator(ExperimentModule, ExpModSubscriber, ResultDataSubscriber):

    def __post_init__(self):
        super().__post_init__()

    def estimate(self, times, queries, vars) -> NDArray[Shape["query_nr, ... result_dim"], Number]:
        raise NotImplementedError()

    def query(self, queries):
        raise NotImplementedError()

    def train(self) -> None:
        pass

    def result_update(self, subscription: Subscribable):
        super().result_update(subscription)
        self.train()
        

    def experiment_update(self, subscription: Subscribable):
        super().experiment_update(subscription)
        times = self.exp_modules.data_pools.stream.last_queries
        vars = self.exp_modules.data_pools.stream.last_results
        queries = self.exp_modules.oracles.process.last
        self.estimate(times, queries, vars)
        