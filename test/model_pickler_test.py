
# # the beginning
# df = pd.read_csv('data_real_state_analysis.csv')
#
#
# # Preporcessing data - Cleaning
# def cleaning_data(df):
#
#     df = df.dropna(subset=['actual_price'])
#
#     df = df.dropna(subset=['area'])
#
#     df = df.dropna(subset=['building_condition'])
#
#     df = df.drop_duplicates(subset=['prop_id'])
#
#     df = df.fillna(0)
#     #Now we add the price by m2
#     df['price_x_m2'] = df['actual_price'] / df['area']
#     df = df.drop(columns=['point_of_interest', 'subtype', 'old_price_value', 'room_number',
#            'statistics_bookmark_count', 'statistics_view_count', 'creation_date',
#            'expiration_date', 'last_modification_date', 'kitchen_equipped', 'furnished', 'fireplace',
#            'terrace', 'terrace_area', 'garden', 'garden_area', 'land_surface',
#            'facade_count', 'swimming_pool', 'building_condition', 'price_x_m2', 'location_lat',
#             'location_lon', 'location'])
#     return df
#
# def classification_by_type(df):
#     #This are the houses.
#     df_houses = df.loc[df['type']=='HOUSE']
#     df_office = df.loc[df['type']=='OFFICE']
#     df_industry = df.loc[df['type']=='INDUSTRY']
#     df_apartment = df.loc[df['type']=='APARTMENT']
#     return df_houses, df_office, df_industry, df_apartment
#
# def classification_by_region(df):
#     df_brussels = df.loc[df['region']=='Brussels']
#     df_flanders = df.loc[df['region']=='Flanders']
#     df_wallonie = df.loc[df['region']=='Wallonie']
#     return df_brussels, df_flanders, df_wallonie
#
# df = cleaning_data(df)
#
# df_houses, df_office, df_industry, df_apartment = classification_by_type(df)
#
# df_h_brus, df_h_fla, df_h_wal = classification_by_region(df_houses)
#
# df_h_brus = df_h_brus.drop(df_h_brus.loc[df_h_brus['area']>2500].index)
#
#
# # Preparing model
#
# y = df_h_brus['actual_price'].to_numpy()
#
# X = df_h_brus['area'].to_numpy()
#
# f"X shape: {X.shape}; y shape {y.shape}"
#
#
# X = X.reshape(282,1)
# y = y.reshape(282,1)
#
#
# ## Plotting to check
# # plt.figure(figsize=(10, 6))
# # plt.scatter(X, y)
# # plt.ylabel('price')
# # plt.xlabel('area')
#
#
# # Training model
# X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=20, test_size=0.2)
#
#
# ## Plotting to check
# # plt.figure(figsize=(10, 6))
# # plt.scatter(X_train, y_train, label='train')
# # plt.scatter(X_test, y_test, label='test')
# # plt.ylabel('price')
# # plt.xlabel('area')
# # plt.legend()
#
# #The purpose of the pipeline is to assemble several steps that can be cross-validated together
# #while setting different parameters.
#
# pipe = Pipeline([
#     ("model", KNeighborsRegressor(n_neighbors=5))
# ])
# pred = pipe.fit(X_train, y_train).predict(X_test)
#
# ## Plotting to check
# # plt.figure(figsize=(10, 6))
# # plt.scatter(X_test, pred, label='prediction')
# # plt.scatter(X_test, y_test, label='test')
# # plt.ylabel('price')
# # plt.xlabel('area')
# # plt.legend()
#
#
# pipe.get_params()
# mod = GridSearchCV(estimator=pipe,
#                    param_grid={
#                        'model__n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#                    },
#                    cv=5)
#
# mod.fit(X_test, y_test);
#
# data = pd.DataFrame(mod.cv_results_)
#
# pipe = Pipeline([("model", KNeighborsRegressor(n_neighbors=10))
#         ])
#
# pred = pipe.fit(X_train, y_train).predict(X_test)
# # print (pred)
#
# packaged_object = [] #TODO fill it
# #save packaged_object to a fill prediction.p
# outfile = open ("prediction.p", 'wb')
# joblib.dump(packaged_object, outfile)
# outfile.close()