# CorsResponse

A Cors Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_cors_id** | **int** | The unique ID of the Cors | 
**fki_apikey_id** | **int** | The unique ID of the Apikey | 
**s_cors_entryurl** | **str** | The entryurl of the Cors | 

## Example

```python
from eZmaxApi.models.cors_response import CorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CorsResponse from a JSON string
cors_response_instance = CorsResponse.from_json(json)
# print the JSON string representation of the object
print(CorsResponse.to_json())

# convert the object into a dict
cors_response_dict = cors_response_instance.to_dict()
# create an instance of CorsResponse from a dict
cors_response_from_dict = CorsResponse.from_dict(cors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


