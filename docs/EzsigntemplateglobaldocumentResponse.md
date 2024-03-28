# EzsigntemplateglobaldocumentResponse

A Ezsigntemplateglobaldocument Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplateglobaldocument_id** | **int** | The unique ID of the Ezsigntemplateglobaldocument | 
**s_ezsigntemplateglobaldocument_name** | **str** | The name of the Ezsigntemplateglobaldocument. | 
**i_ezsigntemplateglobaldocument_pagetotal** | **int** | The number of pages in the Ezsigntemplateglobaldocument. | 
**i_ezsigntemplateglobaldocument_signaturetotal** | **int** | The number of total signatures in the Ezsigntemplateglobal. | 

## Example

```python
from eZmaxApi.models.ezsigntemplateglobaldocument_response import EzsigntemplateglobaldocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateglobaldocumentResponse from a JSON string
ezsigntemplateglobaldocument_response_instance = EzsigntemplateglobaldocumentResponse.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateglobaldocumentResponse.to_json())

# convert the object into a dict
ezsigntemplateglobaldocument_response_dict = ezsigntemplateglobaldocument_response_instance.to_dict()
# create an instance of EzsigntemplateglobaldocumentResponse from a dict
ezsigntemplateglobaldocument_response_form_dict = ezsigntemplateglobaldocument_response.from_dict(ezsigntemplateglobaldocument_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


