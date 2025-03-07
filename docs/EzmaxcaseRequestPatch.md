# EzmaxcaseRequestPatch

An Ezmaxcase Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezmaxcasequeue_id** | **int** | The unique ID of the Ezmaxcasequeue | [optional] 
**fki_ezmaxcasepriority_id** | **int** | The unique ID of the Ezmaxcasepriority | [optional] 
**fki_ezmaxcasestate_id** | **int** | The unique ID of the Ezmaxcasestate | [optional] 
**fki_ezmaxfeaturerequest_id** | **int** | The unique ID of the Ezmaxfeaturerequest | [optional] 
**fki_ezmaxknownissue_id** | **int** | The unique ID of the Ezmaxknownissue | [optional] 
**fki_user_id_owner** | **int** | The unique ID of the User | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxcase_request_patch import EzmaxcaseRequestPatch

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxcaseRequestPatch from a JSON string
ezmaxcase_request_patch_instance = EzmaxcaseRequestPatch.from_json(json)
# print the JSON string representation of the object
print(EzmaxcaseRequestPatch.to_json())

# convert the object into a dict
ezmaxcase_request_patch_dict = ezmaxcase_request_patch_instance.to_dict()
# create an instance of EzmaxcaseRequestPatch from a dict
ezmaxcase_request_patch_from_dict = EzmaxcaseRequestPatch.from_dict(ezmaxcase_request_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


