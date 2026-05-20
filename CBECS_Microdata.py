import csv
import statistics

pba_codes = {
    '1':  'Vacant',
    '2':  'Office',
    '4':  'Laboratory',
    '5':  'Nonrefrigerated warehouse',
    '6':  'Food sales',
    '7':  'Public order and safety',
    '8':  'Outpatient health care',
    '11': 'Refrigerated warehouse',
    '12': 'Religious worship',
    '13': 'Public assembly',
    '14': 'Education',
    '15': 'Food service',
    '16': 'Inpatient health care',
    '17': 'Nursing',
    '18': 'Lodging',
    '23': 'Strip shopping center',
    '24': 'Enclosed mall',
    '25': 'Retail other than mall',
    '26': 'Service',
    '91': 'Other'
}

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "cbecs2018_final_public.csv"
fh = open(fname)
reader = csv.reader(fh)
headers = next(reader)
mfbtu_idx = headers.index('MFBTU')
sqft_idx = headers.index('SQFT')
pba_idx = headers.index('PBA')
cendiv_idx = headers.index('CENDIV')
eui_by_type = dict()
results = dict()

for row in reader:
    try:
        if row[cendiv_idx] != '9':
            continue
        pba = row[pba_idx]
        sqft = float(row[sqft_idx])
        mfbtu = float(row[mfbtu_idx])
        if sqft <= 0:
            continue
        eui = mfbtu / sqft
        if pba not in eui_by_type:
            eui_by_type[pba] = []
        eui_by_type[pba].append(eui)
    except:
        continue

#print(eui_by_type)
all_pacific_euis = []
for euis in eui_by_type.values():
    all_pacific_euis.extend(euis)
#print(all_pacific_euis)
pacific_median = statistics.median(all_pacific_euis)
#print(median_eui)
for pba, euis in eui_by_type.items():
    name = pba_codes[pba]
    median_eui = statistics.median(euis)
    count = len(euis)
    results[name] = (count, round(median_eui, 1))

sorted_results = sorted(results.items(), key=lambda x: x[1][1], reverse=True)
#print(sorted_results)

print(f"Pacific Division (CENDIV 9) - Median EUI by Building Type")
print(f"{'Rank':<6} {'Building Type':<35} {'Buildings':>10} {'Median EUI':>12}")
print("-" * 66)
for rank, (name, (count, median)) in enumerate(sorted_results, 1):
    if median > pacific_median:
        print(f"{rank:<6} *** {name:<31} {count:>10} {median:>12.1f}")
    else:
        print(f"{rank:<6}     {name:<31} {count:>10} {median:>12.1f}")
print("-" * 66)
print(f"Pacific division median EUI (all types): {round(pacific_median, 1)}")