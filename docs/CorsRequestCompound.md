# CorsRequestCompound

A Cors Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_cors_id** | **int** | The unique ID of the Cors | [optional] 
**fki_apikey_id** | **int** | The unique ID of the Apikey | 
**s_cors_entryurl** | **str** | The entryurl of the Cors | 

## Example

```python
from eZmaxApi.models.cors_request_compound import CorsRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CorsRequestCompound from a JSON string
cors_request_compound_instance = CorsRequestCompound.from_json(json)
# print the JSON string representation of the object
print(CorsRequestCompound.to_json())

# convert the object into a dict
cors_request_compound_dict = cors_request_compound_instance.to_dict()
# create an instance of CorsRequestCompound from a dict
cors_request_compound_from_dict = CorsRequestCompound.from_dict(cors_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


