from datahandler import all_data_loaders

trainpath = 'data/AmazonReviewFull/amazon_review_full_csv/train.csv'
testpath = 'data/AmazonReviewFull/amazon_review_full_csv/test.csv'

train_loader,val_loader,test_loader = all_data_loaders(trainpath,testpath)
print('done')