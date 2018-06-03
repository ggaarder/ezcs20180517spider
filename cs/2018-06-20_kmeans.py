import csv
import itertools
import operator
import matplotlib.pyplot

def load_irisdata(col1, col2, filename='iris-dataset.csv'):
    COLS = list(range(0, 4))
    if not col1 in COLS or not col2 in COLS:
        raise IndexError('Iris data column should be in [0, 4)')

    dat = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dat.append([row[col1], row[col2]])
    return dat

COLOURS, MARKERS = 'kbgrcmy', 'ov^<>1234sp*hH+xDd|_'
FMTS = sorted([operator.add(*i)
               for i in itertools.product(COLOURS, MARKERS)],
              # sorted to let formats of same colours but different markers
              # come firstly, instead same markers but different colours
              # i.e. 'k.' 'k,' 'ko' ... instead of 'k.' 'b.' 'g.' ...
              key = lambda c: abs(ord(c[0])-ord('k'))
              # 'k' (black) comes first
)

def plot(dats):
    """dats = [[[x1, y1], [x2, y2], ...],  (group1)
               [[x1, y1], [x2, y2], ...],  (group2)
               [[x1, y1], [x2, y2], ...],  (group3)
               ...]
    """
    fmts = FMTS
    if len(dats) > len(fmts):
        fmts *= 2
        while len(dat) > len(fmts):
            fmts += FMTS

    plotargs = []
    for points, fmt in zip(dats, fmts):
        x, y = [p[0] for p in points], [p[1] for p in points]
        plotargs += [x, y, fmt]
        
    matplotlib.pyplot.plot(*plotargs)
    matplotlib.pyplot.show()

if __name__ == '__main__':
    testdats = []
    
    for col1 in range(0, 4):
        for col2 in range(col1+1, 4):
            dat = load_irisdata(col1, col2)
            testdats.append(dat)

    plot(testdats)
