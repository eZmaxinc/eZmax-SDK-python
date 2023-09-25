# DescriptionstaticResponseCompound

A Descriptionstatic Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_descriptionstatic_id** | **int** | The unique ID of the Descriptionstatic | 
**s_descriptionstatic_description** | **str** | The description of the Descriptionstatic | 

## Example

```python
from eZmaxApi.models.descriptionstatic_response_compound import DescriptionstaticResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptionstaticResponseCompound from a JSON string
descriptionstatic_response_compound_instance = DescriptionstaticResponseCompound.from_json(json)
# print the JSON string representation of the object
print DescriptionstaticResponseCompound.to_json()

# convert the object into a dict
descriptionstatic_response_compound_dict = descriptionstatic_response_compound_instance.to_dict()
# create an instance of DescriptionstaticResponseCompound from a dict
descriptionstatic_response_compound_form_dict = descriptionstatic_response_compound.from_dict(descriptionstatic_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


