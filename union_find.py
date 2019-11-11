

# 1. quick-find
# 2. quick-union
# 3. weighted QU
# 4. QU + path compression
# 5. weighted QU + path compression

import random
import time


#import matplotlib.pyplot as plt

class UF(object):
    """Union Find class

    """

    def __init__(self):
        self.id = []

    def qf_init(self, N):
        """initialize the data structure

        """
        for x in range(N):
            self.id.append(x)

    def qf_union(self, p, q):


        """Union operation for Quick-Find Algorithm.
        connect p and q. You need to
        change all entries with id[p] to id[q]
        (linear number of array accesses)
        """


        old= self.id[p]
        new=self.id[q]
        for idx, x in enumerate(self.id):
            if x==old:
                self.id[idx]=new





    def get_root(self,idx):
        while idx != self.id[idx]:
            idx=self.id[idx]
        return idx
    def qf_connected(self, p, q):

        """Find operation for Quick-Find Algorithm.
        simply test whether p and q are connected

        """

        return self.id[p] == self.id[q]



    def qu_union(self, p, q):
        """Union operation for Quick-Union Algorithm.
         connect p and q.

         """

        idp =self.get_root(p)
        self.id[idp]=self.get_root(q)




    def qu_connected(self, p, q):
        """Find operation for Quick-Union Algorithm.
         test whether p and q are connected

         """

        return self.id[p] == self.id[q]

    def find(self, p):
        while p!=self.id[p]:
            p=self.id[p]
        return p

    def wqu_union(self, p, q):
        """Union operation for Weighted Quick-Union Algorithm.
         connect p and q.

         """

        idp=self.id[p]
        idq=self.id[q]

        rootP=self.get_root(idp)
        rootQ=self.get_root(idq)

        if rootP==rootQ:
            return
        elif self.id[rootP]>self.id[rootQ]:
            self.id[rootQ]=rootP
            self.id[rootP]+= self.id[rootQ]
        else:
            self.id[rootP]= rootQ
            self.id[rootQ]+= self.id[rootP]

    def find_w(self, p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        return p




    def wqu_connected(self, p, q):
        """Find operation for Weighted Quick-Union Algorithm.
         test whether p and q are connected

         """

        return self.find_w(p) == self.find_w(q)

    def pqu_union(self, p, q):
        """Union operation for path compressed Quick-Union Algorithm.
         connect p and q.

         """

        idp = self.id[p]
        idq = self.id[q]

        rootP = self.get_root(idp)
        rootQ = self.get_root(idq)

        if rootP == rootQ:
            return
        elif self.id[rootP] > self.id[rootQ]:
            self.id[rootQ] = rootP
            self.id[rootP] += self.id[rootQ]
        else:
            self.id[rootP] = rootQ
            self.id[rootQ] += self.id[rootP]

    def pqu_connected(self, p, q):
        """Find operation for path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """

        return self.find_w(p) == self.find_w(q)


    def pqu_Find(self,x):
        if self.id[x]==x:
            return x
        else:
            return self.pqu_Find(self.id[x])
    def wpqu_union(self, p, q):
        """Union operation for Weighted path compressed Quick-Union Algorithm.
         connect p and q.

         """
        idp=self.get_root(p)
        idq=self.get_root(q)
        if(self.id[idq]> self.id[idp]):
            idp,idq= idq,idp

        self.id[idq]=idp
        self.id[idp]+= self.id[idq]

        self.SZid=[]



    def wpqu_connected(self, p, q):
        """Find operation for Weighted path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """

        return self.get_root(p) == self.get_root(q)

if __name__ == "__main__":

    # iteration
    set_szs = [10]
    timing = []

    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            inodes.qf_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!


    # plt.plot(set_szs, timing)
    # plt.xscale('log')
    # plt.yscale('log')
    # plt.title('log')
    # plt.ylabel('some numbers')
    # plt.show()