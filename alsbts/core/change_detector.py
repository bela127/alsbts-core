from alts.core.experiment_module import ExperimentModule

class ChangeDetector(ExperimentModule):

    def detect(self, changing_signal) -> float:
        raise NotImplementedError()
