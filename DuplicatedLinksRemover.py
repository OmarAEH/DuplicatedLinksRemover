"""
This script coded by github.com/OmarAEH
Feel free to contact me at anytime.
"""

with open("Links.txt", "r") as rf:
    links = [line.rstrip() for line in rf]
    for link in links:
        if "instagram" in link:
            # Take the link without cut if it's instagram link
            with open("Results.txt", "a") as wff:
                wff.write(link + "\n")
        # Ignore the result if it's facebook link
        elif "facebook" in link:
            continue
        else:
            # Split the link by /
            link = link.split("/")
            try:
                # Check if domain contains ww
                if link[2].index("ww") == 0:
                    # Check if there is digit after ww
                    if link[2][2].isdigit():
                        continue
                    # Check if there is digit after www
                    elif link[2][3].isdigit():
                        continue
                    else:
                        # Take the result, regroup the link and add /
                        clear_link = link[0] + str("//") + link[2] + str("/")
                        with open("Results.txt", "a") as wff:
                            wff.write(clear_link + "\n")
            except:
                # Take the result if the domain not start with ww or www, regroup the link and add /
                clear_link = link[0] + str("//") + link[2] + str("/")
                with open("Results.txt", "a") as wff:
                    wff.write(clear_link + "\n")

uniqlines = set(open('Results.txt').readlines())
fo = open('Results.txt', 'w').writelines(set(uniqlines))
