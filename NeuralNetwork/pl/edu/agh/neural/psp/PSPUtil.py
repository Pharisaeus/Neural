from pl.edu.agh.neural.psp.SumPotential import SumPotential

class PSPUtil(object):
    SUM_POTENTIAL = SumPotential.NAME

    REGISTERED_PSP = {
        SUM_POTENTIAL: SumPotential()
    }

    @staticmethod
    def registered_psps():
        return PSPUtil.REGISTERED_PSP.keys()

    @staticmethod
    def get_psp(name):
        return PSPUtil.REGISTERED_PSP[name]

    @staticmethod
    def default_psp():
        return PSPUtil.SUM_POTENTIAL
