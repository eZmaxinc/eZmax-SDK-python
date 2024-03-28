# EzsignbulksendtransmissionResponse

An Ezsignbulksendtransmission Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsignbulksendtransmission_id** | **int** | The unique ID of the Ezsignbulksendtransmission | 
**fki_ezsignbulksend_id** | **int** | The unique ID of the Ezsignbulksend | 
**s_ezsignbulksendtransmission_description** | **str** | The description of the Ezsignbulksendtransmission | 
**i_ezsignbulksendtransmission_errors** | **int** | The number of errors during the Ezsignbulksendtransmission | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksendtransmission_response import EzsignbulksendtransmissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendtransmissionResponse from a JSON string
ezsignbulksendtransmission_response_instance = EzsignbulksendtransmissionResponse.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendtransmissionResponse.to_json())

# convert the object into a dict
ezsignbulksendtransmission_response_dict = ezsignbulksendtransmission_response_instance.to_dict()
# create an instance of EzsignbulksendtransmissionResponse from a dict
ezsignbulksendtransmission_response_form_dict = ezsignbulksendtransmission_response.from_dict(ezsignbulksendtransmission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


