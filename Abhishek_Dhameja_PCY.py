import sys
import itertools
import os

def getSingleFrequentItems(baskets):
    countTable={}
    result=[]
    allItems=[]
    for basket in baskets:
        for item in basket:
            countTable.setdefault(item,0)
            countTable[item]+=1
    for item,count in countTable.iteritems():
        #print item,count
        allItems.append(int(item))
        if count>=s:
            result.append(int(item))
    # print countTable
    return sorted(result),sorted(allItems)

def computeHashTable(allPairs,baskets):
    h={}
    frequentHashes=[]
    for pair in allPairs:
        #print (pair[0]*a+pair[1]*b)%N
        h.setdefault((pair[0]*a+pair[1]*b)%N,0)
        for basket in baskets:
            if pair[0] in basket and pair[1] in basket:
                h[(pair[0]*a+pair[1]*b)%N]+=1
    for hash,count in h.iteritems():
        if count>=s:
            frequentHashes.append(hash)
    return h,frequentHashes

def getAllCandidates(singleFrequentItems,frequentbuckets,allPairs):
    candidates=[]
    rejected=[]
    for item in singleFrequentItems:
        candidates.append(item)
    for pair in allPairs:
        if (pair[0]*a+pair[1]*b)%N in frequentbuckets and pair[0] in singleFrequentItems and pair[1] in singleFrequentItems:
            candidates.append(pair)
        if (pair[0]*a+pair[1]*b)%N not in frequentbuckets and pair[0] in singleFrequentItems and pair[1] in singleFrequentItems:
            rejected.append(pair)
    return candidates,sorted(rejected)

def getAllFrequents(allCandidates,baskets):
    frequents=[]
    #rejected=[]
    counttable={}
    for candidate in allcandidates:
        if type(candidate) is tuple:
            #print 'candidate:',candidate
            counttable.setdefault(candidate,0)
            for basket in baskets:
                if candidate[0] in basket and candidate[1] in basket:
                    counttable[candidate]+=1
        else:
            frequents.append(candidate)
    for candidate,count in counttable.iteritems():
        if counttable[candidate]>=s:
            frequents.append(candidate)
        # else:
        #     rejected.append(candidate)
    return sorted(frequents)

if __name__ == '__main__':
    if len(sys.argv) != 7:
        print 'Usage: python Abhishek_Dhameja_PCY.py <a> <b> <N> <s> <output-dir>'
        exit(-1)
    inputfile=open(sys.argv[1])
    a=int(sys.argv[2])
    b=int(sys.argv[3])
    N=int(sys.argv[4])
    s=int(sys.argv[5])
    outputfilepath=sys.argv[6]
    baskets=[]

    lines = inputfile.readlines()
    for line in lines:
        line=line.strip().split(',')
        line=map(int,line)
        baskets.append(line)
    #print len(baskets)
    hashtable={}
    singleFrequentItems,singleItems=getSingleFrequentItems(baskets)
    # print 'single frequent items:',singleFrequentItems
    allPairs=[]
    for pair in itertools.combinations(singleItems,2):
        allPairs.append(pair)

    #getPairCounts()
    hashtable,frequentbuckets=computeHashTable(allPairs,baskets)


    #print 'baskets:',baskets
    # print 'hashtable:',hashtable
    # print 'frequent buckets:',frequentbuckets
    allcandidates,rejected=getAllCandidates(singleFrequentItems,frequentbuckets,allPairs)
    # print 'all candidates:',allcandidates
    frequents=getAllFrequents(allcandidates,baskets)

    # print 'all pairs:', allPairs
    # print 'frequents:',frequents
    # print 'rejected:',rejected
    #print baskets


    if not os.path.exists(outputfilepath):
        os.mkdir(outputfilepath)
    f = open(os.path.join(outputfilepath, 'frequentset.txt'), 'w')
    for item in frequents:
        if type(item) is tuple:
            f.write("("+str(item[0])+","+str(item[1])+")" +"\n")
        else:
            f.write(str(item) + "\n")
    f.close()

    f = open(os.path.join(outputfilepath, 'candidates.txt'), 'w')
    for item in rejected:
        if type(item) is tuple:
            f.write("("+str(item[0])+","+str(item[1])+")" +"\n")
        else:
            f.write(str(item) + "\n")
    f.close()

    print 'False Positive Rate:', ("%0.3f") % (float(len(frequentbuckets)) / N)
    #print 'end'