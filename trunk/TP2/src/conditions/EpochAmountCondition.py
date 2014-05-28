

class EpochAmountCondition:

    def endConditionIsMet(self,epoch, etta):
        return epoch > 200
        # return epoch > 1000 --> maso menos converge para ojaM
        #return epoch > 250 --> converge sanger con estas iteraciones