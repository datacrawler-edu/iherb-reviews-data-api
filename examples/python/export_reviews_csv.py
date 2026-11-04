"""Export existing review Dataset rows to CSV without starting another Actor run."""
import argparse
import csv
from common import iter_rows

FIELDS=['productId','reviewId','rating','title','text','date','language','verifiedPurchase','helpfulYes','helpfulNo','productUrl']

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dataset_id')
    parser.add_argument('--output',default='data/exported-reviews.csv')
    args=parser.parse_args()
    count=0
    with open(args.output,'w',encoding='utf-8-sig',newline='') as file:
        writer=csv.DictWriter(file,fieldnames=FIELDS);writer.writeheader()
        for row in iter_rows(args.dataset_id):
            writer.writerow({k:row.get(k) for k in FIELDS});count+=1
    print('Exported '+str(count)+' rows to '+args.output)

if __name__=='__main__':main()
