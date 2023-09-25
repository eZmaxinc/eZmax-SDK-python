# CustomFormDataEzsignformfieldgroupResponse

An FormDataSigner->Ezsignformfieldgroup Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezsignformfieldgroup_label** | **str** | The Label for the Ezsignformfieldgroup | 
**a_obj_ezsignformfield** | [**List[CustomFormDataEzsignformfieldResponse]**](CustomFormDataEzsignformfieldResponse.md) |  | 

## Example

```python
from eZmaxApi.models.custom_form_data_ezsignformfieldgroup_response import CustomFormDataEzsignformfieldgroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFormDataEzsignformfieldgroupResponse from a JSON string
custom_form_data_ezsignformfieldgroup_response_instance = CustomFormDataEzsignformfieldgroupResponse.from_json(json)
# print the JSON string representation of the object
print CustomFormDataEzsignformfieldgroupResponse.to_json()

# convert the object into a dict
custom_form_data_ezsignformfieldgroup_response_dict = custom_form_data_ezsignformfieldgroup_response_instance.to_dict()
# create an instance of CustomFormDataEzsignformfieldgroupResponse from a dict
custom_form_data_ezsignformfieldgroup_response_form_dict = custom_form_data_ezsignformfieldgroup_response.from_dict(custom_form_data_ezsignformfieldgroup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


