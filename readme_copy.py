#!/usr/bin/env python
# This script takes the information of the README on the last level and copies it into the yearly README and general README

years = [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013]


f_papers = '/Papers/README.md'
f_presentation = '/In_the_News/README.md'
f_news = '/Presentations/README.md'

all_text_papers = ['\n## Publications\n']
all_text_presentation = ['\n## List of presentations\n']
all_text_news = ['\n## In the News\n']

for year in years:
    file1 = open(str(year)+f_papers)
    file2 = open(str(year)+f_presentation)
    file3 = open(str(year)+f_news)

    out_text = ['# Perpetuation', '\n', '\n', '## ' +
                str(year), '\n', '\n', 'Contains the publications, presentations and other documents pertaining to the group\'s research and projects.', '\n', '\n']

    out_text.append('### Publications')
    out_text.append('\n')
    out_text.append('\n')
    all_text_papers.append('\n### '+str(year)+'\n')

    num = 0
    for line in file1:
        if(line[0] == '*'):
            out_text.append(line)
            all_text_papers.append(line)
            num += 1

    if num == 0:
        out_text.append('* None for now\n')
        # all_text_papers.append('* None for now\n')
        all_text_papers.pop()

    out_text.append('\n')
    out_text.append('### In the News')
    out_text.append('\n')
    out_text.append('\n')
    all_text_news.append('\n### '+str(year)+'\n')

    num = 0
    for line in file2:
        if(line[0] == '*'):
            out_text.append(line)
            all_text_news.append(line)
            num += 1

    if num == 0:
        out_text.append('* None for now\n')
        # all_text_news.append('* None for now\n')
        all_text_news.pop()

    out_text.append('\n')
    out_text.append('### List of presentations')
    out_text.append('\n')
    out_text.append('\n')
    all_text_presentation.append('\n### '+str(year)+'\n')

    num = 0
    for line in file3:
        if(line[0] == '*'):
            out_text.append(line)
            all_text_presentation.append(line)
            num += 1

    if num == 0:
        out_text.append('* None for now\n')
        # all_text_presentation.append('* None for now\n')
        all_text_presentation.pop()

    file_out = open(str(year)+'/README.md', 'w')

    for line in out_text:
        file_out.write(line)

file_all = open('README.md', 'w')

file_all.write('# Perpetuation\n')
file_all.write(
    'Contains the publications, presentations and other documents pertaining to the group\'s research and projects.\n')

if(len(all_text_papers) > 1):
    for l in all_text_papers:
        file_all.write(l)
if(len(all_text_news) > 1):
    for l in all_text_news:
        file_all.write(l)
if(len(all_text_presentation) > 1):
    for l in all_text_presentation:
        file_all.write(l)
