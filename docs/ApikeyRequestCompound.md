# ApikeyRequestCompound

An Apikey Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_apikey_id** | **int** | The unique ID of the Apikey | [optional] 
**fki_user_id** | **int** | The unique ID of the User | 
**obj_apikey_description** | [**MultilingualApikeyDescription**](MultilingualApikeyDescription.md) |  | 
**b_apikey_isactive** | **bool** | Whether the apikey is active or not | [optional] 
**b_apikey_issigned** | **bool** | Whether the apikey is signed or not | [optional] 

## Example

```python
from eZmaxApi.models.apikey_request_compound import ApikeyRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyRequestCompound from a JSON string
apikey_request_compound_instance = ApikeyRequestCompound.from_json(json)
# print the JSON string representation of the object
print ApikeyRequestCompound.to_json()

# convert the object into a dict
apikey_request_compound_dict = apikey_request_compound_instance.to_dict()
# create an instance of ApikeyRequestCompound from a dict
apikey_request_compound_form_dict = apikey_request_compound.from_dict(apikey_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


