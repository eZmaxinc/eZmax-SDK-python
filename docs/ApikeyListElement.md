# ApikeyListElement

A Branding List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_apikey_id** | **int** | The unique ID of the Apikey | 
**s_apikey_description_x** | **str** | The description of the Apikey in the language of the requester | 
**s_user_firstname** | **str** | The first name of the user | 
**s_user_lastname** | **str** | The last name of the user | 
**b_apikey_isactive** | **bool** | Whether the apikey is active or not | 
**b_apikey_issigned** | **bool** | Whether the apikey is signed or not | 

## Example

```python
from eZmaxApi.models.apikey_list_element import ApikeyListElement

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyListElement from a JSON string
apikey_list_element_instance = ApikeyListElement.from_json(json)
# print the JSON string representation of the object
print(ApikeyListElement.to_json())

# convert the object into a dict
apikey_list_element_dict = apikey_list_element_instance.to_dict()
# create an instance of ApikeyListElement from a dict
apikey_list_element_from_dict = ApikeyListElement.from_dict(apikey_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


