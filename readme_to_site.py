#!/usr/bin/env python

# This script take the general README and turns in into several json file.
# The json file created can then be used for the website

import json
import os


def read_comment(comments, entry, dictionnay, file):
    '''
    Read the comments present in the README for additional informations
    comments;   comments to look for and read in the the README
    entry;      key of the dictionary where the information will be stored
    dictionary; self-explanatory
    file;       path to the README
    '''
    try:
        f_readme = open(file)
        for line in f_readme:
            for comm, key in zip(comments, entry):
                if line.lower().startswith(comm) and len(line[len(comm)+1:-4]) > 3:
                    dictionnay[key] = line[len(comm)+1:-4]

    except:
        # print(error+"Unable to open ", file,reset)
        print('error')
        print(file)


# Adding colours to make things more visually pleasing and understandable
reset = '\033[0m'
title = '\033[1;32m\033[4;32m'
text = '\033[0;32m'
warning = '\033[0;33m'
error = '\033[0;31m'

file = open('README.md')


state = 0
# 0 None
# 1 publication
# 2 in the news
# 3 presentations

publication = []
news = []
presentations = []
year = 0
for line in file:

    if line.find("## Publications") != -1:
        state = 1
    elif line.find("## In the News") != -1:
        state = 2
    elif line.find("## List of presentations") != -1:
        state = 3

    if line.find("###") != -1:
        for y in [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012]:
            if line.find(str(y)) != -1:
                year = y

    if line.startswith('*'):
        if state == 1:
            publication.append([line, str(year)])
        elif state == 2:
            news.append([line, str(year)])
        elif state == 3:
            presentations.append([line, str(year)])


publication_list = []

all_publication_dict = {}

all_publication_dict['publication'] = {}

count = 0
index = 0
for p_all in publication:
    # print(p)
    p = p_all[0]
    part_1 = p[p.find('[')+1:p.find(']')]
    part_2 = p[p.find(']')+2:-2]
    # print(part_1)
    # print(part_2)

    publication_dict = {}
    publication_dict['authors'] = part_1[:part_1.find('*')].rstrip(', ')
    publication_dict['title'] = part_1[part_1.find(
        '*')+1:part_1.find('*', part_1.find('*')+1)].rstrip(', ')

    try:
        publication_dict['publisher'] = part_1[part_1.find(
            '*', part_1.find('*')+1)+3:part_1.find('(')].rstrip(', ')
    except:
        publication_dict['publisher'] = ''

    try:
        publication_dict['date'] = p_all[1]
    except:
        publication_dict['date'] = ''

    publication_dict['display'] = part_1

    display_temp = publication_dict['display']

    for _ in range(3):
        display_temp = display_temp.replace('**', '<b>', 1)
        display_temp = display_temp.replace('**', '</b>', 1)

    for _ in range(3):
        display_temp = display_temp.replace('*', '<i>', 1)
        display_temp = display_temp.replace('*', '</i>', 1)

    publication_dict['display'] = display_temp

    part_2 = part_2.replace('tree', 'blob', 1)
    # print(part_2[part_2.find('master')+6:])

    name_pdf = ''
    name_readme = ''

    for root, dirs, files in os.walk(part_2[part_2.find('master')+7:]):
        for name in files:
            if root == part_2[part_2.find('master')+7:]:
                # print(name)
                if name.endswith('.pdf'):
                    name_pdf = name
                elif name.endswith('.md'):
                    name_readme = name

    part_2_root = part_2 + '/'

    if len(name_pdf) > 3:
        publication_dict['url'] = part_2_root+name_pdf
    else:
        publication_dict['url'] = part_2

    publication_dict['tags'] = ''

    if len(name_readme) > 3:
        # print(part_2_root + name_readme)
        try:
            file_name = part_2[part_2.find('master')+7:] + '/' + name_readme

            read_comment(['<!-- keywords:'], ['tags'],
                         publication_dict, file_name)

        except:
            print(error+"Unable to open " + part_2_root+name_readme+reset)

    else:
        print(warning+"WARNING! No ReadMe for " + part_2_root + reset)

    name = 'p_' + (str(count).zfill(2))
    count += 1
    all_publication_dict['publication'][name] = publication_dict


