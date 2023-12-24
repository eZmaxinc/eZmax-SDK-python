# VersionhistoryResponseCompound

A Versionhistory Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_versionhistory_id** | **int** | The unique ID of the Versionhistory | 
**fki_module_id** | **int** | The unique ID of the Module | [optional] 
**fki_modulesection_id** | **int** | The unique ID of the Modulesection | [optional] 
**s_module_name_x** | **str** | The Name of the Module in the language of the requester | [optional] 
**s_modulesection_name_x** | **str** | The Name of the Modulesection in the language of the requester | [optional] 
**e_versionhistory_usertype** | [**FieldEVersionhistoryUsertype**](FieldEVersionhistoryUsertype.md) |  | [optional] 
**obj_versionhistory_detail** | [**MultilingualVersionhistoryDetail**](MultilingualVersionhistoryDetail.md) |  | 
**dt_versionhistory_date** | **str** | The date  at which the Versionhistory was published or should be published | 
**dt_versionhistory_dateend** | **str** | The date  at which the Versionhistory will no longer be visible | [optional] 
**e_versionhistory_type** | [**FieldEVersionhistoryType**](FieldEVersionhistoryType.md) |  | 
**b_versionhistory_draft** | **bool** | Whether the Versionhistory is published or still a draft | 

## Example

```python
from eZmaxApi.models.versionhistory_response_compound import VersionhistoryResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of VersionhistoryResponseCompound from a JSON string
versionhistory_response_compound_instance = VersionhistoryResponseCompound.from_json(json)
# print the JSON string representation of the object
print VersionhistoryResponseCompound.to_json()

# convert the object into a dict
versionhistory_response_compound_dict = versionhistory_response_compound_instance.to_dict()
# create an instance of VersionhistoryResponseCompound from a dict
versionhistory_response_compound_form_dict = versionhistory_response_compound.from_dict(versionhistory_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


