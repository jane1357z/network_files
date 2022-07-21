import networkx as nx
import numpy as np
import pandas as pd
import matplotlib
import random

import matplotlib.pyplot as plt




############### link to gihab #########################################
# plt.show()
# url = 'https://github.com/jane1357z/network_files/blob/f97b7534cae4eae574f013414236ea9f76e89dfc/house.csv?raw=true'
# df = pd.read_csv(url, sep=',', header=0, engine='python')

#######################################################################

##################### PROJECT #########################################
# def rgb2hex(r,g,b):
#     return "#{:02x}{:02x}{:02x}".format(r,g,b)

# df = pd.read_csv('co_authorship.csv')

# df_authors=df.iloc[1:200, :]

#######################################################################

################### cut aouthor list csv###############################
# fields = pd.read_csv('users_fields.csv')

# authors_list = []
# for el in df_authors.source_id.unique():
#     authors_list.append(el)
# for el in df_authors.target_id.unique():
#     authors_list.append(el)

# authors_list = list(set(authors_list))
# author_field = []

# for j in range(len(fields)):
#     x = fields.loc[j][0]
#     if x in authors_list:
#         author_field.append([x,fields.loc[j][1]])
# ddd = pd.DataFrame(author_field, columns=['author', 'field'])
# ddd.to_csv("cut_author_list.csv", sep=',', encoding='cp1251')

#######################################################################

############### GRAPH #################################################
# df_fields = pd.read_csv('cut_author_list.csv')
# authors = df_fields['author'].to_list()
# fields_list = df_fields['field'].to_list()
# fields_list_unique = list(set(fields_list))
# colors = []
# print(len(fields_list_unique))
# for i in range(len(fields_list_unique)):
#     colors.append(rgb2hex(random.randint(0,255), random.randint(0,255), random.randint(0,255)))



# columns = list(df_authors.columns.values)# Get columns name

# g = nx.empty_graph(0, nx.DiGraph()) #initialize an empty graph

# for i in range(len(columns)-1):
#     g.add_edges_from(zip(df_authors[columns[i]], df_authors[columns[i+1]])) #Create edge between 2 values, between all consecutive coumns


# graph_colors = []
# for r,v in g.nodes(data=True):
#     ind_author = authors.index(r)
#     field_name = fields_list[ind_author]
#     ind_field = fields_list_unique.index(field_name)
#     graph_colors.append(colors[ind_field])
        

# l_ones = []
# for i in range(len(fields_list_unique)):
#     l_ones.append(1)
#     fields_list_unique[i] = str(fields_list_unique[i])

# fig, ax = plt.subplots(1,1)
# plt.subplots_adjust(left=0.5, right=1.5)
# barlist=plt.barh(fields_list_unique, l_ones, align='edge')
# for i in range(len(fields_list_unique)):
#     barlist[i].set_color(colors[i])


# plt.show()

# dg = g.degree()
# dg = np.array([dg[n] for n in g.nodes])
# nx.draw(g, with_labels=False, node_size=dg*80, arrows=True, node_color=graph_colors)

# plt.show()

#######################################################################

#################### MERGE ############################################

# df = pd.read_csv('co_authorship.csv')
# di_fields = pd.read_csv('users_fields_no_commas.csv')
# m = df.merge(di_fields, how='left', on='source_id')
# m.to_csv("merged_co_authorship_field.csv", sep=',', encoding='cp1251')


df = pd.read_csv('merged_co_authorship_field.csv')
di_fields = pd.read_csv('users_attributes.csv')
m = df.merge(di_fields, how='left', on='source_id')
m = m.drop(m.columns[[0]], axis=1) 
m.to_csv("merged_everything.csv", sep=',', encoding='cp1251')
 

#######################################################################