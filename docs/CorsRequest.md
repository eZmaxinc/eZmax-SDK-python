# CorsRequest

A Cors Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_cors_id** | **int** | The unique ID of the Cors | [optional] 
**fki_apikey_id** | **int** | The unique ID of the Apikey | 
**s_cors_entryurl** | **str** | The entryurl of the Cors | 

## Example

```python
from eZmaxApi.models.cors_request import CorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CorsRequest from a JSON string
cors_request_instance = CorsRequest.from_json(json)
# print the JSON string representation of the object
print CorsRequest.to_json()

# convert the object into a dict
cors_request_dict = cors_request_instance.to_dict()
# create an instance of CorsRequest from a dict
cors_request_form_dict = cors_request.from_dict(cors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


