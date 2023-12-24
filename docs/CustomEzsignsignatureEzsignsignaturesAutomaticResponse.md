# CustomEzsignsignatureEzsignsignaturesAutomaticResponse

An Ezsignsignature Object in the context of an EzsignsignaturesAutomatic path

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignsignature_id** | **int** | The unique ID of the Ezsignsignature | 
**e_ezsignsignature_type** | [**FieldEEzsignsignatureType**](FieldEEzsignsignatureType.md) |  | 
**i_ezsignpage_pagenumber** | **int** | The page number in the Ezsigndocument | 

## Example

```python
from eZmaxApi.models.custom_ezsignsignature_ezsignsignatures_automatic_response import CustomEzsignsignatureEzsignsignaturesAutomaticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignsignatureEzsignsignaturesAutomaticResponse from a JSON string
custom_ezsignsignature_ezsignsignatures_automatic_response_instance = CustomEzsignsignatureEzsignsignaturesAutomaticResponse.from_json(json)
# print the JSON string representation of the object
print CustomEzsignsignatureEzsignsignaturesAutomaticResponse.to_json()

# convert the object into a dict
custom_ezsignsignature_ezsignsignatures_automatic_response_dict = custom_ezsignsignature_ezsignsignatures_automatic_response_instance.to_dict()
# create an instance of CustomEzsignsignatureEzsignsignaturesAutomaticResponse from a dict
custom_ezsignsignature_ezsignsignatures_automatic_response_form_dict = custom_ezsignsignature_ezsignsignatures_automatic_response.from_dict(custom_ezsignsignature_ezsignsignatures_automatic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


