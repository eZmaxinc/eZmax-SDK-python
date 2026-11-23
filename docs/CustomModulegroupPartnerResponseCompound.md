# CustomModulegroupPartnerResponseCompound

A Modulegroup Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_modulegroup_id** | **int** | The unique ID of the Modulegroup | 
**s_modulegroup_name_x** | **str** | The name of the Modulegroup in the language of the requester | 
**a_obj_module** | [**List[CustomModulePartnerResponseCompound]**](CustomModulePartnerResponseCompound.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.custom_modulegroup_partner_response_compound import CustomModulegroupPartnerResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of CustomModulegroupPartnerResponseCompound from a JSON string
custom_modulegroup_partner_response_compound_instance = CustomModulegroupPartnerResponseCompound.from_json(json)
# print the JSON string representation of the object
print(CustomModulegroupPartnerResponseCompound.to_json())

# convert the object into a dict
custom_modulegroup_partner_response_compound_dict = custom_modulegroup_partner_response_compound_instance.to_dict()
# create an instance of CustomModulegroupPartnerResponseCompound from a dict
custom_modulegroup_partner_response_compound_from_dict = CustomModulegroupPartnerResponseCompound.from_dict(custom_modulegroup_partner_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


