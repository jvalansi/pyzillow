from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

with open(fpath, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')


address = 'YOUR ADDRESS'
zipcode = 'YOUR ZIPCODE'
...
zillow_data = ZillowWrapper(YOUR_ZILLOW_API_KEY)
deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
result = GetDeepSearchResults(deep_search_response)
...
result.zillow_id # zillow id, needed for the GetUpdatedPropertyDetails
