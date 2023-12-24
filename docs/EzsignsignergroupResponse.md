# EzsignsignergroupResponse

An Ezsignsignergroup Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignsignergroup_id** | **int** | The unique ID of the Ezsignsignergroup | 
**obj_ezsignsignergroup_description** | [**MultilingualEzsignsignergroupDescription**](MultilingualEzsignsignergroupDescription.md) |  | 
**s_ezsignsignergroup_description_x** | **str** | The Description of the Ezsignsignergroup in the language of the requester | [optional] 

## Example

```python
from eZmaxApi.models.ezsignsignergroup_response import EzsignsignergroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsignergroupResponse from a JSON string
ezsignsignergroup_response_instance = EzsignsignergroupResponse.from_json(json)
# print the JSON string representation of the object
print EzsignsignergroupResponse.to_json()

# convert the object into a dict
ezsignsignergroup_response_dict = ezsignsignergroup_response_instance.to_dict()
# create an instance of EzsignsignergroupResponse from a dict
ezsignsignergroup_response_form_dict = ezsignsignergroup_response.from_dict(ezsignsignergroup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


