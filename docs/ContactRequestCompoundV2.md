# ContactRequestCompoundV2

A Contact Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_contactinformations** | [**ContactinformationsRequestCompoundV2**](ContactinformationsRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.contact_request_compound_v2 import ContactRequestCompoundV2

# TODO update the JSON string below
json = "{}"
# create an instance of ContactRequestCompoundV2 from a JSON string
contact_request_compound_v2_instance = ContactRequestCompoundV2.from_json(json)
# print the JSON string representation of the object
print(ContactRequestCompoundV2.to_json())

# convert the object into a dict
contact_request_compound_v2_dict = contact_request_compound_v2_instance.to_dict()
# create an instance of ContactRequestCompoundV2 from a dict
contact_request_compound_v2_from_dict = ContactRequestCompoundV2.from_dict(contact_request_compound_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


