from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass
from abc import abstractmethod

from alts.core.experiment_module import ExperimentModule
from alts.core.subscriber import ExpModSubscriber, ResultDataSubscriber
from alts.core.estimator import Estimator

if TYPE_CHECKING:
    from nptyping import  NDArray, Number, Shape
    from alts.core.subscribable import Subscribable

class SBEstimator(Estimator, ExpModSubscriber, ResultDataSubscriber):

    def estimate(self, exp_mods) -> NDArray[Shape["query_nr, ... result_dim"], Number]:
        times = self.exp_modules.data_pools.stream.last_queries
        vars = self.exp_modules.data_pools.stream.last_results
        queries = self.exp_modules.oracles.process.latest_add
        return self.sb_estimate(times, queries, vars)
    
    abstractmethod
    def sb_estimate(self, times, queries, vars) -> NDArray[Shape["query_nr, ... result_dim"], Number]:
        raise NotImplementedError()

        