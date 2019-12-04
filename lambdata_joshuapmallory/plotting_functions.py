"""My plotting functions so I don't need to relearn it every time."""

def force_explain(X_train, y_train, X_val, y_val, row):
    """Shap Force Plot Function"""
    
    import category_encoders as ce
    from sklearn.pipeline import make_pipeline
    from sklearn.impute   import SimpleImputer
    from xgboost          import XGBClassifier
    from sklearn.ensemble import RandomForestClassifier
    import shap
    
    
    # Pipeline to process the dataframe for use
    shap_pipe         = make_pipeline(ce.OrdinalEncoder()
                                     ,SimpleImputer(strategy = 'median')
                                     )

    X_train_processed = shap_pipe.fit_transform(X_train)
    X_val_processed   = shap_pipe.transform(X_val)

    # Set the model
    shap_model        = XGBClassifier(n_estimators = 1000
                                     ,n_jobs       = -1
                                     ,random_state = 6
                                     )

    # Take in processed data 
    shap_model.fit(X_train_processed
                  ,y_train
                  ,eval_set              = [(X_val_processed, y_val)]
                  ,eval_metric           = 'auc'
                  ,early_stopping_rounds = 10
                  ,verbose               = False
                  )

    explainer     = shap.TreeExplainer(shap_model)
    
    selected_row  = X_train.iloc[[row]]
    row_processed = shap_pipe.transform(selected_row)
    
    shap.initjs()
    return shap.force_plot(base_value  = explainer.expected_value
                          ,shap_values = explainer.shap_values(row_processed)
                          ,features    = selected_row
                          ,link        = 'logit'
                          )



def pdp_isolate_explain(X, y, feature):
    """PDP Isolate Function"""
    
    import category_encoders as ce
    from sklearn.pipeline import make_pipeline
    from sklearn.impute   import SimpleImputer
    from sklearn.ensemble import RandomForestClassifier
    from pdpbox.pdp       import pdp_isolate, pdp_plot

    
    # Encode, impute as needed
    X_encoded   = ce.OrdinalEncoder().fit_transform(X)
    X_processed = SimpleImputer().fit_transform(X_encoded)

    # Pick a model and fit the data
    pdp_model = RandomForestClassifier(n_estimators = 200
                                      ,n_jobs       = -1
                                      ,random_state = 6
                                      )
    pdp_model.fit(X_processed
                 ,y
                 )

    # The actual plotting
    pdp_isolate = pdp_isolate(model          = pdp_model
                             ,dataset        = X_encoded
                             ,model_features = X_encoded.columns
                             ,feature        = feature
                             )
    pdp_plot(pdp_isolate
            ,feature_name = feature
            ,plot_lines   = True
            ,frac_to_plot = 100
            )



def pdp_interact_explain(X, y, feature):
    """PDP Interact Fucntion"""
    
    import category_encoders as ce
    from sklearn.pipeline import make_pipeline
    from sklearn.impute   import SimpleImputer
    from sklearn.ensemble import RandomForestClassifier
    from pdpbox.pdp       import pdp_interact, pdp_interact_plot

    
    # Encode, impute as needed
    X_encoded   = ce.OrdinalEncoder().fit_transform(X)
    X_processed = SimpleImputer().fit_transform(X_encoded)

    # Pick a model and fit the data
    pdp_model = RandomForestClassifier(n_estimators = 200
                                      ,n_jobs       = -1
                                      ,random_state = 6
                                      )
    pdp_model.fit(X_processed
                 ,y
                 )

    # The actual plotting
    pdp_interact = pdp_interact(model          = pdp_model
                               ,dataset        = X_encoded
                               ,model_features = X_encoded.columns
                               ,features       = feature
                               )
    # There's a TypeError in the pdpinteract code that prevents the axes from getting labels
    # and I can't be bothered to go fix their mistakes.
    # This ignores it and lets it continue with the plotting
    try:
        pdp_interact_plot(pdp_interact
                         ,feature_names = feature
                         ,plot_type     = 'contour'
                         )
    except:
        pass



# New Functions go here #
