# Package(Module) Manual Loading 
import pip, os, importlib 

# Package(Module) Auto-Importing/Loading 
def loadLib(pkg, pkgModl):

    try:
        if pkgModl != '':
            pkgModl = getattr(importlib.import_module(pkg), pkgModl)
        else:
            pkgModl = importlib.import_module(pkg)
    except ModuleNotFoundError:
        os.system("pip install " + pkg)
        pkgModl = getattr(importlib.import_module(pkg), pkgModl)
    return pkgModl


randomUniform = loadLib('random', 'uniform')
statsMean = loadLib('statistics', 'mean')
statsMedian = loadLib('statistics', 'median')

plt = loadLib('matplotlib.pyplot', '')
tckr = loadLib('matplotlib', 'ticker')

pltTckrMLoc = loadLib('matplotlib.ticker', 'MultipleLocator')
pltTckrMLoc = loadLib('matplotlib.ticker', 'AutoMinorLocator')

math = loadLib('math', '')
np = loadLib('numpy', '')
repeat = loadLib('itertools', 'repeat')

# Constants Definition
numb_range_start = -1000
numb_range_end = 1000
numbs_in_vector = 200
threshold = 0          # threshold is the min(abs(mean-median)) 
                       # after it gets reached data elements  
                       # removal will cease


# Function Declarations
def rmvEdgeElems(lst):
    """
    removes a lists's LeftMost & RightMost elements 
    and returns back the shortened lists for each removal
    """
    lstnoL = list(lst[1::]) 
    lstnoR = list(lst[:-1:])
    return lstnoL, lstnoR


def mn_md_diff(lstL, lstR):
    """
    Calcs the abs(mean median diff) for 2 lists
    and returns 
    1. the abs(mean median diff) for each list
    2. an 1-letter response denoting the lower diff list 
    3. both lists' mean, median value pairs
    """
    mnL = statsMean(lstL) 
    mdL = statsMedian(lstL)

    mnR = statsMean(lstR) 
    mdR = statsMedian(lstR)

    diffL = abs(mnL - mdL)
    diffR = abs(mnR - mdR)
    
    if diffL > diffR:
        return [diffR, 'R', mnR, mdR]
    elif diffL < diffR:
        return [diffL, 'L', mnL, mdL]
    else:
        return [diffL, 'E', mnL, mdL]   # for Equal mean median diffs


# numlst = randomUniform(range(1,10000), 100)   
# numlst = np.random.normal(120, 34, 1000)     
# numlst = [1,24,57,47,3,58,7,9,69,4,30,2,45,5,77,5,4,25,2,45,83,1,97,5,4,4,5,47,0,6]

# Produces a vector of random real numbers
numlst= []
for i in range(0, numbs_in_vector):
    numlst.append(randomUniform(numb_range_start, numb_range_end))

numlst = sorted(numlst)
lst = list(numlst)

diff = abs(statsMean(numlst) - statsMedian(numlst))
if abs(diff < threshold):
    print(f"I am breaking b/c the mean median diff = {diff} and " \
          f"that's is lower than threshold {threshold}")
    exit()


# initiates 3 new lists for the means, the medians and their diffs
diffs, mns, mds = map(lambda x: list(x), repeat([], 3))

# checks which data element removal (the first or the last) renders 
# the lower mean median diff and keeps the list w/o it. Then repeats 
# the same logic on that list 
for i in range(0, len(numlst)-2):
    # print(f"iteration {i}")
    lstnoL, lstnoR = rmvEdgeElems(lst)      # drops L & R edge (first & last) elements
    # print('no L')
    # print(lstnoL)
    # print('no R')
    # print(lstnoR)
    # print('   ')

    diff, side, mn, md = mn_md_diff(lstnoL, lstnoR)
    diffs.append(diff)
    mns.append(mn)
    mds.append(md)
    # print(f"no {side}-most elem list was picked")
    # print(f"mean = {mns}")
    # print(f"median = {mds}")
    # print('  ')

    if diff > threshold:
        if side == 'L':
            lst = lstnoL[:]
        elif side == 'R':
            lst = lstnoR[:]
        elif side == 'E':
            # keeps the list w/ R-most elem dropped b/c after eliminating either 
            # its L- or R-most elems it's more likely that one of the 2 diffs 
            # will be lower comparing to the diffs the list w/o its L-most elem 
            # will exhibit when we eliminate either of its edge elems
            lst = list(lstnoR)  # keep the list w/ R-most elem dropped (lstnoR)
    else:
        print(f"I am breaking b/c the mean median diff = {diff} and " \
              f"that's is lower than threshold {threshold}")
        break


# Ploting the continuously shrinking list's means, medians and the diffs 
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.subplots_adjust(hspace=1.0)

# diffs = list(map(lambda x: math.log(x+0.0001, 10), diffs))
ax1.plot(diffs, 'g-', label='mean and median abs diffs')
ax1.set_xlabel('iteration')
ax1.set_ylabel('abs(mean-median)')
ax1.set_title ('mean and median abs diffs')
ax1.xaxis.set_minor_locator(tckr.MultipleLocator(5))
ax1.yaxis.set_minor_locator(tckr.MultipleLocator(20))

# mns = [math.log(y, 10) for y in mns]
# mds = [math.log(x, 10) for x in mds]

ax2.plot(mds, mns, 'b-.', label='mean vs median')
ax2.set_xlabel('median')
ax2.set_ylabel('mean')
ax2.set_title ('mean vs median')
ax2.xaxis.set_minor_locator(tckr.MultipleLocator(5))
ax2.yaxis.set_minor_locator(tckr.MultipleLocator(20))

# color marks the beginning and end of the md,mn (x,y) pairs' line   
plt.scatter(mds[0], mns[0], c='red', marker='H', s=50)        # start (1st point)
plt.scatter(mds[-1], mns[0-1], c='green', marker='H', s=50)   # end   (last point)

plt.show()