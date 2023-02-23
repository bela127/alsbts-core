from alts.core.configuration import Configurable


class ChangeDetector(Configurable):

    def detect(self, changing_signal) -> float:
        raise NotImplementedError()
