#!/usr/bin/env python
# This script reads the README.md of the papers, presentations and news, check or create the links to the correct folders

import os
import difflib


years = [2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013]

r_me = "/README.md"

f_papers = "Papers"
f_presentation = "Presentations"
f_news = "In_the_News"

# Adding colours to make things more visually pleasing and understandable
reset = "\033[0m"
title = "\033[1;32m\033[4;32m"
text = "\033[0;32m"
warning = "\033[0;33m"
error = "\033[0;31m"


for year in years:

    ###Papers
    file = open(str(year) + "/" + f_papers + r_me)

    start_link = "https://github.com/GeeeHesso/Perpetuation/tree/master/"
    length_start_link = len(start_link)

    directory_root = []
    directory_name = []

    for root, dirs, files in os.walk(str(year) + "/" + f_papers):
        for d in dirs:
            directory_root.append(root + "/" + d)
            directory_name.append(d)
        break

    line_final = []

    for line in file:
        if line[0] == "*":
            line_link = line[line.find("]") + 1 :]
            if (
                line_link.find("(") != -1
                and line_link.find(")") != -1
                and len(line_link) > length_start_link
            ):  # link should be correct. Test it to be sure

                l1 = line_link[1 : line_link.find(")")]
                l1 = l1.split("/")[-1]
                similarity = 0.0
                for d_n in directory_name:
                    if difflib.SequenceMatcher(None, l1, d_n).ratio() > similarity:
                        similarity = difflib.SequenceMatcher(None, l1, d_n).ratio()
                        directory_name_finish = d_n
                if similarity > 0.8:
                    print(text + str(year) + " good" + reset)
                    pass
                else:
                    print(
                        warning
                        + "Careful! This link:"
                        + line_link
                        + " can be wrong. Please make sure to check it."
                        + reset
                    )

                line_final.append(line)

            else:  # No link so we have to create one
                line_title_f = line[: line.find("]") + 1]
                line_title = line[line.find("[") + 1 : line.find("]")]
                line_title = line_title[line_title.find("*") + 1 :]
                line_title = line_title[: line_title.find("*")]
                similarity = 0.0
                for (
                    d_n
                ) in (
                    directory_name
                ):  # Goes in the dicrectories and try to find the most similar file.
                    if (
                        difflib.SequenceMatcher(None, line_title, d_n).ratio()
                        > similarity
                    ):
                        similarity = difflib.SequenceMatcher(
                            None, line_title, d_n
                        ).ratio()
                        directory_name_finish = d_n

                end_link = (
                    start_link
                    + str(year)
                    + "/"
                    + f_papers
                    + "/"
                    + directory_name_finish
                )

                if similarity < 0.3:
                    print(
                        warning
                        + "Careful! Low similiarity score for link :"
                        + line_title
                        + "toward"
                        + end_link
                        + reset
                    )
                    print(warning + "Please make sure the link is correct" + reset)

                line_final.append(line_title_f + "(" + end_link + ")\n")

        else:
            line_final.append(line)

    file.close()

    file = open(str(year) + "/" + f_papers + r_me, "w")
    for l in line_final:
        file.write(l)

    file.close()

    ###News
    file = open(str(year) + "/" + f_news + r_me)

    start_link = "https://github.com/GeeeHesso/Perpetuation/tree/master/"
    length_start_link = len(start_link)

    directory_root = []
    directory_name = []

    for root, dirs, files in os.walk(str(year) + "/" + f_news):
        for d in dirs:
            directory_root.append(root + "/" + d)
            directory_name.append(d)
        break

    line_final = []

    for line in file:
        if line[0] == "*":
            line_link = line[line.find("]") + 1 :]
            if (
                line_link.find("(") != -1
                and line_link.find(")") != -1
                and len(line_link) > length_start_link
            ):  # link should be correct. Test it to be sure

                l1 = line_link[1 : line_link.find(")")]
                l1 = l1.split("/")[-1]
                similarity = 0.0
                for d_n in directory_name:
                    if difflib.SequenceMatcher(None, l1, d_n).ratio() > similarity:
                        similarity = difflib.SequenceMatcher(None, l1, d_n).ratio()
                        directory_name_finish = d_n
                if similarity > 0.8:
                    print(text + str(year) + " good" + reset)
                    pass
                else:
                    print(
                        warning
                        + "Careful! This link:"
                        + line_link
                        + " can be wrong. Please make sure to check it."
                        + reset
                    )

                line_final.append(line)

            else:  # No link so we have to create one
                line_title_f = line[: line.find("]") + 1]
                line_title = line[line.find("[") + 1 : line.find("]")]
                similarity = 0.0
                for d_n in directory_name:
                    if (
                        difflib.SequenceMatcher(None, line_title, d_n).ratio()
                        > similarity
                    ):
                        similarity = difflib.SequenceMatcher(
                            None, line_title, d_n
                        ).ratio()
                        directory_name_finish = d_n

                end_link = (
                    start_link + str(year) + "/" + f_news + "/" + directory_name_finish
                )

                if similarity < 0.3:
                    print(
                        warning
                        + "Careful! Low similiarity score for link :"
                        + line_title
                        + "toward"
                        + end_link
                        + reset
                    )
                    print(warning + "Please make sure the link is correct" + reset)

                line_final.append(line_title_f + "(" + end_link + ")\n")

        else:
            line_final.append(line)

    file.close()

    file = open(str(year) + "/" + f_news + r_me, "w")
    for l in line_final:
        file.write(l)

    file.close()

    ###Presentation
    file = open(str(year) + "/" + f_presentation + r_me)

    start_link = "https://github.com/GeeeHesso/Perpetuation/tree/master/"
    length_start_link = len(start_link)

    directory_root = []
    directory_name = []

    for root, dirs, files in os.walk(str(year) + "/" + f_presentation):
        for d in dirs:
            directory_root.append(root + "/" + d)
            directory_name.append(d)
        break

    line_final = []

    for line in file:
        if line[0] == "*":
            line_link = line[line.find("]") + 1 :]
            if (
                line_link.find("(") != -1
                and line_link.find(")") != -1
                and len(line_link) > length_start_link
            ):  # link should be correct. Test it to be sure

                l1 = line_link[1 : line_link.find(")")]
                l1 = l1.split("/")[-1]
                similarity = 0.0
                for d_n in directory_name:
                    if difflib.SequenceMatcher(None, l1, d_n).ratio() > similarity:
                        similarity = difflib.SequenceMatcher(None, l1, d_n).ratio()
                        directory_name_finish = d_n
                if similarity > 0.8:
                    print(text + str(year) + " good" + reset)
                    pass
                else:
                    print(
                        warning
                        + "Careful! This link:"
                        + line_link
                        + " can be wrong. Please make sure to check it."
                        + reset
                    )

                line_final.append(line)

            else:  # No link so we have to create one
                line_title_f = line[: line.find("]") + 1]
                line_title = line[line.find("[") + 1 : line.find("]")]
                similarity = 0.0
                for d_n in directory_name:
                    if (
                        difflib.SequenceMatcher(None, line_title, d_n).ratio()
                        > similarity
                    ):
                        similarity = difflib.SequenceMatcher(
                            None, line_title, d_n
                        ).ratio()
                        directory_name_finish = d_n

                end_link = (
                    start_link
                    + str(year)
                    + "/"
                    + f_presentation
                    + "/"
                    + directory_name_finish
                )

                if similarity < 0.3:
                    print(
                        warning
                        + "Careful! Low similiarity score for link :"
                        + line_title
                        + "toward"
                        + end_link
                        + reset
                    )
                    print(warning + "Please make sure the link is correct" + reset)

                line_final.append(line_title_f + "(" + end_link + ")\n")

        else:
            line_final.append(line)

    file.close()

    file = open(str(year) + "/" + f_presentation + r_me, "w")
    for l in line_final:
        file.write(l)

    file.close()
