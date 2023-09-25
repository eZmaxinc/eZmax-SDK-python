# CustomFormDataSignerResponse

A form Data Signer Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | 
**fki_user_id** | **int** | The unique ID of the User | [optional] 
**s_contact_firstname** | **str** | The First name of the contact | 
**s_contact_lastname** | **str** | The Last name of the contact | 
**a_obj_ezsignformfieldgroup** | [**List[CustomFormDataEzsignformfieldgroupResponse]**](CustomFormDataEzsignformfieldgroupResponse.md) |  | 

## Example

```python
from eZmaxApi.models.custom_form_data_signer_response import CustomFormDataSignerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFormDataSignerResponse from a JSON string
custom_form_data_signer_response_instance = CustomFormDataSignerResponse.from_json(json)
# print the JSON string representation of the object
print CustomFormDataSignerResponse.to_json()

# convert the object into a dict
custom_form_data_signer_response_dict = custom_form_data_signer_response_instance.to_dict()
# create an instance of CustomFormDataSignerResponse from a dict
custom_form_data_signer_response_form_dict = custom_form_data_signer_response.from_dict(custom_form_data_signer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


