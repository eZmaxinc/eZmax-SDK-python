# DescriptionstaticResponse

A Descriptionstatic Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_descriptionstatic_id** | **int** | The unique ID of the Descriptionstatic | 
**s_descriptionstatic_description** | **str** | The description of the Descriptionstatic | 

## Example

```python
from eZmaxApi.models.descriptionstatic_response import DescriptionstaticResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptionstaticResponse from a JSON string
descriptionstatic_response_instance = DescriptionstaticResponse.from_json(json)
# print the JSON string representation of the object
print DescriptionstaticResponse.to_json()

# convert the object into a dict
descriptionstatic_response_dict = descriptionstatic_response_instance.to_dict()
# create an instance of DescriptionstaticResponse from a dict
descriptionstatic_response_form_dict = descriptionstatic_response.from_dict(descriptionstatic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


