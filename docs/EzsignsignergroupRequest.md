# EzsignsignergroupRequest

A Ezsignsignergroup Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignsignergroup_id** | **int** | The unique ID of the Ezsignsignergroup | [optional] 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**obj_ezsignsignergroup_description** | [**MultilingualEzsignsignergroupDescription**](MultilingualEzsignsignergroupDescription.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsignergroup_request import EzsignsignergroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupRequest from a JSON string
ezsignsignergroup_request_instance = EzsignsignergroupRequest.from_json(json)
# print the JSON string representation of the object
print(EzsignsignergroupRequest.to_json())

# convert the object into a dict
ezsignsignergroup_request_dict = ezsignsignergroup_request_instance.to_dict()
# create an instance of EzsignsignergroupRequest from a dict
ezsignsignergroup_request_from_dict = EzsignsignergroupRequest.from_dict(ezsignsignergroup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


