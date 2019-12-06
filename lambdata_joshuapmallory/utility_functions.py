'''List of all of my functions'''


def google_drive_useable(link):
    """Changes a google drive link into something usable"""
    return link.replace('/open?', '/uc?')



def cat_prediction_results(y_train
                          ,y_val
                          ,y_train_pred
                          ,y_val_pred
                          ,cat_target    = 0
                          ,sort_by       = 'prediction'
                                                              ):
    """A way to get my metrics all in one place."""
    if cat_target == 0:
        cat_target = y_train.unique()[0]
    from sklearn.metrics import accuracy_score, precision_score, recall_score

    
    metrics     = {accuracy_score:  'Accuracy'
                  ,precision_score: 'Precision'
                  ,recall_score:    'Recall'
                  }
    
    base_y_pred = [cat_target] * len(y_train)
    
    predictions = [['Baseline'   ,y_train  ,base_y_pred]
                  ,['Training'   ,y_train ,y_train_pred]
                  ,['Validation' ,y_val     ,y_val_pred]
                  ]
    
    if sort_by.lower() == 'prediction' or 'predictions':
        for prediction in predictions:
            for metric in metrics:
                if metrics[metric] == 'Accuracy':
                    print(prediction[0],  str(metrics[metric]) + ':\t', metric(prediction[1], prediction[2]))
                else:
                    print(prediction[0],  str(metrics[metric]) + ':\t', metric(prediction[1], prediction[2], pos_label = cat_target))
            print()
    else:
        for metric in metrics:
            if metrics[metric] == 'Accuracy':
                print("Baseline",   metrics[metric], ':\t', metric(y_train, baseline_y_pred))
                print("Training",   metrics[metric], ':\t', metric(y_train,    train_y_pred))
                print("Validation", metrics[metric], ':\t', metric(y_val,        val_y_pred))
            else:
                print("Baseline",   metrics[metric], ':\t', metric(y_train, baseline_y_pred, pos_label = cat_target))
                print("Training",   metrics[metric], ':\t', metric(y_train,    train_y_pred, pos_label = cat_target))
                print("Validation", metrics[metric], ':\t', metric(y_val,        val_y_pred, pos_label = cat_target))
            print()



# New Functions go here #
