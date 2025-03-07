# CustomEzsignfoldertypeTemplateResponse

A Custom Ezsignfoldertype Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignfoldertype_id** | **int** | The unique ID of the Ezsignfoldertype. | 
**b_ezsignfoldertype_allowdownloadproofezsignsigner** | **bool** | Whether we allow the proof to be downloaded by an Ezsignsigner | [optional] 

## Example

```python
from eZmaxApi.models.custom_ezsignfoldertype_template_response import CustomEzsignfoldertypeTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignfoldertypeTemplateResponse from a JSON string
custom_ezsignfoldertype_template_response_instance = CustomEzsignfoldertypeTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignfoldertypeTemplateResponse.to_json())

# convert the object into a dict
custom_ezsignfoldertype_template_response_dict = custom_ezsignfoldertype_template_response_instance.to_dict()
# create an instance of CustomEzsignfoldertypeTemplateResponse from a dict
custom_ezsignfoldertype_template_response_from_dict = CustomEzsignfoldertypeTemplateResponse.from_dict(custom_ezsignfoldertype_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


