# CustomEzsignformfielderrorResponse

A Custom Ezsignformfield Object to contain an error list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezsignformfield_label** | **str** | The Label for the Ezsignformfield | 
**a_obj_ezsignformfielderrortest** | **List[CustomEzsignformfielderrortestResponse]** |  | 

## Example

```python
from eZmaxApi.models.custom_ezsignformfielderror_response import CustomEzsignformfielderrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzsignformfielderrorResponse from a JSON string
custom_ezsignformfielderror_response_instance = CustomEzsignformfielderrorResponse.from_json(json)
# print the JSON string representation of the object
print(CustomEzsignformfielderrorResponse.to_json())

# convert the object into a dict
custom_ezsignformfielderror_response_dict = custom_ezsignformfielderror_response_instance.to_dict()
# create an instance of CustomEzsignformfielderrorResponse from a dict
custom_ezsignformfielderror_response_from_dict = CustomEzsignformfielderrorResponse.from_dict(custom_ezsignformfielderror_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


