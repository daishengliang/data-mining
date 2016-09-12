# Mining heterogeneous network

Question 4 (Programming Required): Similarity Search in Heterogeneous Information Network
This task is to write a program to take a heterogeneous network and evaluate similarity queries based on user-provided meta-paths.   The data input is a heterogeneous information network of academic publications, with 4 types: author, venue, paper and term.
 [Data Set (Heterogeneous Version): dblp_4area.zip] In the dataset we have 4 node files named after its corresponding node type and one relation file:
author.txt: contains all the researchers, first column is id, second column is researcher name
venue.txt: contains 20 representative conferences in 4 areas: data mining, database, information retrieval and machine learning.  First column is id, second column is conference name. Venues in different years are combined into the same entity (e.g., SIGMOD'05 and SIGMOD'06 both refer to entity SIGMOD)
paper.txt: contains the papers published in these 20 conferences before 2011
term.txt: contains all the non-stopword unigrams extracted from paper titles
relation.txt, used to store the undirected relations between entities. First column contains an ID of paper, second column contains an ID of the other three types
[Data Set (Homogeneous Version): APVPA_net, APTPA_net] These two files are the relation files of two compressed homogeneous network using meta-path: APVPA and APTPA, respectively. These networks are UNDIRECTED. Both network only contains the relation between authors. Please use these two networks for Personalized Page-Rank. 
The goal is to evaluate similarity queries using three similarity measures: PathSim and Personalized Page-Rank.  The query input is a researcher's name (e.g., Jiawei Han), the output is the top-10 most similar researchers.
Implementation tips can be found in hw1tips.pdf.
Sub-Task 1. Output the top-10 ranked results (i.e., similar researchers) for two authors: "Christos Faloutsos" and "AnHai Doan", using PathSim and Personalized Page-Rank  as measures respectively, taking APVPA (author-paper-venue-paper-author) as meta-path 
Sub-Task 2. Output the top-10 ranked results for two researchers: "Xifeng Yan" and "Jamie Callan", using PathSim and Personalized Page-Rank as measures respectively, but taking APTPA (author-paper-term-paper-author) as meta-path 