with open('pub.json', 'w') as fp:
    json.dump(all_publication_dict, fp, indent=4, sort_keys=True)

##############

all_news_dict = {}
all_news_dict['news'] = {}

count = 0


for n_all in news:
    n = n_all[0]
    part_1 = n[n.find('[')+1:n.find(']')]
    part_2 = n[n.find(']')+2:n.find(')')]

    news_dict = {}
    news_dict['authors'] = ''
    news_dict['title'] = part_1[:part_1.find('*')].rstrip(', ')

    news_dict['publisher'] = part_1[part_1.find(
        '*')+1:part_1.find('*', part_1.find('*')+1)].rstrip(', ')
    news_dict['date'] = n_all[1]
    news_dict['tags'] = ''
    news_dict['display'] = part_1
    news_dict['url'] = part_2

    display_temp = news_dict['display']

    display_temp = display_temp.replace('*', '<b>', 1)
    display_temp = display_temp.replace('*', '</b>', 1)

    news_dict['display'] = display_temp

    name_readme = ''

    for root, dirs, files in os.walk(part_2[part_2.find('master')+7:]):
        for name in files:
            if root == part_2[part_2.find('master')+7:]:
                # print(name)
                if name.endswith('.pdf'):
                    name_pdf = name
                elif name.endswith('.md'):
                    name_readme = name

    part_2_root = part_2 + '/'

    news_dict['tags'] = ''

    if len(name_readme) > 3:
        file_name = part_2[part_2.find('master')+7:] + '/' + name_readme

        read_comment(['<!-- keywords:', '<!-- link:'],
                     ['tags', 'url'], news_dict, file_name)
    else:
        print(warning+"WARNING! No ReadMe for " + part_2_root + reset)

    name = 'n_'+(str(count).zfill(2))
    count += 1
    all_news_dict['news'][name] = news_dict

with open('news.json', 'w') as fp:
    json.dump(all_news_dict, fp, indent=4, sort_keys=True)


#################

all_presentations_dict = {}
all_presentations_dict['presentations'] = {}

count = 0


for pr_all in presentations:
    pr = pr_all[0]
    part_1 = pr[pr.find('[')+1:pr.find(']')]
    part_2 = pr[pr.find(']')+2:pr.find(')')]

    pres_dict = {}
    pres_dict['authors'] = ''
    #pres_dict['title']=part_1[:part_1.find('*')].rstrip(', ')
    # Remove the * for cleaner display
    pres_dict['title'] = part_1.replace('*', '')

    pres_dict['publisher'] = part_1[part_1.find(
        '*')+1:part_1.find('*', part_1.find('*')+1)].rstrip(', ')
    pres_dict['date'] = pr_all[1]
    pres_dict['tags'] = ''
    pres_dict['display'] = part_1
    pres_dict['url'] = part_2

    display_temp = pres_dict['display']

    display_temp = display_temp.replace('*', '<b>', 1)
    display_temp = display_temp.replace('*', '</b>', 1)

    pres_dict['display'] = display_temp

    name_readme = ''

    for root, dirs, files in os.walk(part_2[part_2.find('master')+7:]):
        for name in files:
            if root == part_2[part_2.find('master')+7:]:
                # print(name)
                if name.endswith('.pdf'):
                    name_pdf = name
                elif name.endswith('.md'):
                    name_readme = name

    part_2_root = part_2 + '/'

    pres_dict['tags'] = ''

    if len(name_readme) > 3:
        # print(part_2_root + name_readme)
        try:
            file_name = part_2[part_2.find('master')+7:] + '/' + name_readme

            read_comment(['<!-- keywords:', '<!-- link:'],
                         ['tags', 'url'], pres_dict, file_name)
        except:
            print(error+"Unable to open " + part_2_root+name_readme+reset)

    else:
        print(warning+"WARNING! No ReadMe for " + part_2_root+reset)

    name = 'p_'+(str(count).zfill(2))
    count += 1
    all_presentations_dict['presentations'][name] = pres_dict

with open('pres.json', 'w') as fp:
    json.dump(all_presentations_dict, fp, indent=4, sort_keys=True)
