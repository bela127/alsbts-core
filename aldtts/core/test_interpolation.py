from __future__ import annotations
from abc import abstractproperty
from typing import TYPE_CHECKING

from dataclasses import dataclass

import numpy as np
from alts.core.data.data_pool import DataPool

from alts.core.experiment_module import ExperimentModule
from alts.core.queryable import Queryable

if TYPE_CHECKING:
    from typing_extensions import Self #type: ignore
    from alts.core.experiment_modules import ExperimentModules
    from alts.core.data_sampler import DataSampler
    from aldtts.core.two_sample_test import TwoSampleTest



@dataclass
class TestInterpolator(Queryable, ExperimentModule):
    test: TwoSampleTest

    def __call__(self, exp_modules: ExperimentModules = None, **kwargs) -> Self:
        obj = super().__call__(exp_modules, **kwargs)
        obj.test = obj.test()
        return obj