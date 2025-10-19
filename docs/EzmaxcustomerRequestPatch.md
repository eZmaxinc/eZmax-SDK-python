# EzmaxcustomerRequestPatch

A Ezmaxcustomer Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezmaxcustomer_note** | [**MultilingualEzmaxcustomerNote**](MultilingualEzmaxcustomerNote.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxcustomer_request_patch import EzmaxcustomerRequestPatch

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxcustomerRequestPatch from a JSON string
ezmaxcustomer_request_patch_instance = EzmaxcustomerRequestPatch.from_json(json)
# print the JSON string representation of the object
print(EzmaxcustomerRequestPatch.to_json())

# convert the object into a dict
ezmaxcustomer_request_patch_dict = ezmaxcustomer_request_patch_instance.to_dict()
# create an instance of EzmaxcustomerRequestPatch from a dict
ezmaxcustomer_request_patch_from_dict = EzmaxcustomerRequestPatch.from_dict(ezmaxcustomer_request_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


