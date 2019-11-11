
import lib.hw1.union_find

class Test_UF(object):
    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""
        print ("\n#####  Start Function Tests   #####\n")


    def test_one(self):
        pass

    def test_two(self):
        expected = (1, 2, 3)
        actual = (1, 2, 3)
        assert expected == actual

    def test_qf_not_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # test if (1, 2) is connected
        actual = inodes.qf_connected(1, 2)

        expected = False

        assert expected == actual
        print("qf not connected ")

    def test_qf_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # connect (1, 2)
        inodes.qf_union(1, 2)

        # test if (1, 2) is connected
        actual = inodes.qf_connected(1, 2)

        expected = True

        assert expected == actual
        print("qf connected")

    def test_qu_not_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # test if (1, 2) is connected
        actual = inodes.qu_connected(1, 2)

        expected = False

        assert expected == actual

        print("qu not connected")

    def test_qu_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # connect (1, 2)
        inodes.qu_union(1, 2)

        # test if (1, 2) is connected
        actual = inodes.qu_connected(1, 2)

        expected = True

        assert expected == actual

        print("qu connected")


    def test_wqu_not_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # test if (1, 2) is connected
        actual = inodes.wqu_connected(1, 2)

        expected = False

        assert expected == actual

        print("wqu not connected ")

    def test_wqu_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # connect (1, 2)
        inodes.wqu_union(1, 2)

        # test if (1, 2) is connected
        actual = inodes.wqu_connected(1, 2)

        expected = True

        assert expected == actual

        print("wqu  connected ")


    def test_pqu_not_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # test if (1, 2) is connected
        actual = inodes.pqu_connected(1, 2)

        expected = False

        assert expected == actual

        print("test pqu not connected ")

    def test_pqu_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # connect (1, 2)
        inodes.pqu_union(1, 2)

        # test if (1, 2) is connected
        actual = inodes.pqu_connected(1, 2)

        expected = True

        assert expected == actual

        print("test pqu  connected ")

    def test_wpqu_not_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # test if (1, 2) is connected
        actual = inodes.wpqu_connected(1, 2)

        expected = False

        assert expected == actual

        print("test wpqu not connected ")

    def test_wpqu_connected(self):

        # initialize network nodes
        inodes = lib.hw1.union_find.UF()
        inodes.qf_init(10)

        # connect (1, 2)
        inodes.wpqu_union(1, 2)

        # test if (1, 2) is connected
        actual = inodes.wpqu_connected(1, 2)

        expected = True

        assert expected == actual

        print("test wpqu  connected ")

t =Test_UF()
t.test_one()
t.test_two()

t.test_qf_not_connected()
t.test_qf_connected()
t.test_qu_not_connected()
t.test_qu_connected()
t.test_wqu_not_connected()
t.test_wqu_connected()
t.test_pqu_not_connected()
t.test_pqu_connected()
t.test_wpqu_not_connected()
t.test_wpqu_connected()

