from pl.edu.agh.neural.learning.cp.rules.DeltaRule import DeltaRule
from pl.edu.agh.neural.learning.cp.rules.WidrowHoff import WidrowHoff

class RulesUtil(object):
    DELTA_RULE = DeltaRule.NAME
    WIDROW_HOFF = WidrowHoff.NAME

    REGISTERED_RULES = {
        DELTA_RULE: DeltaRule(),
        WIDROW_HOFF: WidrowHoff()
    }

    @staticmethod
    def rules():
        return RulesUtil.REGISTERED_RULES.keys()

    @staticmethod
    def default_layer():
        return RulesUtil.WIDROW_HOFF

    @staticmethod
    def get_rule(name):
        return RulesUtil.REGISTERED_RULES[str(name)]