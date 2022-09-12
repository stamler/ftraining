import math
from itertools import chain

# The sliderule is a device for performing multiplication and division using
# logarithms. In this case we're going to use the same tick marks as the E6B
# mechanical flight computer, which is a common device for pilots to use for
# making calculations in flight and during preflight planning. This device is a
# round sliderule so each rotation of the outer ring represents a factor of 10.
# The ticks have a lower resolution as the numbers get larger, so we generate
# the list of spacings piecewise. The result is a list of 225 numbers indicating
# the relative position of each of the tick marks on the circle (angular) or
# line (distance). The resulting spacings can be used on both the A and B scales
# and represent, from an arbitrary position on the circle's perimeter, the
# offset of each tick. The position of 0 and 1 are the same position on the
# circle, or overlap on a linear sliderule.
int_iterator = chain(
  range(100, 150), range(150, 300, 2), range(300, 600, 5), range(600, 1000, 10)
)
tick_positions = list(map(lambda x: math.log10(x) -2, int_iterator))

# long ticks are every 5th tick except for the range of 30 to 60, which is
# every 2nd
long_ticks = [True if x % 5 == 0 else False for x in range(0, 126)] + \
              [True if x % 2 == 0 else False for x in range(126, 185)] + \
              [True if x % 5 == 0 else False for x in range(185, 225)]

# There are 26 number marks from 10 to 90. Each  unit from 10 to 25 is included,
# then every 5th unit from 25 to 60 then finally every 10th unit from 60 to 90.
number_labels = [str(int(x / 10)) if x % 10 == 0 else None for x in range(100, 150)] + \
    [str(int(x / 10)) if x % 10 == 0 else None for x in range(150, 250, 2)] + \
    [str(int(x / 10)) if x % 50 == 0 else None for x in range(250, 300, 2)] + \
    [str(int(x / 10)) if x % 50 == 0 else None for x in range(300, 600, 5)] + \
    [str(int(x / 10)) if x % 100 == 0 else None for x in range(600, 1000, 10)]

# Every tick on the A and B scales of an E6B slide rule.
e6b_ab_ticks = zip(tick_positions, long_ticks, number_labels)