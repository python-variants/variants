
class DivisionDataClass(object):
    def __init__(self):
        self.MODE_VALS = self.__get_mode_vals()

    ALL_VALS = [(0, 1, 0)]

    DIV_VALS = ALL_VALS + [
        (12, 8, 1.50),
        (11, 4, 2.75),
        (21, 4, 5.25)
    ]

    ROUND_VALS = ALL_VALS + [
        (12, 8, 2.00),
        (11, 4, 3.00),
        (21, 4, 5.00)
    ]

    FLOOR_VALS = ALL_VALS + [
        (12, 8, 1.0),
        (11, 4, 2.0),
        (21, 4, 5.0)
    ]

    CEIL_VALS = ALL_VALS + [
        (12, 8, 2.0),
        (11, 4, 3.0),
        (21, 4, 6.0)
    ]

    def __get_mode_vals(self):
        modes_vals = [
            (None, self.DIV_VALS),
            ('round', self.ROUND_VALS),
            ('floor', self.FLOOR_VALS),
            ('ceil', self.CEIL_VALS)
        ]

        out = [(vals + (mode,))
               for mode, all_vals in modes_vals
               for vals in all_vals]

        return out

DivisionData = DivisionDataClass()