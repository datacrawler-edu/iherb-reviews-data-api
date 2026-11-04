"""Two sequential product review requests; each is a separate billed run."""
import json
from common import start_once, wait_for_dataset, iter_rows

def main():
    for product in ['61864','117074']:
        actor_input={'products':[product],'maxReviews':2,'maxReviewsPerProduct':2,'reviewsWithPhotosOnly':False}
        run_id=start_once(actor_input,maximum_usd=0.01)
        dataset_id=wait_for_dataset(run_id)
        print(json.dumps({'productInput':product,'reviews':list(iter_rows(dataset_id))},ensure_ascii=False))

if __name__=='__main__':main()
