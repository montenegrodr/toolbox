import csv


def main():
    filepath = '/home/robson/Documents/new/plan.csv'
    uniques = '/home/robson/Documents/new/uniques.csv'
    ambiguous = '/home/robson/Documents/new/ambiguous.csv'
    repeated = '/home/robson/Documents/new/repeated.csv'


    rows = []
    rep_rows = []
    amb_rows = []
    uni_rows = []

    with open(filepath, 'r') as fp:
        reader = csv.reader(fp)
        for i, row in enumerate(reader):
            rows.append(row)

    rows = sorted(rows, key=lambda x: x[4])

    for i, r1 in enumerate(rows):
        print '{}/{}/{} {}'.format(len(rep_rows), len(uni_rows), len(amb_rows), i)
        inserted = False
        doi1 = r1[4].lstrip('http://dx.doi.org/').lower()
        title1 = r1[1].lower().strip()
        year1 = r1[0].strip()

        for j, r2 in enumerate(rows):
            if i == j:
                continue

            doi2 = r2[4].lstrip('http://dx.doi.org/').lower()
            title2 = r2[1].lower().strip()
            year2 = r2[0].strip()

            if doi1 == doi2 and doi1 and doi2:
                if doi1 not in [t[4].lstrip('http://dx.doi.org/').lower() for t in uni_rows]:
                    uni_rows.append(r1)
                else:
                    rep_rows.append(r1)
                inserted = True
                break
            elif title1 == title2 and title1 and title2:
                if year1 == year2 and year1 and year2:
                    amb_rows.append(r1)
                else:
                    uni_rows.append(r1)
                inserted = True
                break
        if not inserted:
            uni_rows.append(r1)

    uni_rows =  sorted(uni_rows, key=lambda x: x[4])
    rep_rows =  sorted(rep_rows, key=lambda x: x[4])
    amb_rows =  sorted(amb_rows, key=lambda x: x[4])

    with open(uniques, 'w') as fp:
        writer = csv.writer(fp)
        writer.writerows(uni_rows)

    with open(repeated, 'w') as fp:
        writer = csv.writer(fp)
        writer.writerows(rep_rows)

    with open(ambiguous, 'w') as fp:
        writer = csv.writer(fp)
        writer.writerows(amb_rows)

if __name__=='__main__':
    main()