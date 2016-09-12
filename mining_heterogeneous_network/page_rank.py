# -*- coding: utf-8 -*-
"""PageRank algorithm for evaluating similarity of queries.

This module take a heterogeneous network and evaluate similarity
of queries based on user-provided meta-paths.


Example:
    To run the code::

        $ python page_rank.py


@author: ShengliangDai

"""

import pprint
import pandas as pd
import numpy as np

# pylint: disable=invalid-name
# pylint: disable=no-member
# pylint: disable=redefined-outer-name

dblp = './dblp_4area/'
author = pd.read_table(dblp + 'author.txt', header=None)
paper = pd.read_table(dblp + 'paper.txt', header=None)
relation = pd.read_table(dblp + 'relation.txt', header=None)
term = pd.read_table(dblp + 'term.txt', header=None)
venue = pd.read_table(dblp + 'venue.txt', header=None)
APVPA = pd.read_table('APVPA.txt', header=None)
APTPA = pd.read_table('APTPA.txt', header=None)

author = author.rename(columns={0: 'id', 1: 'name'})
author = author.reset_index()


def convertToIndex(names):
    """Convert strings to indices.

    Args:
        names: A list of strings.

    Returns:
        A dictionary mapping strings to indices.

    """
    index = 0
    dic = {}
    for name in names:
        dic[name] = index
        index += 1
    return dic
authorIndex = convertToIndex(author.id)


def convertToID(names):
    """Convert indices to strings.

    Args:
        names: A list of strings.

    Returns:
        A dictionary mapping indices to strings.

    """
    index = 0
    dic = {}
    for name in names:
        dic[index] = name
        index += 1
    return dic
authorID = convertToID(author.id)


def buildAdjacencyMatrix(metapath):
    """Build adjacency matrix.

    Args:
        metapath: A matrix containing the meta-paths information.

    Returns:
        An adjacency matrix for authors.

    """
    adjMatrix = np.empty([len(author), len(author)], dtype=int)
    metapath = metapath.values
    for i in range(len(metapath)):
        author0 = metapath[i][0]
        author1 = metapath[i][1]
        author0Index = authorIndex[author0]
        author1Index = authorIndex[author1]
        adjMatrix[author0Index][author1Index] = 1
        adjMatrix[author1Index][author0Index] = 1
    return adjMatrix

adjAPVPA = buildAdjacencyMatrix(APVPA)

print 'APVPA'
pprint.pprint(adjAPVPA)

adjAPTPA = buildAdjacencyMatrix(APTPA)

print 'APTPA'
pprint.pprint(adjAPTPA)


def pageRank(adjMatrix, query):
    """PageRank algorithm.

    Args:
        adjMatrix: An adjacency matrix for authors..
        query: The name of one author.

    Returns:
        The similarity score between this author and other authors.

    """
    c = 0.15
    t = 10
    v = [1.0 / len(adjMatrix)] * len(adjMatrix)
    u = np.zeros(len(adjMatrix))
    query = int(author.id[author.name == query])
    u[authorIndex[query]] = 1
    while t > 0:
        # normalize adjacency matrix
        adjMatrix = 1.0 * adjMatrix / adjMatrix.sum(axis=1)[:, np.newaxis]
        t -= 1
        v = (1 - c) * np.dot(adjMatrix.T, v) + c * u
    return v

#---------------------------------------------------
# Subtask 1
score = pageRank(adjAPVPA, 'Christos Faloutsos')
TopAuthorID = score.argsort()[-10:]
TopScore = score[score.argsort()[-10:]]

ans = []
for i in TopAuthorID:
    ans.append(list(author.name[author.id == authorID[i]].values))
res = zip(ans, TopScore)
for i, j in res[::-1]:
    print i, j

#---------------------------------------------------
score = pageRank(adjAPVPA, 'AnHai Doan')
TopAuthorID = score.argsort()[-10:]
TopScore = score[score.argsort()[-10:]]

ans = []
for i in TopAuthorID:
    ans.append(list(author.name[author.id == authorID[i]].values))
res = zip(ans, TopScore)
for i, j in res[::-1]:
    print i, j


#---------------------------------------------------
# Subtask 2
score = pageRank(adjAPTPA, 'Xifeng Yan')
TopAuthorID = score.argsort()[-10:]
TopScore = score[score.argsort()[-10:]]

ans = []
for i in TopAuthorID:
    ans.append(list(author.name[author.id == authorID[i]].values))
res = zip(ans, TopScore)
for i, j in res[::-1]:
    print i, j

#---------------------------------------------------
score = pageRank(adjAPTPA, 'Jamie Callan')
TopAuthorID = score.argsort()[-10:]
TopScore = score[score.argsort()[-10:]]

ans = []
for i in TopAuthorID:
    ans.append(list(author.name[author.id == authorID[i]].values))
res = zip(ans, TopScore)
for i, j in res[::-1]:
    print i, j
