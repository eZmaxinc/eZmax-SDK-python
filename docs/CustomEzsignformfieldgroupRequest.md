# CustomEzsignformfieldgroupRequest

A Custom Ezsignformfieldgroup Object to fill an Ezsignform using submitForm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignformfieldgroup_id** | **int** | The unique ID of the Ezsignformfieldgroup | [optional] 
**s_ezsignformfieldgroup_label** | **str** | The Label for the Ezsignformfieldgroup | [optional] 
**a_obj_ezsignformfield** | [**List[CustomEzsignformfieldRequest]**](CustomEzsignformfieldRequest.md) | An array containing all the values to fill the Ezsignform. | 

## Example

```python
from eZmaxApi.models.custom_ezsignformfieldgroup_request import CustomEzsignformfieldgroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignformfieldgroupRequest from a JSON string
custom_ezsignformfieldgroup_request_instance = CustomEzsignformfieldgroupRequest.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignformfieldgroupRequest.to_json())

# convert the object into a dict
custom_ezsignformfieldgroup_request_dict = custom_ezsignformfieldgroup_request_instance.to_dict()
# create an instance of CustomEzsignformfieldgroupRequest from a dict
custom_ezsignformfieldgroup_request_from_dict = CustomEzsignformfieldgroupRequest.from_dict(custom_ezsignformfieldgroup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


