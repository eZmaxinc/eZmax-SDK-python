# EzsignbulksendtransmissionResponseCompound

An Ezsignbulksendtransmission Object and children to create a complete structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksendtransmission_id** | **int** | The unique ID of the Ezsignbulksendtransmission | 
**fki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | 
**s_ezsignbulksendtransmission_description** | **str** | The description of the Ezsignbulksendtransmission | 
**i_ezsignbulksendtransmission_errors** | **int** | The number of errors during the Ezsignbulksendtransmission | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 
**a_obj_ezsignfoldertransmission** | [**List[CustomEzsignfoldertransmissionResponse]**](CustomEzsignfoldertransmissionResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendtransmission_response_compound import EzsignbulksendtransmissionResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendtransmissionResponseCompound from a JSON string
ezsignbulksendtransmission_response_compound_instance = EzsignbulksendtransmissionResponseCompound.from_json(json)
# print the JSON string representation of the object
print EzsignbulksendtransmissionResponseCompound.to_json()

# convert the object into a dict
ezsignbulksendtransmission_response_compound_dict = ezsignbulksendtransmission_response_compound_instance.to_dict()
# create an instance of EzsignbulksendtransmissionResponseCompound from a dict
ezsignbulksendtransmission_response_compound_form_dict = ezsignbulksendtransmission_response_compound.from_dict(ezsignbulksendtransmission_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


