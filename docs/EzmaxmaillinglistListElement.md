# EzmaxmaillinglistListElement

A Ezmaxmaillinglist List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxmaillinglist_id** | **int** | The unique ID of the Ezmaxmaillinglist | 
**s_ezmaxmaillinglist_name_x** | **str** | The name of the Ezmaxmaillinglist in the language of the requester | 
**s_ezmaxmaillinglist_description_x** | **str** | The description of the Ezmaxmaillinglist in the language of the requester | 
**b_ezmaxmaillinglist_subscribed** | **bool** | Whether the user subscribed to this Ezmaxmaillinglistor not | 

## Example

```python
from eZmaxApi.models.ezmaxmaillinglist_list_element import EzmaxmaillinglistListElement

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxmaillinglistListElement from a JSON string
ezmaxmaillinglist_list_element_instance = EzmaxmaillinglistListElement.from_json(json)
# print the JSON string representation of the object
print(EzmaxmaillinglistListElement.to_json())

# convert the object into a dict
ezmaxmaillinglist_list_element_dict = ezmaxmaillinglist_list_element_instance.to_dict()
# create an instance of EzmaxmaillinglistListElement from a dict
ezmaxmaillinglist_list_element_from_dict = EzmaxmaillinglistListElement.from_dict(ezmaxmaillinglist_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


