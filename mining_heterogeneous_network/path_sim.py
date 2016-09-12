# -*- coding: utf-8 -*-
"""PathSim algorithm for evaluating similarity of queries.

This module takes a heterogeneous network and evaluate similarity
of queries based on user-provided meta-paths.

Example:

    To run the code::

        $ python page_sim.py

@author: ShengliangDai

"""

import pprint
import pandas as pd
import numpy as np

# pylint: disable=invalid-name
# pylint: disable=no-member
# pylint: disable=redefined-outer-name

dblp = './dblp_4area/'
author = pd.read_table(dblp + 'author.txt',
                       header=None).rename(columns={0: 'id', 1: 'name'})
paper = pd.read_table(dblp + 'paper.txt',
                      header=None).rename(columns={0: 'id', 1: 'name'})
relation = pd.read_table(dblp + 'relation.txt',
                         header=None).rename(columns={0: 'id', 1: 'avt'})
term = pd.read_table(
    dblp + 'term.txt', header=None).rename(columns={0: 'id', 1: 'name'})
venue = pd.read_table(dblp + 'venue.txt',
                      header=None).rename(columns={0: 'id', 1: 'name'})


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
# Build the dictionary for converting original id to index from 0 to len(args)
authorIndex = convertToIndex(author.id)
venueIndex = convertToIndex(venue.id)
termIndex = convertToIndex(term.id)
paperIndex = convertToIndex(np.unique(paper.id))


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
# Build the dictionary for converting index from 0 to len(args) to original id
authorID = convertToID(author.id)
venueID = convertToID(venue.id)
termID = convertToID(term.id)
paperID = convertToID(np.unique(paper.id))


def buildAVMatrix(relation):
    r = relation.values
    index = 0
    Author = []
    Venue = []
    AVMatrix = np.zeros([len(author), len(term)], dtype=int)
    for i in range(len(r)):
        pid = r[i][0]
        avt = r[i][1]
        if pid not in paperIndex:
            index += 1
            continue
        if paperIndex[pid] == index:
            if avt in authorIndex:
                Author.append(r[i][1])
            elif avt in venueIndex:
                Venue.append(avt)
        else:  # the next paper id
            index += 1
            for a in Author:
                for v in Venue:
                    AVMatrix[authorIndex[a]][venueIndex[v]] = 1
            if index < len(np.unique(paper.id)):
                Author = []
                Venue = []
                if avt in authorIndex:
                    Author.append(avt)
                elif avt in venueIndex:
                    Venue.append(avt)

    return AVMatrix


def buildATMatrix(relation):
    ATMatrix = np.zeros([len(author), len(term)], dtype=int)
    r = relation.values
    index = 0
    Author = []
    Term = []
    for i in range(len(r)):
        pid = r[i][0]
        avt = r[i][1]
        if pid not in paperIndex:
            index += 1
            continue
        if paperIndex[pid] == index:
            if avt in authorIndex:
                Author.append(r[i][1])
            elif avt in termIndex:
                Term.append(avt)
        else:  # the next paper id
            index += 1
            for a in Author:
                for t in Term:
                    ATMatrix[authorIndex[a]][termIndex[t]] = 1
            if index < len(np.unique(paper.id)):
                Author = []
                Term = []
                if avt in authorIndex:
                    Author.append(avt)
                elif avt in termIndex:
                    Term.append(avt)

    return ATMatrix

AuthorVenue = buildAVMatrix(relation)
AuthorTerm = buildATMatrix(relation)


def pathSim(adjMatrix, query):
    """PathSim algorithm.

    Args:
        adjMatrix: An adjacency matrix for authors.
        query: The name of one author.

    Returns:
        The similarity score between this author and other authors.

    """
    authorMatrix = author.values
    for i in range(len(author)):
        if authorMatrix[i][1] == query:
            queryID = authorMatrix[i][0]

    queryIndex = authorIndex[queryID]
    x = queryIndex
    score = np.zeros(len(author))
    for y in range(len(adjMatrix)):
        pathsim = 2.0 * np.dot(adjMatrix[x][:], adjMatrix[y][:]) / (np.dot(
            adjMatrix[x][:], adjMatrix[x][:]) + np.dot(adjMatrix[y][:], adjMatrix[y][:]))
        score[y] = pathsim

    return score

#---------------------------------------------------
# Subtask 1
score = pathSim(AuthorVenue, 'Christos Faloutsos')
TopAuthorID = score.argsort()[-10:]
TopScore = score[score.argsort()[-10:]]

ans = []
for i in TopAuthorID:
    ans.append(list(author.name[author.id == authorID[i]].values))
res = zip(ans, TopScore)
for i, j in res[::-1]:
    print i, j
print '\n'

#---------------------------------------------------
score = pathSim(AuthorVenue, 'AnHai Doan')
TopAuthorID = score.argsort()[-10:]
TopScore = score[score.argsort()[-10:]]

ans = []
for i in TopAuthorID:
    ans.append(list(author.name[author.id == authorID[i]].values))
res = zip(ans, TopScore)
for i, j in res[::-1]:
    print i, j
print '\n'

#---------------------------------------------------
# Subtask 2
score = pathSim(AuthorTerm, 'Xifeng Yan')
TopAuthorID = score.argsort()[-10:]
TopScore = score[score.argsort()[-10:]]

ans = []
for i in TopAuthorID:
    ans.append(list(author.name[author.id == authorID[i]].values))
res = zip(ans, TopScore)
for i, j in res[::-1]:
    print i, j
print '\n'

#---------------------------------------------------
score = pathSim(AuthorTerm, 'Jamie Callan')
TopAuthorID = score.argsort()[-10:]
TopScore = score[score.argsort()[-10:]]

ans = []
for i in TopAuthorID:
    ans.append(list(author.name[author.id == authorID[i]].values))
res = zip(ans, TopScore)
for i, j in res[::-1]:
    print i, j
print '\n'
