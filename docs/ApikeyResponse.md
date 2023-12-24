# ApikeyResponse

An Apikey Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_apikey_id** | **int** | The unique ID of the Apikey | 
**fki_user_id** | **int** | The unique ID of the User | 
**obj_apikey_description** | [**MultilingualApikeyDescription**](MultilingualApikeyDescription.md) |  | 
**obj_contact_name** | [**CustomContactNameResponse**](CustomContactNameResponse.md) |  | 
**s_apikey_apikey** | **str** | The Apikey for the API key.  This will be hidden if we are not creating or regenerating the Apikey. | [optional] 
**s_apikey_secret** | **str** | The Secret for the API key.  This will be hidden if we are not creating or regenerating the Apikey. | [optional] 
**b_apikey_isactive** | **bool** | Whether the apikey is active or not | 
**b_apikey_issigned** | **bool** | Whether the apikey is signed or not | [optional] 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_response import ApikeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyResponse from a JSON string
apikey_response_instance = ApikeyResponse.from_json(json)
# print the JSON string representation of the object
print ApikeyResponse.to_json()

# convert the object into a dict
apikey_response_dict = apikey_response_instance.to_dict()
# create an instance of ApikeyResponse from a dict
apikey_response_form_dict = apikey_response.from_dict(apikey_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


