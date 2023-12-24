# ApikeyResponseCompound

An Apikey Object and children to create a complete structure

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
from eZmaxApi.models.apikey_response_compound import ApikeyResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyResponseCompound from a JSON string
apikey_response_compound_instance = ApikeyResponseCompound.from_json(json)
# print the JSON string representation of the object
print ApikeyResponseCompound.to_json()

# convert the object into a dict
apikey_response_compound_dict = apikey_response_compound_instance.to_dict()
# create an instance of ApikeyResponseCompound from a dict
apikey_response_compound_form_dict = apikey_response_compound.from_dict(apikey_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


