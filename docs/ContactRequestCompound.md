# ContactRequestCompound

A Contact Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_contactinformations** | [**ContactinformationsRequestCompound**](ContactinformationsRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.contact_request_compound import ContactRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of ContactRequestCompound from a JSON string
contact_request_compound_instance = ContactRequestCompound.from_json(json)
# print the JSON string representation of the object
print(ContactRequestCompound.to_json())

# convert the object into a dict
contact_request_compound_dict = contact_request_compound_instance.to_dict()
# create an instance of ContactRequestCompound from a dict
contact_request_compound_from_dict = ContactRequestCompound.from_dict(contact_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


