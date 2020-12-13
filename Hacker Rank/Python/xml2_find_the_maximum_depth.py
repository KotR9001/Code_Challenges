import xml.etree.ElementTree as etree

maxdepth = 0
dep = 0
def depth(elem, level):
    global maxdepth
    global dep
    dep += 1
    if dep > maxdepth:
        maxdepth = dep
    dep -= 1
    #print(maxdepth)
    return maxdepth

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)