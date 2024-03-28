# MultilingualUserlogintypeDescription

The description of the Userlogintype

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_userlogintype_description1** | **str** | The description of the Userlogintype in French | [optional] 
**s_userlogintype_description2** | **str** | The description of the Userlogintype in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_userlogintype_description import MultilingualUserlogintypeDescription

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualUserlogintypeDescription from a JSON string
multilingual_userlogintype_description_instance = MultilingualUserlogintypeDescription.from_json(json)
# print the JSON string representation of the object
print(MultilingualUserlogintypeDescription.to_json())

# convert the object into a dict
multilingual_userlogintype_description_dict = multilingual_userlogintype_description_instance.to_dict()
# create an instance of MultilingualUserlogintypeDescription from a dict
multilingual_userlogintype_description_form_dict = multilingual_userlogintype_description.from_dict(multilingual_userlogintype_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


