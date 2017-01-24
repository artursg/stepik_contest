import sys
import cProfile, pstats, io

def run():
        substrates = set([s for s in sys.stdin.readline().rstrip().split(" ")])
        
        r = sys.stdin.readlines()
        r = list(map(lambda x: x.strip().split('->'), r))
        r = list(map(lambda x: [set(x[0].split('+')), set(x[1].split('+'))], r))
        
        n_reactions = len(r)

        while (n_reactions > 0):
            for idx, reaction in enumerate(r):
                #print(str(reaction[0]) + ' is superset of ' + str(substrates))
                if substrates.issuperset(reaction[0]):
                    substrates.update(reaction[1])
                    del r[idx]
                    if (len(r) != n_reactions):
                        n_reactions = len(r)
                    else:
                        break
                    print ((' ').join(sorted(substrates)))
                    
pr = cProfile.Profile()
pr.enable()
run()
pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
