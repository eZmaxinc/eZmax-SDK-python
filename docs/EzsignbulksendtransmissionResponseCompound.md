# EzsignbulksendtransmissionResponseCompound

An Ezsignbulksendtransmission Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsignfoldertransmission** | [**List[CustomEzsignfoldertransmissionResponse]**](CustomEzsignfoldertransmissionResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendtransmission_response_compound import EzsignbulksendtransmissionResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendtransmissionResponseCompound from a JSON string
ezsignbulksendtransmission_response_compound_instance = EzsignbulksendtransmissionResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendtransmissionResponseCompound.to_json())

# convert the object into a dict
ezsignbulksendtransmission_response_compound_dict = ezsignbulksendtransmission_response_compound_instance.to_dict()
# create an instance of EzsignbulksendtransmissionResponseCompound from a dict
ezsignbulksendtransmission_response_compound_from_dict = EzsignbulksendtransmissionResponseCompound.from_dict(ezsignbulksendtransmission_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


