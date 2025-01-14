import numpy as np
import pandas as pd

class Dataset(object):
    def __init__(self, df, livetime, POT, hdrdf=None):
        self.df = df
        self.POT = POT
        self.livetime = livetime
        self.hdrdf = hdrdf

    def concat(self, *othrs, offset=1_000_000):
        POT = sum([o.POT for o in othrs]) + self.POT
        livetime = sum([o.livetime for o in othrs]) + self.livetime

        for i in range(len(othrs)):
            othrs[i].df.index = othrs[i].df.index.set_levels(othrs[i].df.index.levels[0] + offset*(i+1), level=0)
            if self.hdrdf is not None:
                othrs[i].hdrdf.index = othrs[i].hdrdf.index.set_levels(othrs[i].hdrdf.index.levels[0] + offset*(i+1), level=0)

        df = pd.concat([self.df] + [o.df for o in othrs])
        hdrdf = None
        if self.hdrdf is not None:
            hdrdf = pd.concat([self.hdrdf] + [o.hdrdf for o in othrs])

        return Dataset(df, livetime, POT, hdrdf)
