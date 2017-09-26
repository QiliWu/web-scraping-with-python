import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='wuqili2017', db='mysql', charset='utf8')
cur = conn.cursor()

cur.execute('USE wikipedia')

class SolutionFound(RuntimeError):
    def __init__(self, message):
        self.message = message

def getLinks(fromPageId):
    cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s", (fromPageId))
    if cur.rowcount == 0:
        return None
    else:
        return [x[0] for x in cur.fetchall()]

def constructDict(currentPageId):
    links = getLinks(currentPageId)
    #print('links: ',links)
    if links:
        return dict(zip(links, [{}]*len(links)))

def searchDepth(targetPageId, currentPageId, linkTree, depth):
    if depth == 0:
        return linkTree
    if not linkTree:
        linkTree = constructDict(currentPageId)
        if not linkTree:
            return {}
    if targetPageId in linkTree.keys():
        print("TARGET "+str(targetPageId)+" FOUND")
        raise SolutionFound("PAGE 1: "+str(currentPageId))
    for branchKey, branchValue in linkTree.items():
        try:
            linkTree[branchKey] = searchDepth(targetPageId, branchKey, branchValue, depth-1)
        except SolutionFound as e:
            print('11', e.message)
            raise SolutionFound("PAGE 2: "+str(currentPageId))
    return linkTree

try:
    searchDepth(344, 1, {}, 4)
    print("No solution found")
except SolutionFound as e:
    print('22', e.message)

    #TARGET 344 FOUND
    #11 PAGE 1: 277
    #11 PAGE 2: 3
    #22 PAGE 2: 1