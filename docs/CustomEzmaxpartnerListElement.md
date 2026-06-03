# CustomEzmaxpartnerListElement

A custom Ezmaxpartner List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxpartner_id** | **int** | The unique ID of the Ezmaxpartner | 
**s_ezmaxpartner_address_x** | **str** | The complete address in a single line | 
**s_ezmaxpartner_emailaddress_x** | **str** | The email address. | 
**s_ezmaxpartner_shortdescription_x** | **str** | The short description of the Ezmaxpartner in the language of the requester | 
**s_ezmaxpartner_name_x** | **str** | The name of the Ezmaxpartner in the language of the requester | 
**s_ezmaxpartner_phone_e164_x** | **str** | A phone number in E.164 Format | 
**s_ezmaxpartner_url_x** | **str** | The url of the Ezmaxpartner website in the language of the requester | 

## Example

```python
from eZmaxApi.models.custom_ezmaxpartner_list_element import CustomEzmaxpartnerListElement

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzmaxpartnerListElement from a JSON string
custom_ezmaxpartner_list_element_instance = CustomEzmaxpartnerListElement.from_json(json)
# print the JSON string representation of the object
print(CustomEzmaxpartnerListElement.to_json())

# convert the object into a dict
custom_ezmaxpartner_list_element_dict = custom_ezmaxpartner_list_element_instance.to_dict()
# create an instance of CustomEzmaxpartnerListElement from a dict
custom_ezmaxpartner_list_element_from_dict = CustomEzmaxpartnerListElement.from_dict(custom_ezmaxpartner_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


